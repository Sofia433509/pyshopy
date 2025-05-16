from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Paciente(Base):
    __tablename__ = "Pacientes"
    id = Column(Integer,
                primary_key=True)
    nombre=Column(String(60))
    apellido=Column(String(60))
    Tipo_de_documento=Column(String(60))
    numero_de_documento=Column(Integer)
    telefono = Column(Integer)

    #Relacion uno a muchos con producto
    Medicos = relationship("Medico",
                          back_populates="Paciente")

class Medico(Base):
    __tablename__ = "Medicos"
    id = Column(Integer , 
                primary_key=True)
    nombre = Column(String(60))
    apellido = Column(String(60))
    especialidad = Column(String(60))
    
    #clave foranea
    paciente_id=Column(Integer,
                       ForeignKey(Paciente.id))