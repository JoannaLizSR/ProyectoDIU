from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import  Cita
from .forms import CitaForm


import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "vistas/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="vistas/password_reset.html", context={"password_reset_form":password_reset_form})

def home(request):
    return render(request,"vistas/home.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'vistas/signup.html', {'form': form})


def information(request):
    return render(request,"vistas/info.html")

def inicioUsr(request):
    return render(request, "vistas/inicioUsr.html" )

def inicioAdmin(request):
    return render(request, "vistas/inicioAdmin.html" )

def deleteUser(request):

   usuario1 = User(email="likv07@gmail.com",nombre="Lizbeth")
   usuario1.save()

   usuario2 = User(email="liz@gmail.com",nombre="Lizbeth2")
   usuario2.save()

   consulta_Usuario = User.objects.all()
   print(consulta_Usuario)
   return render(request, "vistas/deleteUser.html", {'consulta_Usuario':consulta_Usuario})

def eliminarUsuario(request,email):
   usuario = User.objects.get(email=email)
   usuario.delete()

   return redirect('home')
    

def delete_cita(request,cita_id):
    
    cita = Cita.objects.get(pk=cita_id)
    try:
        cita.delete()
        print("Se logro.Se elimino")
    except Exception as e :
        print(e)    
        print("NO SE  elimino")
    finally:    
        return HttpResponseRedirect('/')

def delete_cita_menu(request,cita_id):
    
    cita =Cita.objects.get(pk=cita_id)
    cita_date = getattr(cita,'cita_fecha')
    dia = cita_date.strftime('%d')
    mes = cita_date.strftime('%m')
    anio = cita_date.strftime('%Y')
    return render(request, "vistas/delete_cita.html",{'dia':dia,'mes':mes,'anio':anio,'cita_id':cita_id})

def update_cita(request,cita_id):
    cita = Cita.objects.get(pk=cita_id)
    form = CitaForm(request.POST or request.FILES or None,instance=cita)
    if form.is_valid():
            form.save()
            print("Se logro la actualización")
            #messages.success("Success in the save")
            return  HttpResponseRedirect('/')
    return render(request,'vistas/update_cita.html',{'cita':cita,'form':form})

def add_cita(request):
    submitted = False
    requiered_l = ['Nombre','Apellido1', 'Apellido2', 'CURP' ,'Direccion', 'Ine','Cita fecha']
    if request.method == "POST":   
        form = CitaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Se logro")
            #messages.success("Success in the save")
            return  HttpResponseRedirect('/add_cita?submitted=True')
        else:
            #messages.error(request,"Error saving")
            print("No se logro")
            
    else:
        form = CitaForm()
        if submitted in request.GET:
            submitted = True    
           
    
    return render(request,'vistas/add_cita.html',{'form':form,'submitted':submitted,'requiered_l':requiered_l})
