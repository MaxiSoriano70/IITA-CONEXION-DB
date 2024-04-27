import psycopg2

conn = psycopg2.connect(
    user="postgres", password="1234", port="5432", host="localhost", database="DB_CarnetVet"
)

cursor = conn.cursor()

cursor.execute("Select * from usuarios")

print(cursor.fetchall())

"""cursor.execute("INSERT INTO usuarios (nombreApellido, email, telefono, fechaNacimiento, contrasenia) VALUES ('Karen Dominguez', 'usuario1@example.com', '387456789', '1990-01-01', '12345678'), ('Karol Neiza', 'usuario2@example.com', '387123456', '1990-02-02', '12345678'), ('Marjorie Alonso', 'usuario3@example.com', '387123789', '1990-03-03', '12345678'), ('Celeste Severich', 'usuario4@example.com', '387478963', '1990-04-04', '12345678'), ('Nadia Sosa', 'usuario5@example.com', '398123698', '1990-05-05', 'contraseña5')")"""

"""cursor.execute("INSERT INTO usuarios (nombreApellido, email, telefono, fechaNacimiento, contrasenia) VALUES('Maxi', 'maxi@example.com', '3874514852', '1998-01-01', '12345678')")"""

conn.commit()

cursor.execute("Select * from usuarios")

print(cursor.fetchall())

cursor.execute("UPDATE usuarios SET nombreApellido = 'Maxi Soriano' WHERE idUsuario = 7")

conn.commit()

cursor.execute("Select * from usuarios")

print(cursor.fetchall())