from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import *
from .utilits import ObjectDetailMixin
from .forms import TagForm, UserForm


def users_list(request):
    users = User_name.objects.all()
    return render(request, 'test_lib/index.html', context={'users': users})

def book_list(request):
    book_name = BookName.objects.all()
    return render(request, 'test_lib/book.html', context={'book_name': book_name})

def book_detail(request, slug):
    book = BookName.objects.get(slug_iexact=slug)
    book = get_object_or_404(BookName, slug_iexact=slug)
    return render(request, 'test_lib/book.html', context={'book', book})





#def user_detail(request, slug):
 #   user = User_name.objects.get(slug_iexact=slug) #получает из бд ссылку
  #  return render(request, 'test_lib/user_detail.html', context={'user': user})


class UserDetail(ObjectDetailMixin, View):
    model = User_name
    template = 'test_lib/user_detail.html',

    #def get(self, request, slug):
        #user = User_name.objects.get(slug_iexact=slug)  # получает из бд ссылку
     #   user = get_object_or_404(User_name, slug_iexact=slug)
      #  return render(request, 'test_lib/user_detail.html', context={'user': user})

class UserCreate(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'test_lib/user_create_form.html', context={'form': form})

    def post(self,request):
        bound_form = UserForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect(new_user)
        return render(request, 'test_lib/user_create_form.html', context={'form': bound_form})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'test_lib/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'test_lib/tag_create.html', context={'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'test_lib/tags_list.html', context={'tags': tags})


#def tag_detail(request, slug):
 #   tag = Tag.objects.get(slug_iexact=slug)
  #  return render(request, 'test_lib/tag_detail.html', context={'tag': tag})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'test_lib/tag_detail.html',

    #def get(self, request, slug):
        #tag = Tag.objects.get(slug_iexact=slug)
        #tag = get_object_or_404(Tag, slug_iexact=slug)
      #  return render(request, 'test_lib/tag_detail.html', context={'tag': tag})


