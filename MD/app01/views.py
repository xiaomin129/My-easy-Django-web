from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import datetime
from django.contrib import messages
import threading

# Create your views here.
def index(request):#个人信息页面
    info = request.session["info"]['ID']
    cheek=models.WorkerInfo.objects.filter(id=info).first()
    if request.method=="GET":
        return render(request,"index.html",{'cheek':cheek})
    name=request.POST.get("name")
    opsw=request.POST.get("opassword")
    npsw=request.POST.get("npassword")
    age=request.POST.get("age")
    sex=request.POST.get("sex")
    models.WorkerInfo.objects.filter(id=cheek.id).update(name=name,age=age,sex=sex)
    if opsw=='':
        messages.error(request,'信息修改成功')
        return redirect("/index/")
    else:
        if opsw==cheek.password:
            models.WorkerInfo.objects.filter(id=cheek.id).update(password=npsw)
            messages.error(request,'信息修改成功')
            return redirect("/index/")
        else:
            messages.error(request,'旧密码输入错误')
            return redirect("/index/")


def login(request):#登陆界面
    if request.method == "GET":
        return render(request,"login.html")
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    login = request.POST.get("login")
    if login == 'menber':
        cheek=models.WorkerInfo.objects.filter(name=name).first()
        if cheek and cheek.password==pwd:
            request.session["info"]={'ID':cheek.id,'name':'worker'}
            return redirect("/index/")
    else:
        cheek=models.ManageInfo.objects.filter(name=name).first()
        if cheek and cheek.password==pwd:
            request.session["info"]={'ID':cheek.id,'name':'root'}
            return redirect("/manage_index/")
    messages.error(request,'请输入正确内容')
    return redirect("/login/")


def drugs_in(request):#药品进货
    if request.method == "GET":
        return render(request,"drugs_in.html")
    name = request.POST.get("name")
    cheek = models.Drugs.objects.filter(name=name).first()
    price = request.POST.get("price")
    num = request.POST.get("num")
    unit = request.POST.get("unit")
    classification = request.POST.get("classification")
    time=datetime.datetime.now()
    worker_id=request.session["info"]["ID"]
    worker_name=models.WorkerInfo.objects.filter(id=worker_id).first()
    if cheek:
        models.Log.objects.create(time=time,worker_name=worker_name.name,drugs_name=name,InOrOut=1,num=num)
        num=int(num)+cheek.num
        models.Drugs.objects.filter(id=cheek.id).update(price=price,num=num,unit=unit,classification=classification)
        messages.error(request,'操作成功')
        return redirect("/index/drugs_in/")
    models.Drugs.objects.create(name=name,price=price,num=num,unit=unit,classification=classification)
    models.Log.objects.create(time=time,worker_name=worker_name.name,drugs_name=name,InOrOut=1,num=num)
    messages.error(request,'进货操作成功')
    return redirect("/index/drugs_in/")
    
def drugs_out(request):#药品销售
    if request.method == "GET":
        n1 = request.GET.get("name")
        n2 = request.GET.get("num")
        cheek = models.Drugs.objects.filter(name=n1).first()
        if cheek and n2:
            pricesum = float(cheek.price) * int(n2)
            return render(request,"drugs_out.html",{'pricesum':pricesum})
        return render(request,"drugs_out.html")
    name = request.POST.get("name")
    num = request.POST.get("num")
    cheek = models.Drugs.objects.filter(name=name).first()
    classification = cheek.classification
    godname = request.POST.get("godname")
    tel = request.POST.get("tel")
    worker_id=request.session["info"]["ID"]
    worker_name=models.WorkerInfo.objects.filter(id=worker_id).first()
    if cheek and cheek.num-int(num)>=0:
        time=datetime.datetime.now()
        if classification:
            if godname and tel:
                models.God.objects.create(name=godname,phone=tel,time=time,drugs=name)
            else:
                messages.error(request,'处方药请输入正确的顾客信息')
                return redirect("/index/drugs_out")
        num1=cheek.num-int(num)
        models.Drugs.objects.filter(id=cheek.id).update(num=num1)
        models.Log.objects.create(time=time,worker_name=worker_name.name,drugs_name=name,InOrOut=0,num=num)
        messages.error(request,'销售操作成功')
        return redirect("/index/drugs_out/")
    messages.error(request,'药品信息不存在或药品库存不足')
    return redirect("/index/drugs_out/")


def drugs_index(request):#药品库存信息
    queryset = models.Drugs.objects.all()
    if request.session["info"]["name"]=='root':
        return render(request,"manage_drugs_index.html",{'queryset':queryset})
    return render(request,"drugs_index.html",{'queryset':queryset})

def log(request):#操作日志
    ID=request.session["info"]['ID']
    Name=models.WorkerInfo.objects.filter(id=ID).first()
    queryset = models.Log.objects.filter(worker_name=Name.name)
    return render(request,"log.html",{'queryset':queryset})

def manage_index(request):#管理员信息
    return render(request,"manage_index.html")

def manage_log(request):#员工日志
    queryset = models.Log.objects.all()
    return render(request,"manage_log.html",{'queryset':queryset})

def exit(request):#注销
    request.session.clear()
    return redirect("login/")

def woker_info(request):#管理员工信息
    queryset = models.WorkerInfo.objects.all()
    return render(request,"worker_info.html",{'queryset':queryset})

def god(request):#购买记录
    queryset = models.God.objects.all()
    return render(request,"god.html",{'queryset':queryset})

def add_worker(request):#增加员工
    if request.method=="GET":
        return render(request,"add_worker.html")
    name = request.POST.get("name")
    psw1 = request.POST.get("password1")
    psw2 = request.POST.get("password2")
    age = request.POST.get("age")
    sex = request.POST.get("sex")
    if psw1 == psw2:
        models.WorkerInfo.objects.create(name=name,password=psw1,age=age,sex=sex) 
        return redirect("/manage_index/worker/")
    messages.error(request,'两次密码输入不一致')
    return redirect("/add_worker/")

def del_worker(request):#删除员工
    nid = request.GET.get('nid')
    models.WorkerInfo.objects.filter(id=nid).delete()
    return redirect("/manage_index/worker/")

def cookie(request):#cookie测试
    info=request.session["info"]['ID']
    print(request.GET.get("n1"))
    return render(request,"cookie.html")

