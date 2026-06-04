from django.contrib import admin

from .models import City, Place, Comment


class PlaceInline(admin.TabularInline):
    model = Place
    extra = 0
    fields = ('name', 'place_type', 'address', 'image_url')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'continent', 'welcome_score', 'score_count')
    list_filter = ('continent',)
    prepopulated_fields = {'slug': ('name', 'country')}
    search_fields = ('name', 'country', 'continent')
    inlines = [PlaceInline]
    readonly_fields = ('score_count', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'country', 'continent', 'slug')}),
        ('Content', {'fields': ('description', 'meta_description')}),
        ('Score', {'fields': ('welcome_score', 'score_count')}),
        ('Location', {'fields': ('latitude', 'longitude')}),
        ('Media', {'fields': ('hero_image_url', 'hero_image_attribution_name', 'hero_image_attribution_url')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'place_type')
    list_filter = ('place_type', 'city__continent')
    search_fields = ('name', 'city__name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'city', 'score', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'city__continent')
    search_fields = ('author__username', 'city__name')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = 'Approve selected comments'