from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from datetime import date

# class UserForm():
def regForm(request):
	title = "Registration Form"
	unique_phone = "Mobile phone number already exist"
	unique_email = "Email already exist"
	valid_phone = "Mobile number is not valid"
	# print("Success")
	message = []
	if request.method == "POST" and request.is_ajax():
		mobile_number = request.POST.get("mobile_number")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		month_birth = request.POST.get("month_birth")
		date_birth = request.POST.get("date_birth")
		year_birth = request.POST.get("year_birth")
		gender = request.POST.get("gender")
		email = request.POST.get("email")
		today = date.today()
		user_filter = User.objects.filter(
			mobile_number=mobile_number,
			email=email
		).exists()
		if user_filter > 0:
			message = {
				"message_status":1,
				"message_header": "Warning!",
				"message_body": "Your data already registered. Please try again"
			}
			print(message['message_header'], message['message_body'])
			return JsonResponse(message, status=200)
		else:
			user_input = User(
				mobile_number=mobile_number,
				first_name=first_name,
				last_name=last_name,
				month_birth=month_birth,
				date_birth=date_birth,
				year_birth=year_birth,
				gender=gender,
				email=email,
				date_registered=today
			).save()
			message = {
				"message_status": 0,
				"message_header": "Success!",
				"message_body": "Your data has been successfully submitted"
			}
			print(message['message_header'], message['message_body'])
			return JsonResponse(message, status=200)
	return render(request,"user/registration_form.html",{
		"title":title,
		# "message_status":message['message_status'],
		# "message_header": message['message_header'],
		# "message_body": message['message_body']
	})

def userLogin(request):
	title = "Login Page"
	return render(request, "user/login.html", {
		"title":title
	})