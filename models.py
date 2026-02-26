from database import base
from sqlalchemy import column,Integer,Boolean,String

class Todos(base):
    __tablename__='todos'
    id=column(Integer,primary_key=True,index=True)
    tite=column(String)
    description=column(String)
    priorty=column(Integer)
    complete=column(Boolean,default=False)