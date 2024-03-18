import requests

url = 'https://api.pokemonbattle.me/v2'
headers_pokemons = {'trainer_token': 'd0389a404899bfab290662aff7dc3f9e'}


def create_pokemons_func():
    create_pokemon = requests.post(f'{url}/pokemons', headers=headers_pokemons,
                                   json={'name': 'generate', 'photo': 'generate'})
    dict_create_pokemon = create_pokemon.json()
    # dict_create_pokemon=dict(eval(create_pokemon.text)) то же самое что и на предыдущей строке. попробовал через text

    return int(dict_create_pokemon['id'])


def update_pokemon():
    change_name_pokemon = requests.put(f'{url}/pokemons', headers=headers_pokemons,
                                       json={'pokemon_id': f'{id_pok}', 'name': 'PIKACHU',
                                             'photo': 'https://dolnikov.ru/pokemons/albums/527.png'})


def in_pokeball_pokemon():
    in_pokeball = requests.post(f'{url}/trainers/add_pokeball', headers=headers_pokemons,
                                json={'pokemon_id': f'{id_pok}'})

# id_pok=create_pokemons_func()
# update=update_pokemon()
# inpok=in_pokeball_pokemon()
