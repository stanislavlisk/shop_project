from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


def index(request):
    paslaugos = ['vienas', 'du', 'trys']
    data = {
        'paslaugos_c': paslaugos
    }

    return render(request, 'index.html', context=data)


@csrf_protect
def register(request):
    if request.method == "POST":
        # duomenu surinkimas is register formos
        #return render(request, "book_list.html")

        username = request.POST['username']
        # username = request.POST.get('username') #naudojant zodyno metoda get, post yra zodynas
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # ar sutampa slaptazodziai?
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username %s ir already exists" % username)
                return redirect('register_n')
            else:
                # ar nera sistemoj tokio pat vartotojo email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f"Vartotojas su email '{email}' jau egzistuoja")
                    return redirect('register_n')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f"Vartotojas {username} užregistruotas !")
                    return redirect('login')
        else:
            messages.error(request, f"Slaptažodžiai turi sutapti !")
            return redirect('register_n')

    return render(request, "registration/register.html")
