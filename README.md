# Sales Management System (CRM)

Sales Management System (or CRM called inside the project) is Python project aimed to 
manage customer information and track sales opportunities.


## Architecture

The project is separated into 3 different packages:

- **CRM**: It's the basic and core module that django uses to store settings. Basically 
contains all the information related to how the server is built, as well as the different 
settings it might have.


- **Backend**: Backend module basically contains the different tables in our project (`models.py`)


- **API**: A simple and minimalistic API built with DjangoRestFramework (DRF) that serves the basic
CRUD operations on the database (retrieve, create, modify and delete) over the Customer and SaleOpportunity
models.


## Installation

All the code is built based on a multi container docker using docker-compose. Make sure you have 
docker compose v2 installed. Just run:
```
docker compose up
```

The first time you install the project, you will probably need to run the migrations, as well
as create a superuser to administrate the system (it will allow you to create also users for the
staff in your company):
```
# Apply the migrations, creating the db schema
docker compose run app python manage.py migrate

# Create a super user to start creating salesperson and access the admin
docker compose run app python manage.py createsuperuser
```


Checks to do:

1. Put in the browser: http://localhost:8000/admin/. Do you see the django administrator? Right!
2. Put in the browser: http://localhost:8000/api/v1/. Do you see the DRF interface? Perfect!
3. Run the tests of every part and check all is rolling fine:
```
docker compose run app python manage.py test
```


## Usage

### 1. Server / Django admin

The server is built with django, a really powerful framework that acts as ORM, as well as providing
some useful tools, like the admin. 

1. Create a couple users with the admin for your stuff (the salespeople)
2. You can create some services that your company offers that will help salespeople to track
easily the preferences of your customers
3. You can see the lists of the Customers and SaleOpportunities in a more tech-orientated way in the admin

---
### 2. API
API is build with DjangoRestFramework. I tried to keep it as simple as possible, so don't expect
any master DRF endpoints. Basically DSR offers native support for REST structure, so using ModelViewSets
will automatically enable the required behavior.

Access the browser GUI in: http://localhost:8000/api/v1/



## Deployment

The deployment realistically depends on how scalable and secure we want our infrastructure to be.
If we had only 1 machine (let's say an Amazon EC2), we could basically ssh to the server, and make a:

```
# SSH to the available server
ssh user@ip

# Clone the repo in the home of the user that will have the rights to run the project
git clone {REPO}

# Set up the correct env variables in the .env file
vim .env

# Build up the containers
docker compose up
```

Improvements:
- Use a dedicated machine for the storage (RDS)
- Do not use the default django wsgi server. Configure gunicorn or daphne instead, that will handle
more natively the requests from the API.
- Use Ansible to set up all the steps to take when deploying. Create a playbook that pulls the repo,
applies migrations, collects static data for the admin, and restart the wsgi workers if needed.
- Install some software monitoring for the server (if not included in the server provider), as
Monit, that helps to track when the system is down, running out of memory, etc.
- Use Amazon secrets to store the sensible information (for example the .ENV variables). Let Ansible
decrypt them when deploying.
- We could **deploy the images instead** of the code. This would add an extra security layer that all the packages
and libraries are exactly how they are meant to be, avoiding production-real-time issues when deploying.


## Development cycle

We could improve the development cycle with the following topics (not done in the test for time reasons):

- **Enable CI** in our git provider (let's say GitHub, using GitHub actions). This will enable the test command
on every PR, and we would ensure a QA in all our development cycle.
- **Enable CD** in our git provider (let's say Bitbucket, using the pipeline module). This will enable
the option for the developers to deploy the PRs once the development has been merged to the master branch.
- We could add a validation check on the formatting when doing PR. I personally use `black` (it's installed in the project)
with `blackd` inside Pycharm.
    ```
    # Run manually the formatting:
    docker compose run app black .
    ```


## Comments
I decided to implement this project with django because it basically provides most of the characteristics
needed by default. The drawback is that I feel that I didn't develop too much code. I basically showed
that I have enough knowledge to create a simple API with the basic CRUD endpoints, but I missed the
"programming" part, which it's one of the ones that I like the most.

IMHO, I would add in the test some "algorithmic" challenge, where the developers can show their OOO basics,
show some patterns, implement a clear domain and operations. Because nowadays, the existing tools can provide
a really simple ways of developing this APIS, and the price to create a project without using this tools is
not worth it.