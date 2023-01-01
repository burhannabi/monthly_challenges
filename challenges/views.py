from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges={
    "january":"Eat no meat for entire month",
    "february":"Walk for 10 mins",
    "march":"Jump for 30 mins",
    "april":"yoga for entire season",
    "may":"take a doctor checkup",
    "june":"listen motivational videos every month",
    "july":"Eat no meat for entire month",
    "august":"Walk for 10 mins",
    "september":"Jump for 30 mins",
    "october":"yoga for entire season",
    "november":"take a doctor checkup",
    "december":None,

}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()   
        


