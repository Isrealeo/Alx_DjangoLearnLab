from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable filtering by publication_year
    list_filter = ('publication_year',)
    
    # Enable search by title or author
    search_fields = ('title', 'author')

# Register Book model with custom admin
admin.site.register(Book, BookAdmin)
