from django.db.models.signals import post_delete, pre_save, post_delete, m2m_changed, post_save
from django.dispatch import receiver

from .models import Student, StudentContract


@receiver(post_save, sender=Student)
def student_contract_create_signal(sender, instance: Student, created, **kwargs):
    if not created:
        return