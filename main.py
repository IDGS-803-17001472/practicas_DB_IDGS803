from flask import Flask, render_template, request, Response, flash, g, redirect, session 
from flask_wtf.csrf import CSRFProtect
import forms
import datetime
from datetime import date
from sqlalchemy.sql import extract
from sqlalchemy import func, cast, Date


from config import DevelopmentConfig

from models import db
from models import Empleados, EncabezadoVenta, DetalleVenta


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
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


@app.route("/eliminar2", methods=["GET", "POST"])
def eliminar2():
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

pizza_form = forms.PizzaForm()
vent_form = forms.VentaPizzaForm()
getVnts_form = forms.ConsultaVentasForm()




@app.route("/getVentas", methods=["POST"])
def filtrar():
    formVentas = forms.ConsultaVentasForm(request.form)
    if request.method == "POST":
        dia_sem = formVentas.dia.data
        mes = int(formVentas.mes.data)
        filtro = int(formVentas.filtro.data)
        ventasArray = []
        totalVentas = 0
        if filtro == 0:
            ventas=EncabezadoVenta.query.filter(cast(EncabezadoVenta.fecha_compra, Date) == date.today()).all()
            for venta in ventas:
                totalVentas+=venta.total
                ventasArray.append(
                    {
                        "nombre": venta.nombre,
                        "direccion": venta.direccion,
                        "telefono": venta.telefono,
                        "total": venta.total,
                        "fecha_compra": venta.fecha_compra,
                    }
                )
        if filtro == 1:
            ventas = EncabezadoVenta.query.filter(func.dayofweek( EncabezadoVenta.fecha_compra)  == dia_sem).all()
            for venta in ventas:
                totalVentas+=venta.total
                ventasArray.append(
                    {
                        "nombre": venta.nombre,
                        "direccion": venta.direccion,
                        "telefono": venta.telefono,
                        "total": venta.total,
                        "fecha_compra": venta.fecha_compra,
                    }
                )
        if filtro == 2:
            ventas = EncabezadoVenta.query.filter(func.extract('month', EncabezadoVenta.fecha_compra) == mes).all()
            for venta in ventas:
                ventasArray.append(
                    {
                        "nombre": venta.nombre,
                        "direccion": venta.direccion,
                        "telefono": venta.telefono,
                        "total": venta.total,
                        "fecha_compra": venta.fecha_compra,
                    }
                )
            session["ventas"] = ventasArray
        if filtro == 3:
            ventas = EncabezadoVenta.query.filter(func.extract('month', EncabezadoVenta.fecha_compra) == mes).all()
            for venta in ventas:
                ventasArray.append(
                    {
                        "nombre": venta.nombre,
                        "direccion": venta.direccion,
                        "telefono": venta.telefono,
                        "total": venta.total,
                        "fecha_compra": venta.fecha_compra,
                    }
                )
            session["ventas"] = ventasArray
    return render_template("pizzeria.html",formv=vent_form,formp=pizza_form, formGetVen=getVnts_form, pizzas=session['lista'], ventas=session['ventas'])


@app.route("/pizzeria", methods = ["GET","POST"])
def pizzeria():
    vent_form = forms.VentaPizzaForm(request.form) 
    session['ventas'] = []
    ventas=EncabezadoVenta.query.filter(cast(EncabezadoVenta.fecha_compra, Date) == date.today()).all()
    totalVentas = 0
    for venta in ventas:
        totalVentas+=venta.total
        session['ventas'].append(
            {
            "nombre": venta.nombre,
            "direccion": venta.direccion,
            "telefono": venta.telefono,
            "total": venta.total,
            "fecha_compra": venta.fecha_compra,
            }
        )
    session.modified = True
    if 'lista' not in session:
        session['lista'] = []
        session.modified = True
    if request.method == "POST" and vent_form.validate() :
        if len(session.get('lista')) == 0:
            return render_template("pizzeria.html",formv=vent_form,formp=pizza_form, pizzas=session['lista'])
        detalleVenta = []
        for detalle in session['lista']: 
            detalleVenta.append(DetalleVenta(pina=detalle[0], jamon=detalle[1], 
                                             champinones=detalle[2], cantidad=detalle[3],
                                             tamanio=detalle[4],subtotal=detalle[5]))
            total = 0
        for detalle in detalleVenta:
            total += detalle.subtotal
        venta = EncabezadoVenta(nombre = vent_form.nombre.data,
        direccion = vent_form.direccion.data,
        telefono = vent_form.telefono.data, detalleVenta=detalleVenta,fecha_compra=request.form.get("fecha"), total=total)
        db.session.add(venta)
        db.session.commit()
        session['lista'] = []
        vent_form = forms.VentaPizzaForm()
    return render_template("pizzeria.html",formv=vent_form,formp=pizza_form, formGetVen=getVnts_form, pizzas=session['lista'], ventas=session['ventas'], totalV=totalVentas)

    


@app.route("/listaPizzas", methods = ["POST"])
def listaPizzas():
    pizza_form = forms.PizzaForm(request.form)
    if request.method == "POST" and pizza_form.validate() :
        subtotal = 0
        if pizza_form.tamanio.data == "chica":
            subtotal += 40
        elif pizza_form.tamanio.data == "mediana":
            subtotal += 80
        elif pizza_form.tamanio.data == "grande":
            subtotal += 120
        if pizza_form.pina.data == True:
            subtotal +=10
        if pizza_form.champinones.data == True:
            subtotal +=10
        if pizza_form.jamon.data == True:
            subtotal +=10
        subtotal= subtotal*int(pizza_form.cantidad.data)
        session['lista'].append([pizza_form.pina.data, pizza_form.jamon.data, 
                                             pizza_form.champinones.data, pizza_form.cantidad.data,
                                             pizza_form.tamanio.data, subtotal])
        session.modified = True
        pizza_form = forms.PizzaForm()
    return render_template("pizzeria.html",formv=vent_form,  formGetVen=getVnts_form,    formp=pizza_form, pizzas=session['lista'], 
                           ventas=session.get('ventas'))

@app.route("/quitarPizza", methods=["GET", "POST"])
def eliminar():
    idquitar=request.form['selectedPizza']
    if request.method == 'POST':
        session["lista"].pop((int(idquitar)-1))
        session.modified = True
    return render_template("pizzeria.html",formv=vent_form,  formGetVen=getVnts_form,    formp=pizza_form, pizzas=session['lista'], 
                           ventas=session.get('ventas'))



if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)


