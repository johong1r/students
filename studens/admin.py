from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Group, Tag, StudentContract

from django.utils.html import format_html

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'group', 'logo_preview',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'group',)
    list_filter = ('group__name', 'age', 'tags',)
    ordering = ('updated_date',)
    list_editable = ("age",)
    readonly_fields = ['updated_date', 'join_date', 'logo_preview']
    fieldsets = (
        ('Основная информация', {
            'fields': ('avatar', 'name', 'age', 'group', 'email', 'phonenumber', 'discription', )
        }),
        ('Дополнительная информация', {
            'fields': ['updated_date']
        })
    )
    date_hierarchy = 'join_date'
    save_on_top = True

    def logo_preview(self, obj):
        if obj.avatar and hasattr(obj.avatar, 'url'): 
            return format_html('<img src="{}" width="60" height="60" style="border-radius:5px;"/>', obj.avatar.url)
        return "— нет аватара —"  # вместо ошибки

    logo_preview.short_description = "Аватар"


class GroupAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')         
    search_fields = ('name',)             
    list_per_page = 20   


class StudentContractAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name')         
    # search_fields = ('name',)             
    # list_per_page = 20   
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(StudentContract, StudentContractAdmin)
