# EBANX project by Lucas Dionatan Torres

### How to execute this project

This project requires:
    
   * Python 3.11

You can execute the project with two options:
- Using Docker compose
- Instaling the all necessary packages

## Using Docker
run the command bellow in project terminal:
```
docker compose up
```

## installation
1 - Install dependencies
We need install project dependencies with `poetry`:
###### obs: Can you install poetry in [this link](https://python-poetry.org/docs/)

```
 poetry install
```

3 - Execute the virtualenv

```
poetry shell
```

4 - Execute the project server:

```
uvicorn apps.main:app --reload
```

- Update dependencies:

```
poetry update
```

- Run tests:

```
pytest
```

## Test result with ipkiss:
![270216886-88976d05-e6a3-4deb-b27f-3ae1ebc59885](https://github.com/lucasldtdionatan/ebanx-test/assets/55671737/00723197-6a97-4d90-b220-ee9ab7d88c5f)
