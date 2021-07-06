from django.contrib import admin
from .models import Document
# Register your models here.
from attachments.admin import AttachmentInlines

class MyEntryOptions(admin.ModelAdmin):
    inlines = (AttachmentInlines,)
    
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['email', 'document_id', 'document_utility']