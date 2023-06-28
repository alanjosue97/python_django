import json

from django.http import HttpResponse ,JsonResponse

from inventory.models import Inventory

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the inventory index ")

def contact(request):
    return HttpResponse("Hello, world. You're at the inventory Contact")


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Inventory.objects.create(
            name = data["name"],
            price = data["price"],
            category = data["category"],
            identifier = data["identifier"],
        ) 
        return HttpResponse("Created")

    else:
        return HttpResponse("Not Allowed")
    
def list(request):
    if request.method == "GET":
        response = [
            {"name": inventory.name,
             "price": inventory.price,
             "category": inventory.category,
             "identifier": inventory.identifier,
             } for inventory in Inventory.objects.all()]
        return JsonResponse({"data": response }, status=200)