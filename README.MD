# HEALTY test task

Games recommendation API

## Run locally


```bash
pip install -r requirements.py
python wsgi.py
```

or with Docker
```bash
docker build -t healthy-test-task:build-tag-1
docker run -p 8080:80 healthy-test-task:build-tag-1  
```

## APIs

```python
/user - CRUD for users
/auth - authorize endpoint
/genres - GRUD for genres
/games - games API
/games/recommendations - recommendations API
```

