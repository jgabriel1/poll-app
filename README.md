# poll-app

It's a simple web application for creating and voting in polls:
* The user can create a poll with however many options they choose;
* they can also choose if they want it to accept multiple votes from each voter;
* upon creation, the poll will be stored in a database and an url will be generated;
* the creator can share that url with the people they wish to inquire;
* upon finishing voting, the voter will be able to see the results of the poll.

## Technoligies used on the project:

* ### **Frontend:** JavaScript on NodeJS with server side rendering using [ReactJS](https://reactjs.org/) framework;

* ### **Backend:** RESTful API using Python and the [FastAPI](https://fastapi.tiangolo.com/) framework;

* ### **Database:** [MongoDB](https://www.mongodb.com/) with an [Atlas](https://www.mongodb.com/cloud/atlas) cloud-hosted cluster.

## For the Backend:
In the ``backend`` folder, create and activate a virtual environment by running:
```
$ python -m venv venv
$ source venv/bin/activate
```
On **Windows**, use:
```
PS> venv\Scripts\Activate.ps1
```

Run to install all the dependencies with ``pip``:
```
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
Start the backend server by running:
```
$ uvicorn app:app
```
or:
```
$ python run.py
```
The server will run by default on http://localhost:8000/

### Using [Poetry](https://python-poetry.org/):
You can alternatively use poetry as dependency manager. It automatically creates and activates the virtual environment for you!

Install dependencies:
```
$ poetry install
```
Run the server:
```
$ poetry run start
```

### For the Database:
It will look for an environment variable called ``MONGO_URL`` in a ``.env`` file on the root ``backend`` directory. That will point to your cluster in Atlas. If the environment variable does not exist, it will use the default port for a ``mongod`` server running in your machine.

## For the Frontend:
In the ``frontend`` folder, install all the dependencies by running:
```
$ npm install
```
Run the **React** server:
```
$ npm start
```
The server will run by default on http://localhost:3333/


<br>

This is an application built for educational purposes. The main goals are learning how these tecnologies work and personal growth as a developer.
