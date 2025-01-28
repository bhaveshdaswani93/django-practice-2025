from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

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
  'december': None
}

def feb(request):
  return HttpResponse('<p>Feb Month </p>')
  
def monthly_challenge_by_number(request, month):
  month_name_list = list(monthly_challenges.keys())
  
  if month > len(month_name_list):
    return HttpResponseNotFound('Month not found')
  
  month_name = month_name_list[month - 1]
  redirect_path = reverse('monthly-challenge', args=[month_name])
  return redirect(redirect_path)
  #return HttpResponse(f'month number {month}')
  
def monthly_challenge(request, month):
  try:
    month_res =  f'<h1>{monthly_challenges[month]}</h1>'
    return render(request, 'challenges/challenge.html', {
      'text': monthly_challenges[month],
      'month': month
    })
    #template_html = render_to_string('challenges/challange.html')
    #return HttpResponse(template_html)
  except:
    return HttpResponseNotFound('<h1>Monthly Challenge not fount</h1>')
  
def index(request):
  list_items = ''
  months = list(monthly_challenges.keys())
  for month in months:
    month_path = reverse('monthly-challenge', args=[month])
    list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
  response_data = f'<ul>{list_items}</ul>'
  return render(request, 'challenges/index.html', {
    'months': months
  })
 # return HttpResponse(response_data)
  
  