from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ACLHEMY_DB = 'mysql+pymysql://dzhonpetrus:root@localhost/fastapi'

engine = create_engine(SQL_ACLHEMY_DB)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()