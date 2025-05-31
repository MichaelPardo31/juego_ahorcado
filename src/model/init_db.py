from sqlalchemy import create_engine
from src.model.db import Base

def init_db():
    # Configurar la conexión a PostgreSQL
    url_conexion = "postgresql://postgres:root@localhost:5432/ahorcado"
    
    # Crear el motor de conexión
    engine = create_engine(url_conexion, echo=True)
    
    # Crear todas las tablas
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db() 