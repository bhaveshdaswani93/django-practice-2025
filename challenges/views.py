from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

monthly_challenges = {
  'january': 'Jan Challenge',
  'feburary': 'Feb Challenge',
  'march': 'March Challenge',
  'april': 'April Challenge',
  'may': 'May Challenge',
  'june': 'June Challenge',
  'july': 'July Challenge',
  'august': 'August Challenge',
  'september': 'September Challenge',
  'october': 'October Challenge',
  'november': 'November Challenge',
  'december': 'December Challenge'
}

# Create your views here.
def index(request):
  return HttpResponse('<p>Hello world</p>')

def feb(request):
  return HttpResponse('<p>Feb Month </p>')
  
def monthly_challenge_by_number(request, month):
  month_name_list = list(monthly_challenge.keys())
  
  if month > len(month_name_list):
    return HttpResponseNotFound('Month not found')
  
  month_name = month_name_list[month - 1]
  redirect_path = reverse('monthly-challenge', args=[month_name])
  return redirect(redirect_path)
  #return HttpResponse(f'month number {month}')
  
def monthly_challenge(request, month):
   try:
    month_res =  monthly_challenge[month]
      return HttpResponse(res)
    except:
       return HttpResponseNotFound('Monthly Challenge not fount')
  
  