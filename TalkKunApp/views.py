import email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from TalkKunApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html', {'questions': Question.objects.all()})

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = 'Invalid Password OR Invalid Username'
            return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        user = User.objects.create_user(username=username,
                                    email=email,
                                    password=pwd)
        try:                            
            user.save()
            return render(request, 'login.html')
        except:
            msg = "Register Failed"
            return render(request, 'register.html', {'msg': msg})
    else:
        return render(request, 'register.html')

def Logout(request):
    logout(request)
    return redirect('/')

def detail(request, id):
    qid = Question.objects.get(id=id)
    ans = Answer.objects.filter(question=qid).select_related('user')
    return render(request, 'detail.html', {'detailQ': qid, 'answers': ans})
    
def detailForme(request, id):
    qid = Question.objects.get(id=id)
    return render(request, 'detailforme.html', {'detailQ': qid})

def statusAdd(status, text):
    statustext = ""
    msg = ""
    if status:
        statustext = "success"
        msg = text + " Success"
    else:
        statustext = "error"
        msg = text + " Failed"

    return [statustext, msg]


def addQ(request):
    if request.method == "POST":
        title = request.POST['title']
        detail = request.POST['detail']
        img = request.FILES['imgFile']
        uid = User.objects.get(id=request.user.id)
        if str((img.name)[-3:]) in ['jpg', 'png']:
            q = Question(title=title, detail=detail, image=img, user=uid)
            q.save()
            status, msg = statusAdd(True, "Add Question")
            return render(request, 'addQuestion.html', {'status':status, 'msg':msg})
        else:
            status, msg = statusAdd(False, "Add Question")
            return render(request, 'addQuestion.html', {'status':status, 'msg':msg})
    else:
        if request.user.is_authenticated:
            return render(request, 'addQuestion.html')
        else:
            return render(request, 'login.html')

def QuestionMe(request):
    if request.user.is_authenticated:
        try:
            uid = User.objects.get(id=request.user.id)
            questions = Question.objects.filter(user=uid)
            return render(request, 'questionMe.html', {'questions': questions })
        except:
            return render(request, 'questionMe.html', {'questions': None })
    else:
        return render(request, 'login.html')

def answer(request):
    if request.method == "POST":
        uid = User.objects.get(id=request.user.id)
        qid = Question.objects.get(id=request.POST['qid'])
        ans = request.POST['answer']
        answer = Answer(answer=ans, user=uid, question=qid)
        answer.save()
        return redirect(f"/detail/{request.POST['qid']}")

def editQ(request):
    title = request.POST['title']
    qid = int(request.POST['qid'])
    detail = request.POST['detail']
    now = timezone.now()
    try:
        img = request.FILES['imgFile']
        if str((img.name)[-3:]) in ['jpg', 'png']:
            Qedit = Question.objects.get(id=qid)
            Qedit.title = title
            Qedit.detail = detail
            Qedit.image = img
            Qedit.date = now
            Qedit.save()
            return redirect(f'QuestionMe/detailForme/{qid}')
    except:
        Qedit = Question.objects.get(id=qid)
        Qedit.title = title
        Qedit.detail = detail
        Qedit.date = now
        Qedit.save()
        return redirect(f'QuestionMe/detailForme/{qid}')

def deleteQ(request, id):
    Question.objects.filter(id=id).delete()
    return redirect('/QuestionMe')
    

        
    





    
    