# To-Do Task Manager

## Overview
The To-Do Task Manager is a simple command-line application that allows users to manage tasks effectively. Users can add, view, modify, delete, search tasks, and generate task completion reports. The application is password-protected to restrict unauthorized access.

## Features
- Password protection with limited login attempts.
- Add new tasks with description, due date, and status (pending, in-progress, complete).
- View all tasks in a tabular format.
- Modify task details.
- Delete tasks by ID.
- Generate summary reports showing total tasks and count by status.
- Search tasks by keywords or status.

## Usage
1. Run the program.
2. Enter the password to access the task manager (`task123` by default).
3. Use the menu to choose actions:
    - Add Task
    - View Tasks
    - Modify Task
    - Delete Task
    - Generate Report
    - Search Tasks
    - Exit

## Task Status Options
- pending
- in-progress
- complete

## Requirements
- Python 3.x

## Notes
- Password attempts are limited to 3.
- Invalid task status entries default to "pending".
- Dates should be entered in the format `YYYY-MM-DD`.

## Author
Vaishnavi Jaswal  
Enrollment No.: 2502140092

