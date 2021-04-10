from django.shortcuts import render
from django.http import HttpResponse

import requests
from requests.exceptions import HTTPError
import json


# Vista principal, de inicio
def index(request):
  series = {}
  try:
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/')

  except HTTPError as err:
    series['error'] = err
    return render(request, "bbad/index.html", {"series":series})

  episodes = response.json()
  bb = 0
  bcs = 0
  bb_seasons = []
  bcs_seasons = []

  for i in range(len(episodes)):
    if episodes[i]['series'] == 'Breaking Bad':
      if int(episodes[i]['season']) > bb:
        bb = int(episodes[i]['season'])
        bb_seasons.append(bb)
    if episodes[i]['series'] == 'Better Call Saul':
      if int(episodes[i]['season']) > bcs:
        bcs = int(episodes[i]['season'])
        bcs_seasons.append(bcs)

  series['bb'] = bb_seasons
  series['bcs'] = bcs_seasons

  return render(request, "bbad/index.html", {"series":series})


# Vista de Breaking Bad
def breaking_bad(request, id):
  response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/')
  episodes = response.json()
  season = {}
  
  for i in range(len(episodes)):
    if episodes[i]['series'] == 'Breaking Bad':
      if int(episodes[i]['season']) == id:
        aux = {}
        aux['episode'] = episodes[i]['episode']
        aux['title'] = episodes[i]['title']
        aux['episode_id'] = episodes[i]['episode_id']
        season[episodes[i]['episode']] = aux

  season['id'] = id

  return render(request, "bbad/breaking_bad.html/", {"season": season})


def better_call_saul(request, id):
  response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/')
  episodes = response.json()
  season = {}
  
  for i in range(len(episodes)):
    if episodes[i]['series'] == 'Better Call Saul':
      if int(episodes[i]['season']) == id:
        aux = {}
        aux['episode'] = episodes[i]['episode']
        aux['title'] = episodes[i]['title']
        aux['episode_id'] = episodes[i]['episode_id']
        season[episodes[i]['episode']] = aux
  
  season['id'] = id

  return render(request, "bbad/better_call_saul.html/", {"season": season})


def episode(request, id):
  info = {}
  try:
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/')
    response.raise_for_status()
    print("\n", response.raise_for_status(), "\n")
  except HTTPError as err:
    info['error'] = err.response.text
    return render(request, "bbad/episode.html/", {'info': info})

  episodes = response.json()

  for i in range(len(episodes)):
    if int(episodes[i]['episode_id']) == id:
      info = episodes[i]

  return render(request, "bbad/episode.html/", {'info': info})

def character(request, name):
  response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters/?name=' + name)
  quotes = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=' + name).json()
  quote = []
  char = response.json()
  charr = char[0]
  aux = ''

  for i in charr['occupation']:
    aux += i 
    aux += ', '

  for i in range(len(quotes)):
    quote.append(quotes[i]['quote'])

  charr['occupation'] = aux
  charr['quotes'] = quote

  return render(request, "bbad/character.html/", {"charr": charr})


def search(request, name):
  response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters/?name=' + name)
  char = response.json()
  charr = char[0]
  aux = ''

  for i in charr['occupation']:
    aux += i 
    aux += ', '

  charr['occupation'] = aux

  return render(request, "bbad/search.html/", {})
  