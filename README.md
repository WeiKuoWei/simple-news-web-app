# simple-news-web-app
## basics:
Running the app:
```zsh
uvicorn main:app --reload
# app is the name of the FastAPI instance in main.py
# --reload flag is for auto-reloading the server on code changes
```

Access parameters from .env
```zsh
pip install python-dotenv
```
```python
load_dotenv()

engine = create_async_engine(
    # sensitive data
    url = os.getenv("DATABASE_URL")
    encho = True
)
```