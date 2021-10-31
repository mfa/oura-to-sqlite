# Oura export to sqlite

![Tests](https://github.com/mfa/oura-to-sqlite/workflows/Tests/badge.svg)

## About

Export all your data from oura into sqlite.
The code is tested with a Gen2 oura ring account.


## Authentication

This app needs a "Personal Access Token".
Setup yours here: <https://cloud.ouraring.com/personal-access-tokens>
Copy ``oura_to_sqlite/secrets.json.template`` to ``oura_to_sqlite/secrets.json``.
And add your token to ``oura_to_sqlite/secrets.json``


## install

```
python setup.py install
```


## Download everything

Either set token via cli:
```
oura-to-sqlite <db_path> --token <token>
```

or via environment:
```
export OURA_PAT=ABC...
oura-to-sqlute <db_path>
```


## Use with [Datasette](https://github.com/simonw/datasette)

install Datasette:

```
pip install datasette
```

run with Datasette:

```
datasette my_oura.db
```


## Thanks

[Simon Willison](https://simonwillison.net/) for Datasette and sqlite-utils.
