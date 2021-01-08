from django.shortcuts import render
from .models import Grocery
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



# Create your views here.
def items(request):
    obj = list(Grocery.objects.all())
    return render(request,'items/items.html',context={'items':obj})

def add_page(request):
    return render(request,'items/add.html')

@csrf_exempt
def add_items(request):
    print('enetered')
    name = request.POST['name']
    quantity = request.POST['quantity']
    status = request.POST['status']
    date = request.POST['date']
    obj = Grocery.objects.create(ItemName=name,ItemQuantity=quantity,ItemStatus=status,Date=date)
    obj.save()
    output = {'msg':'success'}
    return JsonResponse(output)

@csrf_exempt
def delete_items(request):
    id = request.GET['sid']
    obj = Grocery.objects.get(id=id)
    obj.delete()
    total = Grocery.objects.all().values()
    output = {'items':list(total), 'id':id}
    return JsonResponse(output)
    

