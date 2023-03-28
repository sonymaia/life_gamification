from record.models import Daily_Objective, Daily_Record
from datetime import datetime

#check all user's daily goals on the given date and 
#confirm whether it was true or false for each goal
#data={daily_goal_id:False or True}
def daily_goals_check(user, date):
    date_format = datetime.strptime(date, '%Y-%m-%d').date()
 
    objs = Daily_Record.objects.filter(fk_user=user, date=date_format)
    daily_goals = Daily_Objective.objects.all()
    data = {}

    for daily_goal in daily_goals:
        data[daily_goal.id] = objs.filter(fk_daily_obj=daily_goal.id).exists()
    
    return data