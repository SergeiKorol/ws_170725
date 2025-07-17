import requests

def test_get_tasks_():
    response = requests.get("https://todo-app-sky.herokuapp.com/")
    assert response.status_code == 200
    assert type(response.json()) is list