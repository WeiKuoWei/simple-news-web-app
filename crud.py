from models import articles
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from models import articles

# session is a medium for communicating with the database ayync_sessionmaker and
# AsyncSession are used to create a session, which contribute to effective
# asynchronous database management, enhancing performance and scalability by
# efficiently handling concurrent database operations without blocking.

class CRUD:
    async def get_all_articles(self, aync_session: async_sessionmaker[AsyncSession]):
        async with aync_session() as session:
            statement = select(articles).order_by(articles.id)

            result = await session.execute(statement)

            return result.scalars().all() # returns a list of all the articles
        
    async def get_article(self, article_id: int, aync_session: async_sessionmaker[AsyncSession]):
        async with aync_session() as session:
            statement = select(articles).where(articles.id == article_id)

            result = await session.execute(statement)

            return result.scalars().first()
        
    async def create_article(self, article: articles, aync_session: async_sessionmaker[AsyncSession]):
        async with aync_session() as session:
            session.add(article)
            await session.commit()

            await session.refresh(article)
            return article