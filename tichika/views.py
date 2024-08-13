from openai import OpenAI
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from transformers import pipeline
import os

# Set your OpenAI API key here





def get_gemini_response(question):
    gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_KEY_HERE'  # Replace with your actual API key
    }

    payload = {
        'prompt': {
            'text': question
        }
    }

    try:
        response = requests.post(gemini_api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')

        # Logic to process the question and get the response from ChatGPT API
        answer = get_chatgpt_response(question)

        return JsonResponse({'answer': answer})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



# Other views remain unchanged
def signup_action(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Signup successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')

    return redirect('signup')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def index(request):
    return render(request, 'index.html')

def notse(request):
    return render(request, 'notse.html')

def pricing(request):
    return render(request, 'pricing.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def resetpassword(request):
    return render(request, 'reset_password.html')

def notse_index(request):
    return render(request, 'index.html')

def pricing_index(request):
    return render(request, 'index.html')

def notse_pricing(request):
    return render(request, 'pricing.html')

def notse_blog(request):
    return render(request, 'blog.html')

def blog_notse(request):
    return render(request, 'notse.html')

def pricing_contact(request):
    return render(request, 'contact.html')

def pricing_notse(request):
    return render(request, 'notse.html')

def notse_pricing(request):
    return render(request, 'pricing.html')
