from db_alumnat import get_db_connection
from fastapi import HTTPException

# Funció per llistar tots els alumnes
def get_all_alumnes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alumne")
    alumnes = cursor.fetchall()
    conn.close()
    return alumnes

def get_alumne(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alumne WHERE IdAlumne = %s", (id,))
    alumne = cursor.fetchone()
    conn.close()
    if alumne is None:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne

def add_alumne(alumne):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aula WHERE IdAula = %s", (alumne.idAula,))
    aula = cursor.fetchone()
    if not aula:
        conn.close()
        raise HTTPException(status_code=400, detail="IdAula no existeix")

    cursor.execute("INSERT INTO alumne (NomAlumne, Cicle, Curs, IdAula) VALUES (%s, %s, %s, %s)", 
                   (alumne.nomAlumne, alumne.Cicle, alumne.Cuts, alumne.IdAula))
    conn.commit()
    conn.close()
    return {"message": "S'ha afegit correctament"}

def update_alumne(id: int, alumne):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alumne WHERE IdAlumne = %s", (id,))
    existent_alumne = cursor.fetchone()
    if not existent_alumne:
        conn.close()
        raise HTTPException(status_code=404, detail="Alumne no trobat")

    cursor.execute("SELECT * FROM aula WHERE IdAula = %s", (alumne.IdAula,))
    aula = cursor.fetchone()
    if not aula:
        conn.close()
        raise HTTPException(status_code=400, detail="IdAula no vàlid")

    cursor.execute("""
        UPDATE alumne SET NomAlumne = %s, Cicle = %s, Curs = %s, IdAula = %s WHERE IdAlumne = %s
    """, (alumne.NomAlumne, alumne.Cicle, alumne.Curs, alumne.IdAula, id))
    conn.commit()
    conn.close()
    return {"message": "S'ha modificat correctament"}

def delete_alumne(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alumne WHERE IdAlumne = %s", (id,))
    alumne = cursor.fetchone()
    if not alumne:
        conn.close()
        raise HTTPException(status_code=404, detail="Alumne no trobat")

    cursor.execute("DELETE FROM alumne WHERE AlumneId = %s", (id,))
    conn.commit()
    conn.close()
    return {"message": "S'ha esborrat correctament"}

def list_all_alumnes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT alumne.*, aula.DescAula, aula.edifici, aula.pis
        FROM alumne
        JOIN aula ON alumne.idAula = aula.id
    """)
    alumnes = cursor.fetchall()
    conn.close()
    return alumnes
