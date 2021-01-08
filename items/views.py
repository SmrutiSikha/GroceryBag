from django.shortcuts import render
from .models import Grocery
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



# Create your views here.
def items(request):
    return render(request,'items/add.html')

@csrf_exempt
def add_items(request):
    name = request.POST['name']
    quantity = request.POST['quantity']
    status = request.POST['status']
    date = request.POST['date']
    obj = Grocery.objects.create(ItemName=name,ItemQuantity=quantity,ItemStatus=status,Date=date)
    obj.save()
    output = {'msg':'success'}
    return JsonResponse(output)

