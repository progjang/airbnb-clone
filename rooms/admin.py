from django.contrib import admin
from rooms.models import Room, RoomType, Amenity, Facility, HouseRule, Photo
from django.utils.html import mark_safe
# Register your models here.

@admin.register(RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name", "used_by"
    )

    def used_by(self, obj):
        rooms = obj.rooms.count()
        return rooms


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating"
    )

    search_fields = ("=city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")
    raw_id_fields = ("host",)

    inlines = (PhotoInline,)

    def count_amenities(self, obj):
        amenities = obj.amenities.count()
        return amenities

    count_amenities.short_description = "Amenities"

    def count_photos(self, obj):
        photos = obj.photos.count()
        return photos

    count_photos.short_description = "Photo Count"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src= '{obj.file.url}' />")
    
    get_thumbnail.short_description = "Thumbnail"
