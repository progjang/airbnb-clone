from django.contrib import admin
from rooms.models import Room, RoomType, Amenity, Facility, HouseRule, Photo
# Register your models here.

@admin.register(RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name", "used_by"
    )

    def used_by(self, obj):
        rooms = obj.rooms.count()
        return rooms


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

    def count_amenities(self, obj):
        amenities = obj.amenities.count()
        return amenities

    count_amenities.short_description = "Amenities"

    def count_photos(self, obj):
        photos = obj.photos.count()
        return photos


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass