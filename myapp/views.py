from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
import json
from django.contrib.sessions.models import Session

from django.shortcuts import render, redirect
from django.http import HttpResponse

def registration(request):
    if request.method == 'POST':
        # Handle the registration form submission here
        # You can access form data using request.POST.get() or Django forms

        # Assuming registration is successful, redirect to the login page
        return redirect('login')
    else:
        return render(request, 'myapp/registration.html')

def login(request):
    if request.method == 'POST':
        # Handle the login form submission here
        # You can access form data using request.POST.get() or Django forms

        # Assuming login is successful, redirect to the landing page
        return redirect('landing_page')
    else:
        return render(request, 'myapp/login.html')
# myapp/views.py
from django.shortcuts import render

def frontpage(request):
    return render(request, 'myapp/frontpage.html')

def landing_page(request):
    return render(request, 'myapp/landing_page.html')

def grammarly_page(request):
    return render(request, 'myapp/grammarly.html')

def contact_page(request):
    return render(request, 'myapp/contact.html')

def pricing_page(request):
    return render(request, 'myapp/pricing.html')




from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def run_selenium(request):
    try:
        # Replace 'python3' with your Python executable and provide the full path to your script.
        result = subprocess.run(['python3', '/home/peterse/Desktop/code1/myapp/turnitin_automation.py'], capture_output=True, text=True)

        if result.returncode == 0:
            return HttpResponse(f'Selenium Script Executed Successfully:\n{result.stdout}')
        else:
            return HttpResponse(f'Selenium Script Execution Failed:\n{result.stderr}')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}')

def run_cliffnote(request):
    try:
        # Replace 'python3' with your Python executable and provide the full path to your script.
        result = subprocess.run(['python3', '/home/peterse/Desktop/code1/myapp/cliffnote.py'], capture_output=True, text=True)

        if result.returncode == 0:
            return HttpResponse(f'Selenium Script Executed Successfully:\n{result.stdout}')
        else:
            return HttpResponse(f'Selenium Script Execution Failed:\n{result.stderr}')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}')

def run_quillbot(request):
    try:
        # Replace 'python3' with your Python executable and provide the full path to your script.
        result = subprocess.run(['python3', '/home/peterse/Desktop/code1/myapp/quillibot.py'], capture_output=True, text=True)

        if result.returncode == 0:
            return HttpResponse(f'Selenium Script Executed Successfully:\n{result.stdout}')
        else:
            return HttpResponse(f'Selenium Script Execution Failed:\n{result.stderr}')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}')

def run_studypool(request):
    try:
        # Replace 'python3' with your Python executable and provide the full path to your script.
        result = subprocess.run(['python3', '/home/peterse/Desktop/code1/myapp/studypool.py'], capture_output=True, text=True)

        if result.returncode == 0:
            return HttpResponse(f'Selenium Script Executed Successfully:\n{result.stdout}')
        else:
            return HttpResponse(f'Selenium Script Execution Failed:\n{result.stderr}')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}')


