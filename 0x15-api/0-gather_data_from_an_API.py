#!/usr/bin/python3
"""
this script uses REST API for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]
        total_tasks = len(todos_data)

        print("Employee {} is done with tasks({}/{}):"
            .format(user_data['name'], len(completed_tasks), total_tasks))

        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee.id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
