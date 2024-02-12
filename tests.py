import requests


def test_get_request():
    response = requests.get('http://127.0.0.1:8000/visited_domains')
    assert response.status_code == 200


def test_get_bad_request():
    response = requests.get('http://127.0.0.1:8000/visited_domains?from=1707320188&to=1707235203')
    assert response.status_code == 400


def test_post_request():
    data = {"links": ["https://ya.ru/", "https://sber.ru"]}
    response = requests.post('http://127.0.0.1:8000/visited_links', json=data)
    assert response.status_code == 200
