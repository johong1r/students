import django_filters

from .models import Student, Group, Tag
from django import forms

class StudentFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr="icontains", label="Имя десерта")
    groups = django_filters.ModelChoiceFilter(
    queryset=Group.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control'}),
    empty_label="Выберите группу"
)

    tags = django_filters.ModelMultipleChoiceFilter(
    queryset=Tag.objects.all(),
    widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
)



    class Meta:
        model = Student
        fields = ("groups", "tags")