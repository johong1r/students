from django.urls import path

from .views import StudentCreateView, MainAdminView

urlpatterns = [
    path("", MainAdminView.as_view(), name="admin_view"),
    path("students/create/", StudentCreateView.as_view(), name="create_student")
]
