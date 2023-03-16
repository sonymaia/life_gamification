from django.shortcuts import render
from record.models import Daily_Record, User, Goal
import pandas as pd
from django.db.models import Sum


def index(request):
     return render(request, 'record/index.html')

def scoreboard(request): 
    #Search the records in the database
    Daily_Records = Daily_Record.objects.all().values('date','fk_user').order_by('fk_user','date')
    
    #Convert to table in pandas
    table = pd.DataFrame(Daily_Records)

    #creates a new table grouping the repeated items and showing the number of repeated items per line
    group_table = table.value_counts()
  
    #analyzing how many times the user met the daily goals
    #the idea is to create a dictionary with this structure
    #{userId: number of times records were grouped more than 3 times}
    dict = {} 
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
        coins = row[1]

        #Searching for the user's completed goals and adding the rewards with the daily goal coins
        rewards = Goal.objects.filter(fk_user=id_user, done=True).aggregate(Sum('reward'))['reward__sum']
        if rewards is not None:
            coins += rewards

        scoreboardlist.append({'user_name':User.objects.filter(id=id_user).get().name, 'coins':coins}) 
    
    scoreboard = {'scoreboard': scoreboardlist}
    
    return render(request, 'record/scoreboard.html', scoreboard)