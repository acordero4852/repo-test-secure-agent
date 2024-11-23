import requests

API_URL = "http://127.0.0.1:8000/api/tasks/"


def get_tasks():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return []


def create_task(title, description, completed):
    data = {"title": title, "description": description, "completed": completed}
    response = requests.post(API_URL, json=data)
    return response.status_code == 201


def update_task(task_id, title, description, completed):
    data = {"title": title, "description": description, "completed": completed}
    response = requests.put(f"{API_URL}{task_id}/", json=data)
    return response.status_code == 200


def delete_task(task_id):
    response = requests.delete(f"{API_URL}{task_id}/")
    return response.status_code == 204
