from django.urls import path

from .views import MainTemplateView, AboutTemplateView, StudentListFilter


urlpatterns = [
    path('', MainTemplateView.as_view(), name="main"),
    path('about/', AboutTemplateView.as_view(), name="about"),
    # path('', StudentListView.as_view(), name="main")
]