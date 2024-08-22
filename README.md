## Deployment

I've deploy this project on render.com. You can try this API link that i deployed on Postman:

Link: 

https://recommendation-api-4an0.onrender.com


The JSON Request Format: 

{

    "title": "(movie-full-title)"

}

Example:

- {

        "title": "Spider-Man"

    }

- {

        "title": "The Dark Knight Rises"
    
    }


## Documentation

Visit documentation by click this link

[Documentation](https://github.com/XiaoDreT/movie-recommendation-system)


## Run Locally

### Notes:

In this project, the version of python is 3.11.9 also using the conda environtment, you can using "virtualenv" by python or using "conda" environtment. It can be helpful for deploy the Recommendation API

Clone the project

```
  $ git clone https://github.com/XiaoDreT/recommendation-api
```

Go to the project directory

```
  $ cd recommendation-api
```

Install dependencies

```
  $ pip install -r requirements.txt

  or 

  $ pip install pandas scikit-learn flask gunicorn
```

Start the server

```
  $ python recommendation_api.py
```
