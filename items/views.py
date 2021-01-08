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
    print("id",request.user)
    id = request.GET['sid']
    obj = Grocery.objects.get(id=id)
    obj.delete()
    output = {'id':id}
    return JsonResponse(output)

def update_items(request,pk):
    print("pk",pk)
    obj = Grocery.objects.get(id=pk)
    return render(request,"items/update.html",context={'items':obj})

@csrf_exempt
def updated_items(request):
    item = Grocery.objects.get(id=request.POST['itemid'])
    item.ItemName=request.POST['itemname']
    item.ItemQuantity=request.POST['itemquantity']
    item.ItemStatus=request.POST['itemstatus']
    item.Date=request.POST['date']
    item.save()
    obj = list(Grocery.objects.all())
    return render(request,'items/items.html',context={'items':obj})

def filter_items(request):
    dates = Grocery.objects.filter(Date=request.GET['date'])
    return JsonResponse({'items':list(dates.values())})
    

