from database.database import get_connection


def save_project(project):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO projects
        (
        name,
        city,
        land_area,
        floors,
        material_quality
        )
        VALUES (?,?,?,?,?)
        """,
        (
            project.name,
            project.city,
            project.land_area,
            project.floors,
            project.material_quality
        )
    )


    conn.commit()
    conn.close()