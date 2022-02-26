from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Comment, Post, PostLikes,CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_pic',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('custom_field',)}),
    )

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('likes',)
    fieldsets = [
        (None,               {'fields': ['media_path','owner', 'media_desc']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [CommentInline]
    list_display = ('media_path',  'owner', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['media_path']



admin.site.register(Post, PostAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
