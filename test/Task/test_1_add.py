import requests

def test_add():
    body = {"title":"тестовая задача","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

    assert response.status_code == 200

    id = response.json()['id']

    body = {"completed": True}
    response = requests.patch(f"https://todo-app-sky.herokuapp.com/{id}", json=body)

    assert response.status_code == 200
    assert response.json()["completed"] == True

    #тест прошел успешно