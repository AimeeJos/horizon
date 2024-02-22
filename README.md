
# About Project
## Horizon Press

 Horizon Press is a media organization. The organization expresses an interest in using pre-trained models and further refining the model through custom retraining if deemed necessary.

 This  web application is for creating sentiment analysis and a text classifier of sentences given by the user. WE used the Transformer library’s pipeline module to do sentiment analysis and text classification.

 

## Tech Stack

##### Frontend
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

##### Backend

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

##### Database

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Run Locally

Clone the project

```bash
  git clone https://github.com/AimeeJos/horizon.git
  cd horizon
```

Build docker image.

```bash
  docker compose build
```

Start the server

```bash
  docker compose up
```
Run the server:

```bash
  https://localhost:8000
```

###### Add the first sentence, and wait for the models to load.
  
Create superuser:

```bash
   docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

Admin Panel 
```bash
 https://localhost:8000/admin
```

######  Tables/Models 
- Categories
- Sentences



