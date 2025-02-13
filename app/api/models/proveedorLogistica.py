from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Llamar a la base de datos
Base = declarative_base()
# Definir las tablas del API

class Proveedor(Base):
    __tablename__='proveedores'
    id_proveedor = Column(Integer, primary_key=True)
    nombres = Column(String(50))
    documento = Column(String(15))
    direccion = Column(String(50))
    ciudad = Column(String(15))
    representante = Column(String(50))
    telefono_contacto = Column(String(15))
    correo = Column(String(50))
    fecha_envio = Column(Date)
    costo_envio = Column(Integer)
    descripcion = Column(String(100))

class Logistica(Base):
    __tablename__='logisticos'
    id_logistico = Column(Integer, primary_key=True)
    nombre_encargado = Column(String(50))
    correo_encargado = Column(String(50))
    telefono_encargado = Column(String(15))
    fecha_receptor = Column(Date)
    detalles = Column(String(100))