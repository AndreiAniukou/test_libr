from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import User_name, Tag
from .utilits import ObjectDetailMixin
from .forms import TagForm
# Create your views here.

def users_list(request):
    users = User_name.objects.all()
    return render(request, 'test_lib/index.html', context={'users': users})


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


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'test_lib/tag_create.html', context={'form': form})

    def user(self, request):
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


