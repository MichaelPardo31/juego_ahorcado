import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.db import Dificultad, Categoria, Palabra

def seed_db():
    # Configurar la conexión a PostgreSQL
    url_conexion = "postgresql://postgres:root@localhost:5432/ahorcado"
    
    # Crear el motor de conexión
    engine = create_engine(url_conexion, echo=True)
    
    # Crear la sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Crear dificultades
    dificultades = [
        Dificultad(nombre="Fácil"),
        Dificultad(nombre="Media"),
        Dificultad(nombre="Difícil")
    ]
    session.add_all(dificultades)
    
    # Crear categorías
    categorias = [
        Categoria(nombre="Frutas"),
        Categoria(nombre="Animales"),
        Categoria(nombre="Países")
    ]
    session.add_all(categorias)
    
    # Commit para obtener los IDs
    session.commit()
    
    # Crear palabras
    palabras = [
        # Frutas
        Palabra(contenido="MANZANA", categoria_id=1, dificultad_id=1),
        Palabra(contenido="PLATANO", categoria_id=1, dificultad_id=1),
        Palabra(contenido="FRESA", categoria_id=1, dificultad_id=1),
        Palabra(contenido="PAPAYA", categoria_id=1, dificultad_id=2),
        Palabra(contenido="MANDARINA", categoria_id=1, dificultad_id=2),
        Palabra(contenido="GRANADILLA", categoria_id=1, dificultad_id=3),
        
        # Animales
        Palabra(contenido="PERRO", categoria_id=2, dificultad_id=1),
        Palabra(contenido="GATO", categoria_id=2, dificultad_id=1),
        Palabra(contenido="RATON", categoria_id=2, dificultad_id=1),
        Palabra(contenido="ELEFANTE", categoria_id=2, dificultad_id=2),
        Palabra(contenido="JIRAFA", categoria_id=2, dificultad_id=2),
        Palabra(contenido="HIPOPOTAMO", categoria_id=2, dificultad_id=3),
        
        # Países
        Palabra(contenido="PERU", categoria_id=3, dificultad_id=1),
        Palabra(contenido="CHILE", categoria_id=3, dificultad_id=1),
        Palabra(contenido="BRASIL", categoria_id=3, dificultad_id=2),
        Palabra(contenido="COLOMBIA", categoria_id=3, dificultad_id=2),
        Palabra(contenido="VENEZUELA", categoria_id=3, dificultad_id=3),
        Palabra(contenido="ARGENTINA", categoria_id=3, dificultad_id=3)
    ]
    session.add_all(palabras)
    
    # Commit final
    session.commit()
    session.close()

if __name__ == "__main__":
    seed_db() 