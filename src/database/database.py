import sqlite3
from pathlib import Path


DB_PATH = Path("iran_smart_bim.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        city TEXT,

        land_area REAL,

        floors INTEGER,

        material_quality TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def get_projects():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 
        id,
        name,
        city,
        land_area,
        floors,
        material_quality,
        created_at

        FROM projects
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows



def delete_project(project_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM projects
        WHERE id=?
        """,
        (project_id,)
    )

    conn.commit()

    conn.close()    