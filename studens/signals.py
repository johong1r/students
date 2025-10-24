from django.db.models.signals import post_save, pre_save, pre_delete, post_delete, m2m_changed
from django.dispatch import receiver

from .models import Student, StudentContract


@receiver(post_save, sender=Student)
def student_contract_create_signal(sender, instance: Student, created, **kwargs):
    if created:
        contract = StudentContract.objects.create(student=instance)