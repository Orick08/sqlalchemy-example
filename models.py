from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:://zoo.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# animals
# ID / Name / Habitat
class Animal(Base):
    __tablename__ = "animals"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    habitat = Column(String)
    # Should have the same name as the other class
    # back populates should be like this class __tablename__
    logs = relationship("Logbook", back_populates="animal")

    def __repr__(self):
        return f"""
        \nAnimal {self.id}\r
        Name = {self.name}\r
        Habitat = {self.habitat}
        """


# Zookeeper Log
# Id / animal ID (FK) / Notes
class Logbook(Base):
    __tablename__ = "logbook"
    
    id = Column(Integer, primary_key=True)
    # Name of the other table, dot, and then the primary key
    animal_id = Column(Integer, ForeignKey("animals.id"))
    notes = Column(String)
    # Should have the other class name and then the attribute
    # of the other class
    animal = relationship("Animal", back_populates="logs")

    def __repr__(self):
        return f"""
        \nLogbook {self.id}\r
        Animal ID = {self.animal_id}\r
        Notes = {self.notes}
        """