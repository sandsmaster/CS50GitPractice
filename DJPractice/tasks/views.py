from django.shortcuts import render

tasks = ["Clean Fridge", "Clean Bathroom", "Shave Mustache"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html")