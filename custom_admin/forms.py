from django import forms
from .models import Student, Group, Tag

class StudentForm(forms.Form):
    avatar = forms.ImageField(label="Логотип", required=False)
    name = forms.CharField(max_length=100, label='Имя')
    age = forms.IntegerField(label='Возраст', required=False)
    email = forms.EmailField(label='Почта')
    group = forms.ModelChoiceField(label="Группа", queryset=Group.objects.all())
    discription = forms.CharField(label="Описание студента", required=False)
    is_active = forms.BooleanField(label='В присутствие',  required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'group', 'email', 'discription', 'avatar', 'is_active', 'tags']
        labels = {
            'name': 'Имя',
            'age': 'Возраст',
            'group': 'Группа',
            'email': 'Электронная почта',
            'discription': 'Описание',
            'avatar': 'Логотип',
            'is_active': 'В присутствие',
            'tags': 'Теги'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите ваш email', 'class': 'form-control', 'id': 'email-field'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
