# Bioservice

Python version: `3.6.5`

## Setup Project:

- Configure the `.env` file with your project variables
```bash
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
SECRET_KEY=""
ENVIRONMENT_MODULE=""


# Email settings
EMAIL_HOST=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_PORT="587"
EMAIL_USE_TLS="True"
```

- Set `ENVIRONMENT_MODULE` in `.env` file, alternatives are: `develop`, `staging` and `production`.

## Dependencies:

#### Common.in:

1. psycopg2-binary
    - Install `postgresql` on your system

#### Dev.in:

1. pygraphviz
    - Install `graphviz` on your system
