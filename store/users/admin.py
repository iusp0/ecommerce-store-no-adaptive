from django.contrib import admin


from .models import User, Questions
from main.admin import BasketAdmin



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'email']
    inlines = [BasketAdmin]

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
