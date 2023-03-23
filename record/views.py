from django.shortcuts import render
from record.models import Daily_Record, User, Goal, Category, Category_Record, Gift
import pandas as pd
from django.db.models import Sum 
from datetime import datetime

def index(request):
     return render(request, 'record/index.html')

def scoreboard(request): 
    #Search all users in the database
    UsersList = User.objects.all()
    dict = {}
    #create dictionary with users dict = {userId:adding default number for the coins = 0}
    for user in UsersList:
       dict[user.id] = 0

    #Search the records in the database
    Daily_Records = Daily_Record.objects.all().values('date','fk_user').order_by('fk_user','date')

    #Convert to table in pandas
    table = pd.DataFrame(Daily_Records)

    #creates a new table grouping the repeated items and showing the number of repeated items per line
    group_table = table.value_counts()

  
    #analyzing how many times the user met the daily goals
    #the idea is to create a dictionary with this structure
    #dict = {userId: number of times records were grouped more than 3 times}
    for row in group_table.items():
        user = row[0][1]
        count = row[1]
        if count >= 3:
            if len(dict) == 0 or not dict.get(user):
                dict[user] = 1
            else:
                dict[user] += 1

    #Creates list containing dictionaries that contain the {user_name: name, coins: Number of Points}
    #Exemple scoreboard = [{'user_name': 'joao', 'coins': 3}, {'user_name': 'maria', 'coins': 1}]}
    scoreboardlist = []
    for row  in dict.items():
        id_user = row[0]
        daily_goals_coins = row[1]
        total_coins = daily_goals_coins
        categories_summary_list = []

        #Searching for the user's completed goals and adding the rewards with the daily goal coins
        goals = Goal.objects.filter(fk_user=id_user, done=True)
        goals_reward_total = goals.aggregate(Sum('reward'))['reward__sum']
        if goals_reward_total is not None:
            total_coins += goals_reward_total
        else:
            goals_reward_total = 0
        
        
        categories_list = Category.objects.all() 
        category_records_list = Category_Record.objects.all()
        
        for category in categories_list:
            category_reward = category.reward

            category_records_qty = category_records_list.filter(fk_user=id_user, fk_category=category).count()
            category_reward_total =  (category_records_qty * category_reward)
            total_coins += category_reward_total
            
            dict_category = {'category_name':category.name, 'category_records_qty':category_records_qty, 'category_reward_total':category_reward_total}
            categories_summary_list.append(dict_category)

        dict_category = {'category_name':'Daily Goals', 'category_records_qty':daily_goals_coins, 'category_reward_total':daily_goals_coins}
        categories_summary_list.append(dict_category)
        
        dict_category = {'category_name':' Extra Goals', 'category_records_qty':goals.count(), 'category_reward_total':goals_reward_total}
        categories_summary_list.append(dict_category)
        
        unused_gifts, gifts_used = gifts(id_user, total_coins)

        scoreboardlist.append({'user_name':User.objects.filter(id=id_user).get().name, 
                               'coins':total_coins,
                               'categories_list':categories_summary_list,
                               'unused_gifts':unused_gifts,
                               'gifts_used':gifts_used
                               })

    
    scoreboard = {'scoreboard': scoreboardlist}
    
    return render(request, 'record/scoreboard.html', scoreboard)

def gifts(user_id, total_coins):    
    total_gifts = int(total_coins/30)
    gifts_db = Gift.objects.filter(fk_user = user_id).count() 
    gifts_used = 0
    unused_gifts = 0

    difference = total_gifts - gifts_db

    while difference > 0:
        gift = Gift()
        gift.creation_date = datetime.today()
        gift.fk_user = User.objects.get(id = user_id)
        gift.save()
        difference -= 1
  

    gifts_used = Gift.objects.filter(fk_user = user_id, conclusion_date__isnull=False).count() 
    unused_gifts = Gift.objects.filter(fk_user = user_id, conclusion_date__isnull=True ).count() 

    return unused_gifts, gifts_used
