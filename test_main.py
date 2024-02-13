import requests


def test_get_request():
    url = 'http://127.0.0.1:8000/visited_domains'
    response = requests.get(url)
    assert response.status_code == 200


def test_get_bad_request():
    url = 'http://127.0.0.1:8000/visited_domains?from=1707320188&to=1707235203'
    response = requests.get(url)
    assert response.status_code == 400


def test_post_request():
    url = 'http://127.0.0.1:8000/visited_links'
    data = {"links": ["https://ya.ru/", "https://sber.ru"]}
    response = requests.post(url, json=data)
    assert response.status_code == 200
