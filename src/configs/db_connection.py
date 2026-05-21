from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:
  def __init__(self):
    self.__connection_str = 'postgresql+psycopg2://postgres:password@localhost:5432/library'
    self.__engine = create_engine(self.__connection_str)
    self.session = None

  def __enter__(self):
    session_maker = sessionmaker(bind=self.__engine)
    self.session = session_maker()
    return self
  
  def __exit__(self, exc_type, exc, tb):
    self.session.close()
