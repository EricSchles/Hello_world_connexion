# Hello World with Connexion

Hello!  And welcome to this bare bones microservice.  It contains two files (that are relevant):

* app.py
* swagger.yaml

Getting started:

To get started simply run:

`python -m pip install pipenv`


`pipenv install -r requirements.txt`


`pipenv run python app.py` 

The above steps install pipenv (our virtual environment), install our dependencies (found in requirements.txt), and run our server, found in app.py

## How it works

`connexion` is a great tool and works very similarly to flask, in that you specify routes in a python file, usually called app.py for small apps and a way to specify routes.  The routes are specified in a seperate file in this case, called swagger.yaml.  However, you can use any name you like for the yaml file, in general.  We reference the yaml file in app.py as:

`app.add_api`

This specification allows us to use our yaml file as a specification for our api.  It's important to note, that what goes into our yaml file matters.  You specify the routes you want your api to call here, as well as the python code that runs said file.  In order to connect python code to a end point specified in the yaml file include the following lines in your specification:

```
paths:
  /name_of_route:
    http_method:
       tags: [defined types that get returned separated by commas]
       operationId: filename.function_name <-- this is the magic!!!
```

By specifying the operationId it connections the python function to the api end point, and then you are good to go.  Why do things this way you might be asking yourself?  Aren't decorator annotations on apps better?!  

Well the honest answer is yes, if your application is small.  But the whole point of microservices is that you trade complexity at the endpoint level for complexity across the application.  This isn't better or worse, it's case specific.  But if you are building thousands of endpoints, this is definitely better, because remembering where everything goes and how it all gets specified and having to search across the entire code base is tough.  
Having the ease of going to a centralized file that's going to make sense to anyone (even if they don't read python) is a good thing.  This way your front end and backend engineers can coordinate without learning everything the other knows.  So it's a very good thing.


