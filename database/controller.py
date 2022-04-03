
import sqlite3

def crearBD():
    conexion = sqlite3.connect('facultad.db')
    conexion = commit()
    conexion = close()

def crearTablaEstudiante():
    conexion = sqlite3.connect('facultad')

    consulta = conexion.cursor(
    '''CREATE TABLE IF NOT EXISTS estudiante(
    id VARCHAR(20) PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    estado_civil VARCHAR(50) NOT NULL,
    curso_matriculado VARCHAR(50) NOT NULL)'''
    )

    if consulta.execute(estudiante):
        print('Consulta 1 realizada con exito')
    else:
        print('Ha ocurrido un error al crear la tabla estudiante')

    conexion = commit()
    conexion = close()

def crearTablaEmpleado():
    conexion = sqlite3.connect('facultad')

    consulta = conexion.cursor(
    '''CREATE TABLE IF NOT EXISTS empleado(
    id VARCHAR(20) PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    estado_civil VARCHAR(50) NOT NULL,
    años_en_la_facultad INTEGER NOT NULL,
    numero_despacho INTEGER NOT NULL)'''
    )

    if consulta.execute(estudiante):
        print('Consulta 1 realizada con exito')
    else:
        print('Ha ocurrido un error al crear la tabla empleado')

    conexion = commit()
    conexion = close()

def crearTablaProfesor():
    conexion = sqlite3.connect('facultad')

    consulta = conexion.cursor(
    '''CREATE TABLE IF NOT EXISTS profesor(
    id VARCHAR(20) PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    estado_civil VARCHAR(50) NOT NULL,
    departamento VARCHAR(50) NOT NULL)'''
    )

    if consulta.execute(estudiante):
        print('Consulta 1 realizada con exito')
    else:
        print('Ha ocurrido un error al crear la tabla empleado')

    conexion = commit()
    conexion = close()

def insertarDatosEstudiante(ide, nombre, apellido, estdo_civil, curso_matriculado):
    conexion = sqlite3.connect('facultad')
    cursor = conexion.cursor()
    cursor.execute(
        f'''
        INSERT INTO estudiante VALUES ('{ide}', '{nombre}', '{apellido}', 
        '{estdo_civil}', '{curso_matriculado}')
        '''
    )
    conexion.commit()
    conexion.close()

def insertarDatosEmpleado(ide, nombre, apellido, estdo_civil, años_en_la_facultad, numero_despacho):
    conexion = sqlite3.connect('facultad')
    cursor = conexion.cursor()
    cursor.execute(
        f'''
        INSERT INTO empleado VALUES ('{ide}', '{nombre}', '{apellido}', 
        '{estdo_civil}', '{curso_matriculado}', {años_en_la_facultad},
        {numero_despacho})
        '''
    )
    conexion.commit()
    conexion.close()    

def insertarDatosProfesor(ide, nombre, apellido, estdo_civil, departamento):
    conexion = sqlite3.connect('facultad')
    cursor = conexion.cursor()
    cursor.execute(
        f'''
        INSERT INTO profesor VALUES ('{ide}', '{nombre}', '{apellido}', 
        '{estdo_civil}', '{curso_matriculado}', {departamento})
        '''
    )
    conexion.commit()
    conexion.close()    