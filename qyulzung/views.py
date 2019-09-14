from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from .models import QZ, Topic
from time import sleep


#QZ or qz = "Qyulzung" = "Decision"

# Login/Logout/Signout form reference from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
@login_required
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login", {"message": None})

    topic = Topic.objects.all()
    return render(request, "index.html", {"topic": topic})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Open contact page.
def contact(request):
    return render(request, 'contact.html')

# Open about page.
def about(request):
    return render(request, "about.html")


# Step1: index.html --> step1.html, checks methods, if it is POST then clear the ongoing boolean value to False and Make a new "QZ".
def step1(request, user):
    if request.method == "POST":
        topic = request.POST["defineproblem"]
        qz = QZ.objects.filter(user=request.user, ongoing=True)
        if qz.count() > 0:
            qz.update(ongoing=False)

        QZ.objects.create(user=request.user, topic=topic, ongoing=True, post_yn=False)

        context = {
            "topic": topic,
        }
        return render(request, "step1.html", context)
    else:
        return render(request, 'error.html', {"message": 'Please do not try to refresh or connect directly through the URL.'})

# Step2: step1.html --> step2.html, get alternatives value and save it, and return to step2 oage,
def step2(request, user):
    if request.method == "POST":
        qz = QZ.objects.get(user=request.user, ongoing=True)
        topic = qz.topic
        alt1 = request.POST["alt1"]
        alt2 = request.POST["alt2"]
        alt3 = request.POST["alt3"]

        QZ.objects.filter(user=request.user, ongoing=True, topic=topic).update(alt1=alt1, alt2=alt2, alt3=alt3)

        context = {
            "topic": topic,
        }
        return render(request, "step2.html", context)
    else:
        return render(request, 'error.html', {"message": 'Please do not try to refresh or connect directly through the URL.'})

# Step3: step2.html --> step3.html, create 3 Criteria and return to step3.html
def step3(request, user):
    if request.method == "POST":
        qz = QZ.objects.get(user=request.user, ongoing=True)
        topic = qz.topic

        cr1 = request.POST["cr1"]
        cr2 = request.POST["cr2"]
        cr3 = request.POST["cr3"]

        QZ.objects.filter(user=request.user, ongoing=True, topic=topic).update(cr1=cr1, cr2=cr2, cr3=cr3)

        context = {
            "cr1": cr1, "cr2": cr2, "cr3": cr3,
            "topic": topic,
            "range": range(1, 6),
        }
        return render(request, "step3.html", context)
    else:
        return render(request, 'error.html', {"message": 'Please do not try to refresh or connect directly through the URL.'})

# Step4: step3.html --> step4.html Weigh the criteria and give the score to step4.html
def step4(request, user):
    if request.method == "POST":
        qz = QZ.objects.get(user=request.user, ongoing=True)
        topic = qz.topic

        score1 = int(request.POST["score1"])
        score2 = int(request.POST["score2"])
        score3 = int(request.POST["score3"])

        QZ.objects.filter(user=request.user, ongoing=True, topic=topic).update(cr1sco = score1, cr2sco = score2, cr3sco = score3)

        context = {
            "qz": qz,
            "range": range(1, 11),
        }


        return render(request, "step4.html", context)
    else:
        return render(request, 'error.html', {"message": 'Please do not try to refresh or connect directly through the URL.'})

# Result: step4.html --> Result.html, Multiply each of Criterion Score and Alternative Score, save it and then return to result.html
def result(request, user):
    if request.method == "POST":

        qz = QZ.objects.get(user=request.user, ongoing=True)
        topic = qz.topic

        cr1sco = qz.cr1sco
        cr2sco = qz.cr2sco
        cr3sco = qz.cr3sco

        score1_1 = int(request.POST["score1_1"])*cr1sco
        score1_2 = int(request.POST["score1_2"])*cr2sco
        score1_3 = int(request.POST["score1_3"])*cr3sco

        score2_1 = int(request.POST["score2_1"])*cr1sco
        score2_2 = int(request.POST["score2_2"])*cr2sco
        score2_3 = int(request.POST["score2_3"])*cr3sco

        score3_1 = int(request.POST["score3_1"])*cr1sco
        score3_2 = int(request.POST["score3_2"])*cr2sco
        score3_3 = int(request.POST["score3_3"])*cr3sco

        alt1_sco = int(score1_1 + score1_2 + score1_3)
        alt2_sco = int(score2_1 + score2_2 + score2_3)
        alt3_sco = int(score3_1 + score3_2 + score3_3)

        QZ.objects.filter(user=request.user, ongoing=True, topic=topic).update(alt1sco = alt1_sco, alt2sco = alt2_sco, alt3sco = alt3_sco)

        context = {
            "qz":qz,
            "alt1sco":alt1_sco, "alt2sco":alt2_sco, "alt3sco":alt3_sco,
            "score1_1": score1_1, "score1_2": score1_2, "score1_3": score1_3,
            "score2_1": score2_1, "score2_2": score2_2, "score2_3": score2_3,
            "score3_1": score3_1, "score3_2": score3_2, "score3_3": score3_3,
        }
        sleep(0.3)
        return render(request, "result.html", context)
    else:
        return render(request, 'error.html', {"message": 'Please do not try to refresh or connect directly through the URL.'})

# Input comments in the Decision.
def comment(request, user):
    qz = QZ.objects.get(user=request.user, ongoing=True)
    topic = qz.topic
    comment = request.POST["comments"]

    QZ.objects.filter(user=request.user, ongoing=True, topic=topic).update(comment=comment)

    return render(request, 'success.html', {"message": 'Your "Qyulzung" is now successfully saved. Now you can review your Decision Log, or share it to the public.'})

# List user's previous decisions.
def journal(request, user):
    qz = QZ.objects.filter(user=request.user).order_by('-time')

    context = {
        "qz": qz,
    }
    return render(request, "journal.html", context)


def journals(request, arg1, arg2):
    journal = QZ.objects.get(pk=arg2)

    context = {
        "journal": journal,
    }
    return render(request, "journals.html", context)

# List every user's previous decisions which allowed to post.
def board(request):
    qz = QZ.objects.filter(post_yn=True).order_by('time')
    user = request.user

    context = {
        "qz":qz,
        "user": user,
    }
    return render(request, "board.html", context)

# Post a Decision to Board.
def post(request, arg1, arg2):

    if QZ.objects.get(pk=arg2).post_yn == False:
        QZ.objects.filter(pk=arg2).update(post_yn=True)
        return render(request, "success.html", {"message":'Your Decision Log has succesfully posted.'})
    else:
        return render(request, 'error.html', {"message": 'Posted already.'})

# Unpost a Decision to Board.
def unpost(request, arg1, arg2):
    QZ.objects.filter(pk=arg2).update(post_yn=False)
    return render(request, "success.html", {"message":'Your Decision Log has succesfully unposted.'})





def delete(request, arg1):
    QZ.objects.filter(pk=arg1).delete()
    return render(request, "success.html", {"message":'Deleted.'})