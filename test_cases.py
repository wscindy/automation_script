import pytest
import requests

target_api = 'https://pokeapi.co/api/v2/pokemon/'


def test_01():
    response = requests.get(target_api + str(6))
    if response.status_code == 200:
        data = response.json()['name']
        print(f'✅ 第一題：\nMonster id: {data}')
        assert data == 'charizard'
    else:
        return print(f'Error: {response.status_code}')

def test_02():
    print('✅ 第二題：')
    for id in range(1, 21):

        response = requests.get(target_api + str(id))
        if response.status_code == 200:
            data = response.json()['types']
            data_name = response.json()['name']
            print(f'ID: {id}, NAME: {data_name}, Types: {data}')
        else:
            return print(f'Error: {response.status_code}')

    assert 'raticate' in data_name


def test_03():
    print('✅ 第三題：')
    pokeMon = []
    for id in range(1, 101):

        response = requests.get(target_api + str(id))
        if response.status_code == 200:
            if response.json()['weight'] < 50:
                data_name = response.json()['name']
                data_weight = response.json()['weight']
                pokeMon.append((data_name, data_weight))

        else:
            return print(f'Error: {response.status_code}')
    pokeMon.sort(key=lambda pokeMon: pokeMon[1], reverse=True)
    assert pokeMon[0][0] == "meowth"
    assert pokeMon[0][1] == 42
    print(pokeMon)