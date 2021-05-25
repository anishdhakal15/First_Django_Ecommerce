from django.shortcuts import render,HttpResponse
from .models import Blogpost
def home(request):
    a = Blogpost.objects.all()
    res=[]
    for i in range(0,len(a),2):
        try:
            res.append([a[i],a[i+1]])
        except:
            res.append([a[i]])
    results={
        "posts":res,
        "range":range(len(res)),
        "total":len(res)
    }
    return render(request,'blog/index.html',results)

def blogpost(request,id):
    posts = Blogpost.objects.filter(post_id=id)[0]

    return render(request,'blog/blogpost.html',{'post':posts})