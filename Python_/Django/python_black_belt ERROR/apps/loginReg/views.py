from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	return render(request, 'loginReg/index.html')

def validate(request):

	data = {
		"first_name" : request.POST['first_name'],
		"last_name" : request.POST['last_name'],
		"email" : request.POST['email'],
		"password" : request.POST['password'],
		"passconfirm" : request.POST['passconfirm']
	}

	result = User.objects.validate(data)

	if result[0]:
		request.session['user_id'] = result[1].id 
		context = {
		'success': "You have Succesfully Registered! Thank you!"
		}
		return render(request, 'loginReg/index.html', context)
	else:
		for err in result[1]:
			messages.error(request, err)
		return redirect('/')

def success(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.filter(email=email)
		if not EMAIL_REGEX.match(email):
			context = {
			'email': "Email Not Valid"
			}
			return render(request, 'loginReg/index.html', context)
		if bcrypt.hashpw(str(password), str(user[0].password)) == user[0].password:
			pass
		else:
			context = {
			'pass': "Password Not Valid"
			}
			return render(request, 'loginReg/index.html', context)
		return render(request, 'pythonBlackBelt/index.html')
