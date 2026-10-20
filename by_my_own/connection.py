from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

url = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    port=5432,
    database="backend_db",
)
engine = create_engine(url)

localsession = sessionmaker(bind= engine)
