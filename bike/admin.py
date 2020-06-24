from django.contrib import admin
from bike.models import BookingDetails,COBBikesData,COBScooterName,COBBikesCategory,COBScooterCategory

admin.site.register(COBScooterCategory)
admin.site.register(COBBikesData)
admin.site.register(COBBikesCategory)
admin.site.register(COBScooterName)
admin.site.register(BookingDetails)
