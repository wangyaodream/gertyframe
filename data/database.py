from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///data.sqlite3', echo=True)
Base = declarative_base()


class Messages(Base):
    __tablename__ = 'messages'

    name = Column(String, primary_key=True)
    content = Column(String)


# 创建所有表
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()







