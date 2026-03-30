from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from calendar import monthrange
from datetime import datetime

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    

    return render(request, "tasks/index.html", {
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
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
