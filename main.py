# https://www.youtube.com/watch?v=nC9ob8xM3AM&t=1133s


from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from http import HTTPStatus
from pandas import pd
import uuid

from crud import CRUD
from db import engine
from schemas import ArticleModel, ArticleCreateModel
from typing import List
from models import articles


app = FastAPI(
    title="Simple News API",
    description="A simple API to read news articles",
    docs_url="/"
)

session = async_sessionmaker(
    bind = engine, 
    expire_on_commit = False
)

db = CRUD()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/articles', response_model=List[ArticleModel])
async def get_all_articles():
    return await db.get_all_articles(session)

@app.get('articles/{article_id}')
async def get_articles(article_id: int):
    return await db.get_article(article_id, session)

@app.post('/articles', status_code=HTTPStatus.CREATED)
async def create_article(article_data: ArticleCreateModel):
    # new_article = articles(**article.dict())
    new_article = articles(
        # id = int(uuid.uuid4()),
        title = article_data.title,
        authors = article_data.authors,
        url = article_data.url,
        date_publish = article_data.date_publish,
        description = article_data.description,
        maintext = article_data.maintext,
        wayback_time = article_data.wayback_time,
        # date_created = article_data.date_created
    )

    article = await db.create_article(new_article, session)

    return article

@app.get('/{csv_name}')
async def upload_articles_from_csv(csv_name: str):
    df = pd.read_csv(csv_name)
    for _, row in df.iterrows():
        article_data = ArticleCreateModel(
            title=row['title'],
            authors=row['authors'],
            url=row['url'],
            date_publish=row['date_publish'],
            description=row['description'],
            maintext=row['maintext'],
            wayback_time=pd.to_datetime(row['wayback_time'])
        )
        # Encode to JSON compatible format and create article
        article_data = jsonable_encoder(article_data)
        await create_article(article_data)