from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración básica
Base = declarative_base()
engine = create_engine("sqlite:///personas.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# Modelo
class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)


# Crear tabla
Base.metadata.create_all(engine)


def interpretar_texto(texto):
    palabras = texto.lower().split()

    if palabras[0] == "agrega" and palabras[1] == "persona":
        nombre = palabras[2]
        edad = int(palabras[3])

        nueva = Persona(nombre=nombre, edad=edad)
        session.add(nueva)
        session.commit()

        return f"Persona '{nombre}' agregada con edad {edad}"

    elif texto == "muestra todas las personas":
        personas = session.query(Persona).all()

        if personas:
            return "\n".join(
                [f"{p.id}. {p.nombre} - {p.edad} años" for p in personas]
            )

        return "No hay personas registradas."

    return "Instrucción no reconocida."


if __name__ == "__main__":
    print("=== Sistema Text-to-SQL Básico ===")

    while True:
        comando = input("Escribe tu instrucción: ")

        if comando.lower() == "salir":
            break

        print(interpretar_texto(comando))
        print("ruisui")
