from django.http import JsonResponse
from django.shortcuts import render
import json

def index(request):
    return render(request, "main/index.html")

def get_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        reply = f"You typed: {user_message}"
        return JsonResponse({"reply": reply})
    return JsonResponse({"reply": "Invalid request"})
