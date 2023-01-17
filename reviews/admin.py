from django.contrib import admin
from .models import Review, Comments, WatchLater
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_filter = ('status', 'publish_date',) # may not need
    list_display = ('title', 'slug', 'status', 'publish_date') # may not need
    search_fields = ['title', 'content'] # May not need
    prepopulated_fields = {'slug': ('title',)} #
    summernote_fields = ('description', 'review', 'body')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('username', 'body', 'comment_date', 'approved')
    list_filter = ('approved', 'comment_date')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        