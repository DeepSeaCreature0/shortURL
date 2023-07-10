# Link Shorter
A URL shortener project implemented using Django Rest Framework for creating shortened links.

# About
The URL Shortener project is a web application developed using Django Rest Framework (DRF) that allows users to shorten long URLs into shorter and more manageable links. This project utilizes a virtual environment for isolation and dependency management, and MySQL as the database system.

The main objective of the project is to provide a user-friendly interface where users can enter a long URL and generate a shorter version of it. This shortened URL will redirect users to the original long URL when accessed. The project involves the following components and features:

## API Endpoints:
The Django Rest Framework enables the creation of RESTful API endpoints that handle various operations, such as creating short URLs, retrieving original URLs, and handling redirects.

## URL Shortening Algorithm:
The project implements an algorithm that generates unique and short URL slugs. These slugs are used as the key for mapping the shortened URL to the original URL.

## Statistics:
The application can track usage statistics, such as the number of times a shortened URL has been accessed .

## Admin Interface:
Django provides an admin interface that allows administrators to manage the system, view analytics, and perform administrative tasks, such as URL deletion.

## Error Handling:
The project handles potential errors gracefully, such as invalid URLs and expired links, by providing appropriate error messages and responses.

# Environment Setup
* Install Django
* Install all the required packages in the req.txt using the command pip install -r req.txt
* Read Setup.md for further proceedings

# Tech Stack Used
* HTML
* CSS
* JavaScript
* Django
* Django Rest Framework (DRF)
* Virtual Environment
* MySQL
