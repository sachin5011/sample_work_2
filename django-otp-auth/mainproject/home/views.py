from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Profile
import random
import http.client
from django.conf import settings
import pyotp
from datetime import datetime, timedelta



def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        
        user = User(first_name=name, email=email)
        user.save()

        otp_gen = str(random.randint(1000, 9999))
        print(otp_gen)
        profile = Profile(user=user, mobile=phone, otp=otp_gen)
        profile.save()
        otp = send_otp()
        request.session['phone'] = phone
        return redirect('otp')
    return render(request, "register.html")



def send_otp(request):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=120)
    otp = totp.now()
    request.session["otp_secret_key"] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=2)
    request.session["otp_valid_date"] = str(valid_date)
    return otp
    


def login(request):
    mobile = request.POST["phone"]
    user = authenticate(request, mobile)
    if user is not None:
        send_otp(request)
        request.session["phone"]
    return render(request, "login.html")

def otp(request):
    if request.method == "POST":
        mobile = request.session["phone"]
        otp_secret_key = request.session["otp_secret_key"]
        otp_valid_date = request.session["otp_valid_date"]

        if otp_secret_key and otp_valid_date is not None:
            valid_date = datetime.fromisoformat(otp_valid_date)

            if valid_date > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=120)

                if totp.verify(otp):
                    mobile = Profile.get
                    login(request, mobile)
    
    return render(request, "otp.html")
