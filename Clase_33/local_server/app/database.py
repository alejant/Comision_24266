import psycopg2

DATABASE_CONFIG = {
    'user': 'postgres',
    'password': 'Fortin94',
    'host': '192.168.0.20', 
    'database': 'flask_ejemplo',
    'port': '5432'
}


def testear_conexion():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()


def crear_tabla_tareas():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Tareas (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            descripcion VARCHAR(300) NOT NULL,
            completada BOOLEAN NOT NULL,
            activo BOOLEAN NOT NULL
        );
        """
    )


    conn.commit()
    cur.close()
    conn.close()