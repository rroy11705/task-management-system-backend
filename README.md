# Task Management System Backend

A simple Task Management System built with Django and Graphene.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This project is a Task Management System developed using Django and Graphene, providing a flexible and efficient way to manage tasks, statuses and labels.

## Features

- CRUD operations for tasks, statuses and labels
- GraphQL API for efficient data retrieval and manipulation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rroy11705/task-management-system-backend.git
   ```

2. Install dependencies:

    ```
    bash
    cd task-management-system
    pip install -r requirements.txt
    ```
3. Run migrations:

    ```
    bash
    python manage.py migrate
    ```

4. Create a superuser account (for admin access):

    ```
    bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```
    bash
    python manage.py runserver
    ```


## Usage

1. Access the admin interface to manage users, tasks, and labels:

    ```
    bash
    http://localhost:8000/admin/
    ```

2. Access the GraphQL API explorer for interactive queries and mutations:

    ```
    bash
    http://localhost:8000/graphql/
    ```
