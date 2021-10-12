from django.contrib import admin
from .models import Contact
from .models import Post

# Customize Blog Post Data
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'published_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Contact)
admin.site.register(Post, PostAdmin)
