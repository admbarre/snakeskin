from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

test_db = 'sqlite:///test.db'
in_mem = 'sqlite:///:memory:'

#TODO unsure about where to put these variables
Base = declarative_base()

class ExpiringImage(Base):
    __tablename__ = 'expiring_images'
    image_id = Column(Integer, primary_key=True)
    path = Column(String)
    expiration = Column(String)

    def __repr__(self):
        return f'ExpiringImage(id={self.image_id}, path={self.path}, expiration={self.expiration}'

engine = create_engine(test_db,echo=True)
Base.metadata.create_all(engine)
