from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'creation_date')
    list_filter = ['creation_date', 'status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
