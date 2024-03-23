import requests
import pytest
url='https://api.pokemonbattle.me/v2'
headers_pokemons={'trainer_token':'               '}
def test_response_200():
    response_get=requests.get(f'{url}/trainers?trainer_id=253', headers=headers_pokemons)
    json_data=response_get.json()
    assert response_get.status_code==200, 'ok'
    list_data=json_data['data']
    dict_data=list_data[0]
    assert dict_data['trainer_name']=='asabei', 'ok'
