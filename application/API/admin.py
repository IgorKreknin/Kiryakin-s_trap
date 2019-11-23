from django.contrib import admin
from .models import ParkingSlot, Camera, Path, Kiosk

admin.site.register(ParkingSlot)
admin.site.register(Camera)
admin.site.register(Path)
admin.site.register(Kiosk)
