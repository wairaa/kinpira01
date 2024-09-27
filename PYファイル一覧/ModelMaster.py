#ModelMaster.py
from sqlalchemy import Column, Integer, String, DATETIME
from from sqlalchemy import or_
from sqlalchemy.sql import text

from datetime import datetime
from commonDB import Base
class ModelMaster(Base):
    __tablename__ = 'model_master'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    maker = Column(String(1024), default='')
    model = Column(String(1024), default='')
    
    def__repr__(self):
        return "<model_master(" \
                " id='%s', " \
                " maker='%s', " \
                " model='%s' " \
                ")>" % ( \
                       self.id, self.maker, self.model)
def findModeName(session, maker, model):
    query = session.query(ModeMaster).from_statement(
        text("SELECT id, maker, model, length(model) as model_len FROM model_master WHERE INSTR(:x, model)=1 AND maker=:y order by model_len DESC")
        ).params(x=model, y=maker)
    result = query.first()
    if resut == None:
        return {'model' : model, 'isHit' : False}
    else:
        return {'model' : result.model, 'isHit' : True}
def initModelMaster(session):
    session.add_all([
        ModelMaster(maker='KAWAI', model='350'),
        ModelMaster(maker='KAWAI', model='500')])
    session.commit()  
