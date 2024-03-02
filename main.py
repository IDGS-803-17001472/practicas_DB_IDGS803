from flask import Flask, render_template, request, Response, flash, g, redirect
from flask_wtf.csrf import CSRFProtect
import forms

from config import DevelopmentConfig

from models import db
from models import Empleados


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    #g.nombre = 'Daniel'
    print('before_request')

@app.after_request
def after_request(response):
    return response

@app.route("/index", methods = ["GET","POST"])
def index():
    emp_form = forms.EmpleadoForm(request.form)
    if request.method == "POST" and emp_form.validate() :
        empl=Empleados(nombre=emp_form.nombre.data,telefono=emp_form.telefono.data,email=emp_form.email.data,
                       direccion=emp_form.direccion.data,sueldo=emp_form.sueldo.data)
        db.session.add(empl)
        db.session.commit()
    return render_template("index.html",form=emp_form)

@app.route("/ABC_Empleados", methods = ["GET","POST"])
def ABC_Completo():
    emp_form=forms.UserForm2(request.form)
    empleados=Empleados.query.all()
    return render_template("ABC_Empleados.html", empleados=empleados)


@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    emp_form=forms.EmpleadoForm(request.form)
    if request.method=='GET':
        id=request.args.get("id")
        emp1=db.session.query(Empleados).filter(Empleados.id==id).first()
        emp_form.id.data = request.args.get("id")
        emp_form.nombre.data=emp1.nombre
        emp_form.telefono.data = emp1.telefono
        emp_form.direccion.data=emp1.direccion
        emp_form.sueldo.data=emp1.sueldo
    if request.method == 'POST':
        id=emp_form.id.data
        emp=Empleados.query.get(id)
        db.session.delete(emp)
        db.session.commit()
        return redirect('ABC_Empleados')
    return render_template("eliminar.html", form=emp_form)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    emp_form=forms.EmpleadoForm(request.form)
    if request.method=='GET':
        id=request.args.get("id")
        emp1=db.session.query(Empleados).filter(Empleados.id==id).first()
        emp_form.id.data = request.args.get("id")
        emp_form.nombre.data=emp1.nombre
        emp_form.telefono.data = emp1.telefono
        emp_form.direccion.data=emp1.direccion
        emp_form.sueldo.data=emp1.sueldo
    if request.method == 'POST':
        id=emp_form.id.data
        emp1=db.session.query(Empleados).filter(Empleados.id==id).first()
        emp1.nombre=emp_form.nombre.data
        emp1.telefono=emp_form.telefono.data
        emp1.direccion=emp_form.direccion.data
        emp1.sueldo=emp_form.sueldo.data
        db.session.add(emp1)
        db.session.commit()
        return redirect('ABC_Empleados')
    return render_template("modificar.html", form=emp_form)



@app.route("/alumnos", methods = ["GET","POST"])
def alum():
    print("dentro de alumnos")
    nom=''
    apa=''
    ama=''
    alum_form = forms.UserForm(request.form)
    if request.method == "POST" and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        mensaje="Bienvenido {}".format(nom)
        flash(mensaje)
        print("Nombre: {}".format(nom))
        print("ApellidoPa: {}".format(apa))
        print("ApellidoMa: {}".format(ama))
    
    return render_template("alumnos.html", form = alum_form, nombre = nom, apePa = apa, apeMa = ama)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()

