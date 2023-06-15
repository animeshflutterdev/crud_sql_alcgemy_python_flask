from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,Integer,DateTime, create_engine
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = 'sqlite:///' + os.path.join(BASE_DIR,'orm.db')

Base = declarative_base()

engine = create_engine(connection_string,echo=True)

Session = sessionmaker()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key=True)
    userName = Column(String(20),nullable=False,unique=True)
    email = Column(String(80),unique=True,nullable=False)
    date_created =  Column(DateTime(),default=datetime.utcnow)

    def __repr__ (self):
        return f'id = {self.id}, username = {self.userName}, email = {self.email}, date_created = {self.date_created}'

new_user = User(id=1,userName = 'animesh', email= 'a@gmail.com')
print('new user = ', new_user)
