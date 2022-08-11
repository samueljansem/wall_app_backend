## How to run this project

### Requirements:

-   python3
-   python3-pip
-   python3-venv

#### Create your virtual environment:

```shell
$ python3 -m venv venv
```

#### Activate your virtual environment:

```shell
$ source venv/bin/activate
```

#### Install required packages on your virtual environment:

```shell
$ python3 -m pip install -r requirements.txt
```

#### Run migrations:

```shell
$ python3 manage.py migrate
```

#### Run the project:

```shell
$ python3 manage.py runserver
```

## References

-   https://docs.djangoproject.com/en/4.1/
-   https://www.django-rest-framework.org/tutorial/quickstart/
-   https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
-   https://github.com/adamchainz/django-cors-headers
