
import json
from django.http import HttpResponse, JsonResponse
from users.models import Users
import hashlib
import secrets

# Create your views here.
def information(request):
    return HttpResponse("Hello, You're at the information of users")

def create(request):
    if request.method == "POST":
        data=json.loads(request.body)
        Users.objects.create(
            email=data["email"],
            password=hashlib.sha512(data["password"].encode()).hexdigest(),
            token=secrets.token_hex(16)
        )
        return JsonResponse(
            {"message": "User successfully created"},
            status=201
        )
    
    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status=405
        )
