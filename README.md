# Link Shorter
A URL shortener project implemented using Django Rest Framework for creating shortened links.

![Main Page](https://github.com/DeepSeaCreature0/shortURL/assets/138828627/7062c034-5a9a-4278-a3a3-51db0d849ada)

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

<hr/>

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

# Key Points
### No length Restriction:
* There is no limit on URL length. For that purpose we are not using inbuild URL_FIELD feature , because most of them provide support upto 200 char limit and some upto 1000. We will receive free text from user and validate url on server end.
### No loss of URL by formatters:
* Almost all formatter target non-alphanumeric value for formatting. In order to avoid this issue we will generate hashed_url with only alphanumeric values.
### Link Tracker
* We will also manage no. of times user clicked the valid short url

<hr/>

#### APPROCH 1
>https://HOST_NAME/<short_hash_string>
     
1. Basic idea is to generate random short_hash_string string of length (6)
2. Check if 
    - this short_hash_string is not present in DB then insert short_hash_string into DB with actual_url mapping with hit_count=0.
    - If this  short_hash_string is present , repeat step 1 
 
    
##### Limitation on this approch
>for every new request we have look over DB to check wether currently generated string is present in DB or not which is not efficent if try to scale it.

<hr/>

#### APPROCH 2 (Applied on this project):
>https://HOST_NAME/<short_hash_string>

*For this  project length of short_hash_string is >=1 and <=6*

>*This is the respresentation of our schema*

| ID | actual_url | short_hash_string | hit_count
| ----------- | ----------- | ----------- | -----------
| 1 | https://www.youtube.com/ | hash1  | 0
| 2 | https://www.youtube.com/ | hash2  | 2
| n | nth_URL | nth_hash | 102

    
    There are 62 alphanumeric charactor and x is one of alphanumeric charactor
    short_hash_string  combinations
    x                  = 62   
    xx                 = 62*62 = 3844 
    xxx                = 62*62*62 = 246016 
    xxxx               = 62*62*62*62 = 15252992 
    xxxxx              = 62*62*62*62*62 = 945685504  
    xxxxxx             = 62*62*62*62*62*62 = 58632501248  

    -We can provide diffrent url upto 58632501248 (sum of above combination) if we just insert (short_hash_string --> actual_url) mapping without looking for short_hash_string in DB and just increment the primary key ID.
    
    - Now our problem shorten to 'generate a unqiue hash for a interger' and 'to revert back to integer from this generated unique_hash' .
