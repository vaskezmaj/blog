from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('naslov', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['naslov', 'sadrzaj']
    prepopulated_fields = {'slug': ('naslov',)}


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('ime', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('ime', 'email', 'body')
    actions = ['approve_comments']


admin.site.register(Comment)


def approve_comments(self, request, queryset):
    queryset.update(active=True)
