
import json
from django.http import HttpResponse, JsonResponse
from users.models import User
import hashlib
import secrets

# Create your views here.
def information(request):
    return HttpResponse("Hello, You're at the information of users")

def create(request):
    if request.method == "POST":
        data=json.loads(request.body)
        User.objects.create(
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

def login(request):
    if request.method == "POST":
        data=json.loads(request.body)

        try:
            user= User.objects.get(
            email=data["email"],
            password=hashlib.sha512(data["password"].encode()).hexdigest(),
           )
            
            return JsonResponse(
                {
                    "message": "Login Success",
                    "token": user.token
                } , status = 200
            )    

        except User.DoesNotExist:
                return JsonResponse(
                {
                    "message": "Email or password is incorrect",
                } , status = 401,
        )  

        except Exception:
            return JsonResponse(
                {
                    "message": "Internal Server Error",
                },  status=500,
            )
      
        
    
    else:
        return JsonResponse(
            {"message": "Method not allowed"},
            status=405
        )


