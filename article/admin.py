from django.contrib import admin
from .models import Article, ArticleImage, Author, Category, Comment

class ImageInLine(admin.TabularInline):
    model = ArticleImage
    extra = 2
    fields = ('image', )

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]

    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
