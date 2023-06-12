# Docker python

[tutorial](https://docs.docker.com/language/python/run-containers/)
[tutorial](https://docs.docker.com/language/python/run-containers/)

Install poetry
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

```python
poetry run python index.py
```

```sh
docker compose up -f compose.dev.yaml --build
```

## Dependencies

Docker
poetry

beautifulsoup
requests
psycopg3
schedule
