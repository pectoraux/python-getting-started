from django.contrib import admin
from .models import Document
# Register your models here. 
    
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['email', 'document_id', 'document_utility']