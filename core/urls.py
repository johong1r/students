"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studens.views import main
from django.conf import settings
from django.conf.urls.static import static
from studens.views import main, detels, update_student, create_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('main/student/<int:id>/', detels, name='dateils'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('create_student/', create_student, name='create_student'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)