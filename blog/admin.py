from django.contrib import admin
from .models import Post, Comment



class UserInline(admin.TabularInline):
    from django.contrib.auth.models import User
    model = User


class PostInline(admin.TabularInline):
    model = Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_filter = ['id']
    #inlines = [PostInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date_posted', 'author']
    list_filter = ['author']
    fieldsets = (
        (
            'BASIC', {'fields': ('title', 'author')}
        ),
        (
            'DETAILS', {'fields': ('date_posted', 'content')}
        )
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
