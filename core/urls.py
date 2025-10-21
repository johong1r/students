from django.contrib import admin
from django.urls import path
# from studens.views import main
from django.conf import settings
from django.conf.urls.static import static
# from studens.views import main, detels, update_student, create_student
from students.views import StudentView, StudentDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentView.as_view(), name="main"),
    path('students/<int:id>/', StudentDetailView.as_view(), name='dateils'),
    # path('update_student/<int:id>/', update_student, name='update_student'),
    # path('create_student/', create_student, name='create_student'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)