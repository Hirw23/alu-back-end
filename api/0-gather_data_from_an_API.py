#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Fetch employee information
    employee_url = f'{base_url}/users/{employee_id}'
    employee_response = requests.get(employee_url)
    
    if employee_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return
    
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')
    
    # Fetch employee's TODO list
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Calculate TODO list progress
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)
    
    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: The employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)

