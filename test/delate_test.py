import requests


def test_delete():
    #  создаем  задачку
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

    assert response.status_code == 200

    id = response.json()["id"]

    delete_response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    # assert delete_response.status_code == 404

    response = requests.get(f"https://todo-app-sky.herokuapp.com/{id}")
    assert response.status_code == 404
