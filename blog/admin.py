from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('naslov', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['naslov', 'sadrzaj']
    prepopulated_fields = {'slug': ('naslov',)}


admin.site.register(Post, PostAdmin)
