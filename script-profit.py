from sqlalchemy import create_engine
from models import Base  # Importar el modelo Base que contiene las clases definidas
from sqlalchemy.orm import sessionmaker

# Configuración de la conexión a la base de datos
DEBUG = True
TESTING = False
SECRET_KEY = 'dev'
DB_USER = 'grace'
DB_PASSWORD = 'gr4c1a!'
DB_HOST = 'localhost'
DB_NAME = 'cccp'
DATABASE_URI = 'mysql+pymysql://DB_USER:DB_PASSWORD@DB_HOST/DB_NAME'
engine = create_engine(DATABASE_URI)

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)
print("Tablas creadas con éxito.")
