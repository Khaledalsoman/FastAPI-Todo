from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

db_url='sqlite///./todos.db'

engine=create_engine(db_url,connect_args={'check_same_thread':False})

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

base=DeclarativeBase()