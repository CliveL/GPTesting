from django.contrib import admin

from buyside.models import Listings, VehiclePart, Vehicle


class ListingInline(admin.TabularInline):
    model = Listings
    extra = 1


class VehiclePartListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['gecko_part_number', 'name']}),
        ('Search Tree Location', {'fields': ['tree_level_1',
                                             'tree_level_2',
                                             'tree_level_3',
                                             'tree_level_4',
                                             'tree_level_5']
        }),
        ('Vehicles', {'fields': ['vehicles']})
    ]
    inlines = [ListingInline]

class VehicleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['vehicle_id', 'short_name', 'long_name', 'min_year', 'max_year', 'fuel_type', 'body_type']})
    ]



admin.site.register(VehiclePart, VehiclePartListAdmin)
admin.site.register(Vehicle, VehicleAdmin)