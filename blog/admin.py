from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	# This are the attibutes of the instance shown as columns
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	# This is the list of filtering options displayed as a side bar
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug':('title', )}
	raw_id_fields = ('author', )
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')