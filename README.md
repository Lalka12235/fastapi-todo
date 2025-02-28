## Deployment


Build
```bash
  docker build -t fastapi-todo .

```
Run
```bash
  docker run -d -p 8000:80 fastapi-todo

```
Run test 
```bash
  pytest tests/test_api.py::TestApi

```

