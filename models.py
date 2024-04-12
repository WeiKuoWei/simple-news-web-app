from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from datetime import datetime

'''
    "title", "authors", "url", "date_publish", "description", "maintext", "wayback_time"
'''
class articles(Base):
    __tablename__ = "articles"

    # consider defining id with string and using uuid
    id : Mapped[int] = mapped_column(primary_key=True) # this is a newer way to define columns; traditional would be id = Column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(nullable=False)
    authors : Mapped[str] = mapped_column()
    url : Mapped[str] = mapped_column(nullable=False) 
    date_publish : Mapped[str] = mapped_column()
    description : Mapped[str] = mapped_column(Text)
    maintext : Mapped[str] = mapped_column(Text, nullable=False)
    # wayback_time : Mapped[datetime] = mapped_column(default = datetime)
    wayback_time : Mapped[str] = mapped_column()
    date_created : Mapped[datetime] = mapped_column(default = datetime.utcnow) 

    def __repr__(self) -> str:
        return f"<Article {self.title} at {self.wayback_time}>"