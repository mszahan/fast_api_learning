from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#for sqlite3
# DATABASE_URL = 'sqlite:///./todoapp.db'
# engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

#for postgresql
DATABASE_URL = 'postgresql://postgres:1294@localhost/tododb'
engine = create_engine(DATABASE_URL)

#for postgresql
# DATABASE_URL = 'mysql+pymysql://root:password@localhost:3306/database_name'
# engine = create_engine(DATABASE_URL)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()