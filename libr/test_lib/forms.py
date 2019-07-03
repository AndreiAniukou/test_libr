from django import forms
from .models import *
from django.core.exceptions import ValidationError

class TagForm(forms.Form):
    class Meta:
        model = Tag
        fields = ['name_tag', 'slug']

        widgets = {
            'name_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

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

        widgets = {
            'user_name':  forms.TextInput(attrs={'class': 'form-control'}),
            'slug':  forms.TextInput(attrs={'class': 'form-control'}),
            'tags':  forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug not be create')
        return new_slug

