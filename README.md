# A Django DRF URL Shortner
tags: `Django` `DjangoDRF` `SQLite` `URLShortner`

A simple URL shortener service that will accept a URL as an argument over a RESTAPI and return a shortened URL as a result.

## Steps To Use The API

### Requirements

The project requires [Python 3](https://www.python.org/downloads/release/python-396/) or higher and
the [PIP](https://pip.pypa.io/en/stable/) package manager.

### Install the project dependencies
Install dependencies from the project's requirements.txt as:
```console=1
$ pip3 install -r requirements.txt
```

:::info
**Note:** Put requirements.txt in the directory where the command will be executed. If it is in another directory, specify the path.
:::

### :pushpin: Initialize The Database
This application currently uses SQLiteDB. 
```console=1
$ python manage.py makemigrations
$ python manage.py migrate
```

### :no_entry: Perform Tests
Run all tests
```console=1
$ coverage run manage.py test
```

### Finally Run Application

If app is run locally, it will be listening on port `8000`.

```console
$ python3 manage.py runserver
```

## API Endpoints

1. Swagger Documentation - 
```
http://localhost:8000/swagger 
```

2. View All URLs 
```
http://localhost:8000/api/
```

3. Create Short Link - 
```
http://localhost:8000/api/create 
```

-- Abhishek Dev
