import json
import requests

def test_als_user_aanwezig_is_():
    response = requests.get('http://127.0.0.1:8000/persoon/1')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["voornaam"])== str
    assert type(response_dictionary["achternaam"]) == str

def test_als_er_geen_user_id_gevonden():
    response = requests.get('http://127.0.0.1:8000/persoon/20')
    assert response.status_code == 404

def test_opvragen_dat_in_alle_users_items_string():
    response = requests.get('http://127.0.0.1:8000/persoon/')
    assert response.status_code == 200
    response_dict = json.loads(response.text)
    for dict_run in response_dict[0]:
        assert type(dict_run[0]) == str


def test_beroepen_met_verkeerde_link():
    response = requests.get('http://127.0.0.1:8000/beroepde/')
    assert response.status_code == 404

def test_beroepen_testen_of_geslacht_STR():
    response = requests.get('http://127.0.0.1:8000/beroepen/')
    assert response.status_code == 200
    respond_list = json.loads(response.text)
    for lijst in respond_list[0]:
        assert type(lijst[1]) == str

def test_gelimiteerd_beroepen():
    response = requests.get('http://127.0.0.1:8000/beroepen/?skip=0&limit=50')
    assert response.status_code == 200

def test_personen():
    response = requests.get('http://127.0.0.1:8000/persoon/?skip=0&limit=50')
    assert response.status_code == 200