from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from glapg.config import DATABASE_URL


engine = create_engine(DATABASE_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, 
                                         autoflush=False, 
                                         bind=engine))

class BaseModel(object):
    
    def __init__(self):
        super(BaseModel, self).__init__()

    @classmethod
    def get(self, id):
        return self.query.filter(self.id == id).first()

    @classmethod
    def gets(self, ids):
        return self.query.filter(self.id.in_(ids)).all()

    @classmethod
    def all(self):
        return self.query.all()

    def persist(self, commit=True):
        db_session.add(self)
        if commit:
            db_session.commit()

    def delete(self, commit=True):
        model_delete.send(self)
        db_session.delete(self)
        if commit:
            db_session.commit()
    


Model = declarative_base(name="Model", cls=BaseModel)
Model.query = db_session.query_property()

def create_db():
    import glapg.models
    Model.metadata.create_all(bind=engine)


