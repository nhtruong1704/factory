import requests


def test_get_all_factories(url: str):
    res = requests.get(url).json()
    assert (res == [{'factories_id': 1,
     'name': 'SpaceX',
     'description': 'Founded by Elon Musk, SpaceX is an American aerospace manufacturer and space transportation company.',
     'country': 'United States',
     'age': 'Space exploration, satellite manufacturing, rocket engineering'},
    {'factories_id': 2,
     'name': 'Boeing',
     'description': 'Boeing is an American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, telecommunications equipment, and missiles worldwide.',
     'country': 'United States',
     'age': 'Aerospace, defense, rotorcraft'},
    {'factories_id': 3,
     'name': 'Lockheed Martin',
     'description': 'Lockheed Martin is an American aerospace, defense, arms, security, and advanced technologies company.',
     'country': 'United States',
     'age': 'Aerospace, defense, security, advanced technologies'},
    {'factories_id': 4,
     'name': 'Airbus',
     'description': 'Airbus SE is a European multinational aerospace corporation that designs, manufactures, and sells civil and military aeronautical products worldwide.',
     'country': 'Europe',
     'age': 'Aerospace, defense, helicopters'},
    {'factories_id': 5,
     'name': 'Northrop Grumman',
     'description': 'Northrop Grumman Corporation is an American multinational aerospace and defense technology company.',
     'country': 'United States',
     'age': 'Aerospace, defense, technology'}])


def test_get_factory_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'factories_id': 1,
     'name': 'SpaceX',
     'description': 'Founded by Elon Musk, SpaceX is an American aerospace manufacturer and space transportation company.',
     'country': 'United States',
     'age': 'Space exploration, satellite manufacturing, rocket engineering'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/factories/'
    test_get_factory_by_id(URL + '1')
    test_get_all_factories(URL)
