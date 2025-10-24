from django import forms

from studens.models import Student, Group, Tag


class StudentForm(forms.Form):
    name = forms.CharField(label="Имя студента", widget=forms.TextInput(attrs={"class": "student_input student_input2", }))
    last_name = forms.CharField(label="Last name", required=False)
    age = forms.IntegerField(label="Возраст студента", required=False)
    email = forms.EmailField(label="Электронная почта", required=False, widget=forms.EmailInput(attrs={"class": "student_input student_input2", }))
    phone_number = forms.CharField(label="Номер телефона")
    group = forms.ModelChoiceField(label="Группа", queryset=Group.objects.all())
    avatar = forms.ImageField(label="Аватарка", required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    # join_date = forms.DateField(label="Дата присоединения")
    # updated_date = forms.DateTimeField(label="Дата обновления")
    is_active = forms.BooleanField(label="Активен", required=False)



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'last_name', 'age', 'email', 'phone_number', 'group', 'avatar', 'is_active', 'tags')
        labels = {
            'name': 'Имя студента',
            'last_name': 'Last name',
            'age': 'Возраст студента',
            'email': 'Электронная почта',
            'phone_number': 'Номер телефона',
            'group': 'Группа',
            'avatar': 'Аватарка',
            'is_active': 'Активен',
            "tags": "теги",
        }

        widgets = {
            'name': forms.TextInput(attrs={"class": "student_input"}),
            'tags': forms.CheckboxSelectMultiple(attrs={"class": "student_input"})
        }