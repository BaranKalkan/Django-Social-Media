from django.contrib import admin


from .models import Comment, Post, PostLikes

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
