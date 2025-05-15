from django.contrib import admin
from .models import Post, Comment   
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ("title", "slug", "author", "status")
    list_filter = ("status",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created_on"
    ordering = ("status", "created_on")


# Register your models here.
admin.site.register(Comment)
