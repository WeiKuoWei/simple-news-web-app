# this file is used to serialize the data from the database to a json format that can be used by the client.

from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ArticleModel(BaseModel):
    id: int
    title: str
    authors: str
    url: str
    date_publish: str
    description: str
    maintext: str
    # wayback_time: datetime
    wayback_time: str
    date_created: datetime

    model_config = ConfigDict(
        from_attributes=True,
        # orm_mode=True
    )


class ArticleCreateModel(BaseModel):
    # since id is or type uuid, and wayback_time is of datatime.utcnow, they are
    # not included in the create model as they are automatically generated
    
    title: str
    authors: str
    url: str
    date_publish: str
    description: str
    maintext: str
    # wayback_time: datetime
    wayback_time: str

    model_config = ConfigDict(
        from_attributes=True,
        # orm_mode=True,
        # shows up as the example in the swagger docs for Create Article
        json_schema_extra={
            "example": {
                "title": "The title of the article",
                "authors": "The authors of the article",
                "url": "The url of the article",
                "date_publish": "The date the article was published",
                "description": "A brief description of the article",
                "maintext": "The main text of the article",
                "wayback_time": "The time the article was archived"
            }
        }
    )

'''

    id : Mapped[int] = mapped_column(primary_key=True) # this is a newer way to define columns; traditional would be id = Column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(nullable=False)
    authors : Mapped[str] = mapped_column()
    url : Mapped[str] = mapped_column(nullable=False) 
    date_publish : Mapped[str] = mapped_column()
    description : Mapped[str] = mapped_column(Text)
    maintext : Mapped[str] = mapped_column(Text, nullable=False)
    wayback_time : Mapped[datetime] = mapped_column(default = datetime)
    date_created : Mapped[datetime] = mapped_column(default = datetime.utcnow) 

'''