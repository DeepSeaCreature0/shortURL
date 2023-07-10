#### LOCAL SETUP
1. Install virtualenv
      `pip install virtualenv`

2. create/activate virtualenv
   - create 
        `virtualenv venv`

    - activate:
        `source venv/Scripts/activate`

3.  Install packages mentioned in requirement.txt:
    - `pip install -r requirements.txt`

4.  Update environment file (.env)
    -`source .env`

5. create database named <DB_NAME> same as metioned in environment file in mysql database.
    -`CREATE DATABASE <DB_NAME> `
   
7. Migrate changes
    -`python manage.py makemigrations`
    -`python3 manage.py migrate` 
        
8. Start app 
    -`python manage.py runserver`

---

#### END_POINTS:
    <HOST_URL> - html page rendered with a simple  user-friendly form input
    <HOST_URL>/url/   - support [GET,POST] - use POST to create new URL and GET to receive list of all URLS in DB.
    <HOST_URL>/url/<id>

---
#### ENVIRONMENT FILE
    - HOST_IP=127.0.0.1     
    - HOST_PORT=8000
    - HOST_URL=${HOST_IP}:${HOST_PORT}
    
    - DB_NAME='short_urls'
    - DB_USER='' 
    - DB_PASSWORD=''




    


