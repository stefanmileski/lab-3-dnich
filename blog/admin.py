from django.contrib import admin
from .models import Post, MyUser, File, Blocklist, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and request.user == obj.author.user:
            return True
        return False


admin.site.register(Post, PostAdmin)


class MyUserAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and request.user == obj.user:
            return True
        return False


admin.site.register(MyUser, MyUserAdmin)


class FileAdmin(admin.ModelAdmin):
    pass


admin.site.register(File, FileAdmin)


class BlocklistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blocklist, BlocklistAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and obj.post and request.user == obj.author.user:
            return True
        if obj and obj.post and request.user == obj.post.author.user:
            return True
        return False


admin.site.register(Comment, CommentAdmin)
