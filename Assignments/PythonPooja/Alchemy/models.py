from sqlalchemy import create_engine, Column,Integer,String,or_,not_,and_,desc,asc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine('sqlite:///final.db',echo=True) 
# create_engine('postgresql://postgress:123456@localhost:5432/python_test') 
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

class User(Base):
    __tablename__= 'users'
    id= Column(Integer, primary_key=True)
    name=Column(String)
    fullname=Column(String)
    lastname=Column(String)
    def __repr__(self):
        return "<User(name='%s',fullname='%s',nickname='%s')>"%(self.name,self.fullname,self.lastname)

if __name__=="__main__":
    Base.metadata.create_all(engine)

# user_a= User(name="jkg",fullname="ffh",lastname="kujb")    
# session.add(user_a)
# session.commit()
# session.close()
# print(session.query(User).all())

# print(session.query(User).filter(or_(User.name.ilike('P%'),User.lastname.ilike('m%'))).all())
# print(session.query(User).filter(and_(User.name.ilike('P%'),User.lastname.ilike('m%'))).all())

# print(session.query(User).filter(not_(User.name.ilike('b%'))).all())

# print(session.query(User).filter(User.name.ilike('P%')).order_by(desc(User.id)).all())


