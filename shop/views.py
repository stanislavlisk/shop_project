from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .my_utils import password_check
from django.contrib.auth.decorators import login_required

from .forms import UserProfileUpdateForm, UserUpdateForm, ItemCategoryCreateForm, ItemModelCreateForm
from .models import ItemCategory, ItemModel


admin_group_name = 'shop_admin'

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
            if password_check(password, username):
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
                messages.error(request, f"Slaptažodis turi turėti bent vieną skaičių, simbolį ir didžiąją raidę")
                return redirect('login')
        else:
            messages.error(request, f"Slaptažodžiai turi sutapti !")
            return redirect('register_n')

    return render(request, "registration/register.html")

@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('user_profile_n')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.userprofile)

    data = {
        'u_form_cntx': u_form,
        'p_form_cntx': p_form,
    }
    return render(request, "user_profile.html", context=data)


@login_required
def administrator_page(request):
    categories_num = ItemCategory.objects.all().count()
    categories_list = ItemCategory.objects.all()

    data = {
        'categories_num_cntx': categories_num,
        'categories_list_cntx': categories_list
    }
    if admin_group_name in [group.name for group in request.user.groups.all()]:
        return render(request, 'administrator_page.html', context=data)
    else:
        return redirect('index_n')


# ItemCategory create, update, delete

class ItemCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = ItemCategory
    success_url = "/app/administrator"
    template_name = "add_item_category.html"
    form_class = ItemCategoryCreateForm

    def form_valid(self, form):
        form.instance.form_user = self.request.user
        print(f"formos naudotojas: {form.instance.form_user}")
        return super().form_valid(form)

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False

class ItemCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = ItemCategory
    success_url = "/app/administrator"
    template_name = "add_item_category.html"
    form_class = ItemCategoryCreateForm

    def form_valid(self, form):
        form.instance.form_user = self.request.user
        print(f"formos naudotojas: {form.instance.form_user}")
        return super().form_valid(form)

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False

class ItemCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = ItemCategory
    success_url = "/app/administrator"
    template_name = "delete_item_category.html"

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False


# ItemModel create, update, delete

class ItemModelCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = ItemModel
    success_url = "/app/administrator"
    template_name = "add_item_model.html"
    form_class = ItemModelCreateForm

    def form_valid(self, form):
        form.instance.form_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False
















