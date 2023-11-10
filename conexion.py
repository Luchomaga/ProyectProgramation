import mysql.connector
from werkzeug.wrappers import Request, Response
import os
from wsgi_app import render_template, request, Blueprint
from werkzeug.utils import redirect


bp = Blueprint(base_prefix="/")
current_dir = os.path.dirname(os.path.abspath(__file__))
# Configura la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host='localhost',
    user='Magaa',
    password='dragonballz245gt',
    database='negocio2'
)

# Función para obtener los datos de la tabla gestionpersonal
def get_gestionpersonal():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM gestionpersonal')
    result = cursor.fetchall()
    cursor.close()
    return result

def get_caja():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM caja')
    result = cursor.fetchall()
    cursor.close()
    return result

def get_registroclientes():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM registroclientes')
    result = cursor.fetchall()
    cursor.close()
    return result 

# Función para renderizar una plantilla Jinja2

# Función para manejar la solicitud y generar una respuesta HTML a gestionpersonal
@bp.route("/gestion")
def gestionpersonal_app():
    
    if request.method == 'GET':
        data = get_gestionpersonal()
        response = Response( **render_template('ABMPers.html', data=data))
    
    return response

@bp.route("/Caja")
def caja_app():
   
    if request.method == 'GET':
        data = get_caja()
        response = Response(**render_template('Caja.html', data=data))
    
    return response

@bp.route("/registro")
def registroclientes_app():
    if request.method == 'GET':
        data = get_registroclientes()
        response = Response(**render_template('registrocliente.html', data=data))

    return response

@bp.route("/eliminar_registro")
def eliminar_registro():
    print("Eliminando...")
    if request.method == 'POST':
        registro_id = request.form.get('registro_id')
        cursor = db.cursor()
        cursor.execute("DELETE FROM gestionpersonal WHERE id = %s", (registro_id,))
        db.commit()
    return redirect('/gestion')

@bp.route("/actualizar_registro")
def actualizar_registro():
    if request.method == 'POST':
        registro_id = request.form.get('registro_id')
        nuevo_nombre = request.form.get('nuevo_nombre')  
        nueva_fechanacimiento = request.form.get('nueva_fechanacimiento')
        nuevo_genero = request.form.get('nuevo_genero')
        nueva_direccion = request.form.get('nueva_direccion')
        nuevo_telefono = request.form.get('nuevo_telefono')
        nuevo_correo = request.form.get('nuevo_correo')
        nueva_fechainicio = request.form.get('nueva_fechainicio')
        nuevo_Usuariopersonal = request.form.get('nuevo_Usuariopersonal')
        nuevo_Documento = request.form.get('nuevo_Documento')

        cursor = db.cursor()
        sql = "UPDATE gestionpersonal SET nombre=%s, fechanacimiento=%s, genero=%s, direccion=%s, telefono=%s, correo=%s, fechainicio=%s, Usuariopersonal=%s, Documento=%s WHERE id=%s"
        values = (nuevo_nombre, nueva_fechanacimiento, nuevo_genero, nueva_direccion, nuevo_telefono, nuevo_correo, nueva_fechainicio, nuevo_Usuariopersonal, nuevo_Documento, registro_id)
        cursor.execute(sql, values)
        db.commit()
    return redirect('/gestion')
