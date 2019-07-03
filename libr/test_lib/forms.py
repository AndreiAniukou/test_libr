from django import forms
from .models import *
from django.core.exceptions import ValidationError

class TagForm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.CharField(max_length=100)

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug not be create')
        return new_slug


    def save(self):
        new_tag = Tag.objects.create(title=self.cleaned_data['title'],
                                     slug=self.cleaned_data['slug']
                                     )
        return new_tag


class UserForm(forms.ModelForm):
    class Meta:
        model = User_name
        fields = ['user_name', 'slug', 'tags']