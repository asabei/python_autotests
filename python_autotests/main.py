import requests
url='https://api.pokemonbattle.me/v2'
headers_pokemons={'trainer_token':'d0389a404899bfab290662aff7dc3f9e'}
create_pokemon=requests.post(f'{url}/pokemons', headers=headers_pokemons, json={'name': 'generate', 'photo': 'generate'} )
print(create_pokemon.json())
dict_create_pokemon=create_pokemon.json()
#dict_create_pokemon=dict(eval(create_pokemon.text)) то же самое что и на предыдущей строке. попробовал через text
change_name_pokemon=requests.put(f'{url}/pokemons', headers=headers_pokemons, json={'pokemon_id':f'{dict_create_pokemon['id']}','name': 'PIKACHU', 'photo':'https://dolnikov.ru/pokemons/albums/527.png'})
print(change_name_pokemon.json())
in_pokeball=requests.post(f'{url}/trainers/add_pokeball', headers=headers_pokemons, json={'pokemon_id':f'{dict_create_pokemon['id']}'})
print(in_pokeball.json())