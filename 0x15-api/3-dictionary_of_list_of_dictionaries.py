#!/usr/bin/python3
"""
This script uses REST API to gather TODO list progress for all employees.
It then exports the data in JSON format.
"""
import json
import requests
import sys


def get_todo_all_employees():
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        all_tasks = {}

        for user in users_data:
            user_id = user['id']
            user_name = user['username']
            todos_url = f'{base_url}/todos?userId={user_id}'
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            tasks = [
                {"username": user_name, "task": task['title'],
                "completed": task['completed']}
                for task in todos_data
                ]
            all_tasks[user_id] = tasks
        export_to_json(all_tasks)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_json(data):
    filename = "todo_all_employees.json"
    
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    get_todo_all_employees()
