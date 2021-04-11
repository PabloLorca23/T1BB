from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import requests





def index(request):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    r = r.json()
    temporadas_bb = []
    temporadas_bcs = []
    for i in r:
        if i['series'] == "Breaking Bad":
            temporadas_bb.append(i['season'])
        else:
            temporadas_bcs.append(i['season'])

    temporadas_bb = sorted(list(set(temporadas_bb)))
    temporadas_bcs = sorted(list(set(temporadas_bcs)))
    context = {
        'temporadas_bb': temporadas_bb,
        'temporadas_bcs': temporadas_bcs
    }
    return render(request, 'bbAPI/index.html', context)


def capitulo(request,serie, temporada):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    r = r.json()
    context = { 'temporada': temporada,
        'r': r,
        'serie': serie
    }
    return render(request, 'bbAPI/capitulo.html', context)

def episodio(request,serie, temporada, episodio):
    r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    r = r.json()
    context = { 'temporada': temporada,
        'r': r,
        'serie': serie,
        'episodio': episodio
    }
    return render(request, 'bbAPI/episodio.html', context)

def personaje(request, personaje):
    if personaje == "buscar":
        personaje = request.POST[personaje]
        p2 = personaje.replace(" ", "+")
        p = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+p2)
        p = p.json()
        print(p)
        personaje = "Personajes con nombres similares"
        q = 0


    else:
        p2 = personaje.replace(" ", "+")
        p = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+p2)
        p = p.json()
        p[0]['category']=p[0]['category'].split(",")
        print(p[0]['better_call_saul_appearance'])
        payload = {'author': p[0]['name']}
        q = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote', params=payload)
        q = q.json()
        if len(q) == 0:
            q= [{"quote":"Este personaje no cuenta con frases que valga la pena recordar"}]
    context = {
        'p': p,
        'personaje': personaje,
        'q': q
    }
    return render(request,'bbAPI/personaje.html', context)


