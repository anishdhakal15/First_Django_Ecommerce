from django.shortcuts import render,HttpResponse,redirect,reverse
from math import ceil
from .models import Product,Contact,Orders,OrderUpdate
import json


def home(request):
    products = Product.objects.all()
    
    # params  = { 'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products }
    allProds = []
    vals = Product.objects.values('category')
    cats = {items['category'] for items in vals}
    for cat in cats:
        prd = Product.objects.filter(category=cat)
        n = len(prd)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        print(nSlides)
        allProds.append([prd,range(1,nSlides),nSlides])

    params = {
        'allprods':allProds
    }
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return render(request, 'shop/contact.html',{'success':True})
    return render(request, 'shop/contact.html')
def tracker(request):
    if request.method=="POST":
        email = request.POST.get('email', '')
        orderid = request.POST.get('orderId','')
        print(orderid,email)
        try:
            order = Orders.objects.filter(order_id=orderid,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates =[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    responce = json.dumps([updates,order[0].items], default=str)
                return HttpResponse(responce)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'shop/tracker.html')
def searchmatch(item,query):
    if query.lower() in item.product_name.lower() or query.lower() in item.desc.lower() or query.lower() in item.category:
        return True
    else:
        return False
def search(request):
    products = Product.objects.all()
    query = request.GET.get('search','')
    # params  = { 'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products }
    allProds = []
    vals = Product.objects.values('category')
    cats = {items['category'] for items in vals}
    for cat in cats:
        prdtmp = Product.objects.filter(category=cat)
        prd = [item for item in prdtmp if searchmatch(item,query)]
        n = len(cats)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prd)!=0 and len(query)>3:
            allProds.append([prd,range(1,nSlides),nSlides])
    params = {
        'allprods':allProds
    }
    if (len(allProds)==0):
        params['emsearch']=query
        params['em']=True
        if len(query)<4:
            params['queryerr']=True
        return render(request,'shop/index.html',params)
    return render(request,'shop/index.html',params)
def productview(request,myid):
    prod = Product.objects.filter(id=myid)
    params={
        'product':prod[0]
    }
    return render(request,'shop/prodview.html',params)
def checkout(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        amount = request.POST.get('amount',0)
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        itemJson = request.POST.get('itemJson', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('addr1', '')
        address2 = request.POST.get('addr2', '')
        
        order = Orders(name=name, email=email,amount=amount, phone=phone, city=city, state=state, zipcode=zip_code, items=itemJson, address1=address, address2=address2 )
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="order has been placed")
        update.save()
        return render(request,'shop/checkout.html',{'thank':'thank','id':order.order_id})
    return render(request,'shop/checkout.html')
