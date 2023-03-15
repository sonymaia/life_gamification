from django.shortcuts import render
from record.models import Daily_Record
import pandas as pd


def index(request):
     return render(request, 'record/index.html')

def scoreboard(request): 
    #Daily_Records = {
    #    'Daily_Records': Daily_Record.objects.all().values('date','fk_user').order_by('fk_user','date')
    #}
    
    Daily_Records = Daily_Record.objects.all().values('date','fk_user').order_by('fk_user','date')
    table = pd.DataFrame(Daily_Records)
    print(Daily_Records)
    print(table)

    group_table = table.value_counts()
    print(table.value_counts())
    
    dict = {}
    coins = 0
    for row in group_table.items():
        user = row[0][1]
        count = row[1]

        if count >= 3:
            if len(dict) == 0 or not dict.get(user):
                dict[user] = 1
            else:
                dict[user] += 1

    print(dict)

    for row in dict:
        print('Resultado1:', row)
        print('Resultado2:', dict[row])
        





    #print(Daily_Records)
    return render(request, 'record/scoreboard.html')