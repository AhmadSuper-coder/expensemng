from django.forms.widgets import FileInput
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from app.forms import EditProfileForm, LoginForm,SignupForm,ExpenseForm,PasswordChangeForm,TaskForm,EditProfileForm,MakeProfileForm,UserLoginForm,UserCreationForm,GroundNameForm
from app.models import Expense, TaskModel,ProfileModel,UserCreation,GroupName
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Min, Sum
# Create your views here.


def Signup(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=SignupForm(request.POST)
            print(fm)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Congratulation Account has been created succesfully !!")
                return HttpResponseRedirect('/signup/')

        else:
            fm=SignupForm()
    else:
        return HttpResponseRedirect('/')
    return  render(request,'app/signup.html',{'form':fm})


def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                login(request,user)
                username=request.user
                return HttpResponseRedirect('/dashboard/')
            
        else:
            fm=LoginForm()
        return  render(request,'app/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def Dashboard(request):
    
    if request.user.is_authenticated:
        exp=Expense.objects.all()
        if exp:
        # exp=Expense.objects.filter(user=1)
            exp=Expense.objects.all()
            user=request.user.username
            totals=exp.aggregate(Sum('price'))
            total=(totals['price__sum'])
            user=User.objects.count()
            avgs=total/user
            avg=round(avgs,1)
            us=User.objects.all()
            prices=[]
            for u in us:
                uex=Expense.objects.filter(user_id=u.id).aggregate(Sum('price'))
                usern=u.username
                uprice=uex['price__sum']
                if uprice==None:
                    usern=usern
                    uprice=0
                    overall=(avg-uprice)
                else:
                    overall=(avg-uprice)
                d={"username":usern,'price':uprice,"overall":overall}
                prices.append(d)
            context={'total':total,"avg":avg,"uex":uex,"prices":prices}
        else:
            total=0
            avg=0
            uex=0
            prices="0"
            context={'total':total,"avg":avg,"uex":uex,"prices":prices}
    else:
        return HttpResponseRedirect('/')
    return render(request,'app/dashboard.html',context)



def ViewTotal(request):
    if request.user.is_authenticated:
        user=request.user.username
        exp=Expense.objects.all()
    else:
        return HttpResponseRedirect('/')
    return render(request,'app/viewtotal.html',{'user':user,"exps":exp,})





def Profile(request):
    profiles=ProfileModel.objects.all()
    user=request.user
    return render(request,'app/profile.html',{'user':user,'profiles':profiles})


def Expenses(request):
    if request.user.is_authenticated:
        username=request.user.username
        if request.method == 'POST':
            fm=ExpenseForm(request.POST)
            if fm.is_valid():
                user=request.user
                item=fm.cleaned_data['itemname']
                qt=fm.cleaned_data['quantity']
                pr=fm.cleaned_data['price']
                dt=fm.cleaned_data['date']
                ex=Expense(user=user,itemname=item,quantity=qt,price=pr,date=dt)
                ex.save()
                fm=ExpenseForm()
                messages.success(request,"Successfully Added")
        else:       
            fm=ExpenseForm()
    else:
        return HttpResponseRedirect('/')
    items=Expense.objects.all()
    return render(request,'app/expense.html',{'form':fm,'username':username})


def ViewExpense(request):
    if request.user.is_authenticated:
        items=Expense.objects.all()
    else:
        return HttpResponseRedirect('/')
    return render(request,'app/viewexpense.html',{'items':items})




def Task(request):
    if request.method=='POST':
        fm=TaskForm(request.POST)
        if fm.is_valid():
            user=request.user
            nm=fm.cleaned_data['name']
            st=fm.cleaned_data['start']
            en=fm.cleaned_data['end']
            note=fm.cleaned_data['note']
            tk=TaskModel(user=user,name=nm,start=st,end=en,note=note)
            tk.save()
            fm=TaskForm()
            messages.success(request,"Successfully submited")
            return HttpResponseRedirect('/task/')
    else:
        fm=TaskForm()
    items=TaskModel.objects.all()
    user=request.user
    return render(request,'app/task.html',{"form":fm,'items':items,'user':user})


def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Password Changed successfully !! ")
                return HttpResponseRedirect('/changepassword/')

        else:
            fm=PasswordChangeForm(user=request.user)
    else:
        return HttpResponseRedirect('/')
    return render(request,'app/changepassword.html',{"form":fm})


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")




# Crud Oepration  for Expense Form

def DeleteItem(request,id):
    data=Expense.objects.get(pk=id)
    data.delete()
    messages.success(request,"Successfully deleted item")
    return HttpResponseRedirect('/expense/')


def EditItem(request,id):
    if request.method=='POST':
        data=Expense.objects.get(pk=id)
        fm=ExpenseForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Updated sucessfuly !! ")
            return HttpResponseRedirect('/viewexpense/')
    else:       
        data=Expense.objects.get(pk=id)
        fm=ExpenseForm(instance=data)
    return render(request,'app/edit.html',{"form":fm})




# Crud opertaion for task

def EditTask(request,id):
    if request.method=='POST':
        data=TaskModel.objects.get(pk=id)
        fm=TaskForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Updated sucessfuly !! ")
            return HttpResponseRedirect('/task/')
    else:       
        data=TaskModel.objects.get(pk=id)
        fm=TaskForm(instance=data)
    return render(request,'app/edittask.html',{"form":fm})


def DeleteTask(request,id):
    data=TaskModel.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/task/')




def MakeProfile(request):
    if request.method=="POST":
        fm=MakeProfileForm(request.POST, request.FILES)
        if fm.is_valid():
            user=request.user
            print(user)
            im=fm.cleaned_data['img']
            print(im)
            dsc=fm.cleaned_data['desc']
            print(dsc)
            occu=fm.cleaned_data["occupation"]
            print(occu)
            mar=fm.cleaned_data["martial"]
            pm=ProfileModel(user=user,img=im,desc=dsc,occupation=occu,martial=mar)
            pm.save()
            return HttpResponseRedirect('/profile/')
    else:
        fm=MakeProfileForm()
    return render(request,'app/makeprofile.html',{'form':fm})



def EditProfileUser(request,id):
    if request.method=='POST':
        data=ProfileModel.objects.get(pk=id)
        fm=EditProfileForm(request.POST,request.FILES,instance=data)
        if fm.is_valid():
            user=request.user
            print(user)
            im=fm.cleaned_data['img']
            dsc=fm.cleaned_data['desc']
            print(dsc)
            occu=fm.cleaned_data["occupation"]
            print(occu)
            mar=fm.cleaned_data["martial"]
            pm=ProfileModel(user=user,img=im,desc=dsc,occupation=occu,martial=mar)
            pm.save()
            return HttpResponseRedirect('/profile/')

    else:
        data=ProfileModel.objects.get(pk=id)
        fm=EditProfileForm(instance=data)
    
    return render(request,'app/editprofileu.html',{"form":fm})


# def BaseRender(request):
#     profiles=ProfileModel.objects.all()
#     user=request.user
#     return render(request,'app/base.html',{'user':user,'profiles':profiles})