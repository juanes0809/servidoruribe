from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Llamar a la base de datos
# Definir las tablas del API

class Proveedor():
    __tablename__='proveedores'
    nombres=Column(String(50))
    documento=Column(String(50))
    