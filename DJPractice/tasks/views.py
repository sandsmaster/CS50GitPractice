from django.shortcuts import render
from calendar import monthrange
from datetime import datetime

tasks = ["Clean Fridge", "Clean Bathroom", "Shave Mustache"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks":tasks
    })

def add(request):
    return render(request, "tasks/add.html")

def stats(request):
    cal_range = calc_calendar_range()    

    return render(request, "tasks/stats.html", {
        "days_in_month":cal_range[0],
        "days_last_month":cal_range[1] 
    })

def calc_calendar_range():
    '''
    cmd => curr_month_days
    lmd => last_month_days
    '''
    now = datetime.now()
    if now.month == 1:  # If it's january
        cmd = monthrange(now.year, now.month)   # take january
        lmd = monthrange(now.year - 1, 12) # and dec last year
    else:
        cmd = monthrange(now.year, now.month)
        lmd = monthrange(now.year, now.month - 1)

    return [
        range(1, cmd[1] + 1),
        range(lmd[1] - cmd[0] + 1, lmd[1]+1)
    ]