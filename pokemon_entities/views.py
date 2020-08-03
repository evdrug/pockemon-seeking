from datetime import datetime

import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render

from pokemon_entities.models import Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    # with open("pokemon_entities/pokemons.json", encoding="utf-8") as database:
    #     pokemons = json.load(database)['pokemons']
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in pokemon.pokemonentity_set.filter(
                appeared_at__lte=datetime.now(),
                disappeared_at__gte=datetime.now()):
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon.title,
                request.build_absolute_uri(f'/media/{pokemon.image}'))

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.pk,
            'img_url': request.build_absolute_uri(f'/media/{pokemon.image}'),
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(pk=pokemon_id)

    except Pokemon.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.pokemonentity_set.filter(
                appeared_at__lte=datetime.now(),
                disappeared_at__gte=datetime.now()):
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon.title,
            request.build_absolute_uri(f'/media/{pokemon.image}'))

    formatting_pokemon = {
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'img_url': request.build_absolute_uri(f'/media/{pokemon.image}'),
    }
    if pokemon.previous_evolution:
        formatting_pokemon['previous_evolution'] = {
            'pokemon_id': pokemon.previous_evolution_id,
            'title_ru': pokemon.previous_evolution.title,
            'img_url': request.build_absolute_uri(
                f'/media/{pokemon.previous_evolution.image}'),
        }
    next_pokemon = pokemon.next_evolution.first()
    if next_pokemon:
        formatting_pokemon['next_evolution'] = {
            'pokemon_id': next_pokemon.id,
            'title_ru': next_pokemon.title,
            'img_url': request.build_absolute_uri(
                f'/media/{next_pokemon.image}'),
        }

    return render(request, "pokemon.html",
                  context={'map': folium_map._repr_html_(),
                           'pokemon': formatting_pokemon})
