from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Book, FileSave


class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'publication_date')


admin.site.register(Book, BookAdmin)
admin.site.register(FileSave)