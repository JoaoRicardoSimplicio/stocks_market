Stocks Market
===========

Platform for measuring stocks

## Installation

### Backend

First, enter the folder

```bash
    $ cd market-backend/
```

Next, setup the postgres container with docker:

```bash
    $ docker-compose up -d
```

Now create a virtual environment and install the required packages with the following commands:

```bash
    $ virtualenv env --python=python3.8     # Create a virtual environment called env
    $ source env/bin/activate               # Activate the environment
    (env) $ pip install -r requirements.txt # Install the required packages
```

Create migrations

```bash
    $ python3 manage.py migrate
```

Now, Update stocks price extracted from websites

```bash
    $ python3 manage.py stocks_update_prices
```

Run your local server:

```bash
    $ python3 manage.py runserver
```

To extract stocks and just show in terminal

```bash
    $ python3 manage.py stocks_extract_prices
```


### Frontend

First, enter the folder

```bash
    $ cd market-frontend/
```

Next, install the dependencies

```bash
    $ npm install
```

Now, run your application react

```bash
    $ npm start
```

**NOTE**: For the correct functioning of your react application it is necessary to run the local backend server
