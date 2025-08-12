from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Group, Label, Expense

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group')
    search_fields = ('name',)
    list_filter = ('group',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'label', 'amount', 'date')
    list_filter = ('date', 'label__group')
    search_fields = ('label__name', 'user__username')
