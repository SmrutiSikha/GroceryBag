from django.shortcuts import render, redirect
from .models import Grocery
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
def items(request):
    if request.user.is_authenticated:
        obj = list(Grocery.objects.filter(UserId=User.objects.get(username=request.user).id))
        return render(request,'items/items.html',context={'items':obj})

    else:
        return redirect('/user/login')

def add_page(request):
    return render(request,'items/add.html')

@csrf_exempt
def add_items(request):
    if request.user.is_authenticated:
        uid = User.objects.get(username=request.user).id
        name = request.POST['name']
        quantity = request.POST['quantity']
        status = request.POST['status']
        date = request.POST['date']
        obj = Grocery.objects.create(ItemName=name,ItemQuantity=quantity,ItemStatus=status,Date=date, UserId=uid)
        obj.save()
        output = {'msg':'success'}
        return JsonResponse(output)
    else:
        return render(request, "registration/login.html")

@csrf_exempt
def delete_items(request):
    id = request.GET['sid']
    obj = Grocery.objects.get(id=id)
    obj.delete()
    output = {'id':id}
    return JsonResponse(output)

def update_items_page(request,pk):
    print("pk",pk)
    obj = Grocery.objects.get(id=pk)
    return render(request,"items/update.html",context={'items':obj})

@csrf_exempt
def updated_items(request):
    if request.method == "POST":
        print('bhitata')
        print(request.POST['itemid'])
        print(request.POST['itemname'])
        print(request.POST['itemquantity'])
        print(request.POST['itemstatus'])
        print(request.POST['date'])
        item = Grocery.objects.get(id=request.POST['itemid'])
        item.ItemName=request.POST['itemname']
        item.ItemQuantity=request.POST['itemquantity']
        item.ItemStatus=request.POST['itemstatus']
        item.Date=request.POST['date']
        item.save()
        return redirect('allItems')
    else:
        return redirect('allItems')

def filter_items(request):
    dates = Grocery.objects.filter(Date=request.GET['date'], UserId=User.objects.get(username=request.user).id)
    return JsonResponse({'items':list(dates.values())})
    

