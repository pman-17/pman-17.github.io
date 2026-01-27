from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

class Pets(BaseModel):
    type: str
    age: int
    name: str
    color: str

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_database():
    connection = sqlite3.connect('my_pets.db')
    print('Created Database.')

    curor = connection.cursor()
    print('Cursor Connected')

    curor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            color TEXT,
            age INTEGER
        )
    ''')
    print("✅ Created a table to store pets!")

create_database()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/pets")
async def root(item: Pets):
    print(item)
    connection = sqlite3.connect('my_pets.db')
    print('Created Database.')

    curor = connection.cursor()
    curor.execute('INSERT INTO pets (name, type, color, age) VALUES (?, ?, ?, ?)',
                (item.name, item.type, item.color, item.age))
    connection.commit()
    return item

@app.get("/getpets")
async def getpets():
    connection = sqlite3.connect('my_pets.db')
    curor = connection.cursor()

    curor.execute('SELECT * FROM pets')
    all_pets = curor.fetchall()

    for pet in all_pets:
        pet_id, name, pet_type, color, age = pet
        print(f"{name} the {pet_type} {color} (Age: {age})")

    return all_pets

