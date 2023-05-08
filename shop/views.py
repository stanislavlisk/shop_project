from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .my_utils import password_check
from django.contrib.auth.decorators import login_required


from .forms import UserProfileUpdateForm, UserUpdateForm, ItemCategoryCreateForm, ItemModelCreateForm, \
    ItemCreateForm
from .models import ItemCategory, ItemModel, Item, Cart, CartItem

# html vistiek reikia pakeisti
admin_group_name = 'shop_admin'


def index(request):
    return redirect('view_items_models_list_n')

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            check_result = password_check(password, username)
            if check_result == 'ok':
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
                messages.error(request, f"error: {check_result}")
                return redirect('register_n')
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
    item_models_list = ItemModel.objects.all()
    item_list = ItemModel.objects.all()

    data = {
        'categories_num_cntx': categories_num,
        'categories_list_cntx': categories_list,
        'item_models_list_cntx': item_models_list,
        'item_list_cntx': item_list,
    }
    if admin_group_name in [group.name for group in request.user.groups.all()]:
        return render(request, 'administrator_page.html', context=data)
    else:
        return redirect('index_n')


# Item Category

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


# Item Model

class ItemModelCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = ItemModel
    form_class = ItemModelCreateForm
    success_url = "/app/administrator"
    template_name = "add_item_model.html"

    def form_valid(self, form):
        form.instance.form_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False


class ItemModelUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = ItemModel
    form_class = ItemModelCreateForm
    success_url = "/app/administrator"
    template_name = "add_item_model.html"

    def form_valid(self, form):
        form.instance.form_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False


class ItemModelDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = ItemModel
    success_url = "/app/administrator"
    template_name = "delete_item_model.html"

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False


class ItemModelListView(generic.ListView):
    model = ItemModel
    context_object_name = 'itemmodel_list'
    template_name = 'view_items_models_list.html'
    paginate_by = 6

    def get_queryset(self):
        query = ItemModel.objects.order_by('item_model_name')
        return query



class ItemModelDetailView(generic.DetailView):
    model = ItemModel
    context_object_name = 'itemmodel'
    template_name = 'view_item_model_detail.html'


# Item

class ItemCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = Item
    form_class = ItemCreateForm
    success_url = "/app/administrator"
    template_name = "add_item.html"

    def form_valid(self, form):
        form.instance.form_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Item
    form_class = ItemCreateForm
    success_url = "/app/administrator/view_items"
    template_name = "add_item.html"

    def form_valid(self, form):
        form.instance.form_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Item
    success_url = "/app/administrator/view_items"
    template_name = "delete_item.html"

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False


class ItemView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'view_items_list.html'
    paginate_by = 5

    def get_queryset(self):
        query = Item.objects.order_by('item_model_id')
        return query

    def test_func(self):
        user_groups_list = [group.name for group in self.request.user.groups.all()]
        if admin_group_name in user_groups_list:
            return True
        else:
            return False


@login_required
@csrf_protect
def user_cart_view(request):
    user_cart_id = request.user.cart.id  # galime trumpiau, grazint tiesiai cart
    cart = get_object_or_404(Cart, pk=user_cart_id)
    data = {
        'cart_cntx': cart,
    }
    return render(request, "user_cart.html", context=data)


@login_required
@csrf_protect
def add_item_to_cart(request):
    if request.method == "POST":
        data = request.POST
        item_id = data.get("item_to_add")
        item_obj_by_id = ItemModel.objects.get(pk=item_id)  # ItemModel object instance

        print(f"item id: {item_id}")
        print(f"item obj: {item_obj_by_id}")
        print(f"request user: {request.user}")
        print(f"request user cart: {request.user.cart}")

        if item_obj_by_id in [i.item_model_id for i in request.user.cart.cartitem_set.all()]:
            print("Already in CART!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            new_cart_item = CartItem()
            new_cart_item.item_model_id = item_obj_by_id
            new_cart_item.cart_id = request.user.cart
            new_cart_item.quantity = 1
            new_cart_item.user = request.user

            new_cart_item.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
@csrf_protect
def remove_item_from_cart(request):
    if request.method == "POST":
        data = request.POST
        item_id = data.get("item_to_delete")
        item_obj_by_id = CartItem.objects.get(pk=item_id)
        item_obj_by_id.delete()
        return redirect('user_cart_n')


@login_required
@csrf_protect
def increase_item_count(request):
    if request.method == "POST":
        data = request.POST
        item_id = data.get("increase_quantity")
        item_obj_by_id = CartItem.objects.get(pk=item_id)
        item_obj_by_id.quantity += 1
        item_obj_by_id.save()
        return redirect('user_cart_n')


@login_required
@csrf_protect
def decrease_item_count(request):
    if request.method == "POST":
        data = request.POST
        item_id = data.get("decrease_quantity")
        item_obj_by_id = CartItem.objects.get(pk=item_id)
        item_obj_by_id.quantity -= 1
        item_obj_by_id.save()
        return redirect('user_cart_n')
