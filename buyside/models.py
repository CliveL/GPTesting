from django.db import models

# contains only and all information necessary for search page


TLA_LENGTH = 3  # (Three Letter Acronym)
ID_LENGTH = 8
LONG_ID_LENGTH = 15
NAME_LENGTH = 32
TYPE_LENGTH = 12
DESCRIPTION_LENGTH = 400
CONDITION_CHOICES = (
    (1, 'Excellent'),
    (2, 'Good'),
    (3, 'Fair'),
    (4, 'Poor')
)
DELIVERY_STATUS = (
    (1, 'Available for purchase'),
    (2, 'Reserved'),
    (3, 'Order Received'),
    (4, 'Awaiting Pickup'),
    (5, 'With Courier'),
    (6, 'Delivered - On Time'),
    (7, 'Delivered - Late')
)
RETURN_STATUS = (
    (1, 'Received <90 days'),
    (2, 'Disputed - Unresolved'),
    (3, 'Disputed - Resolved Satisfactorily'),
    (4, 'Disputed - Resolved but Unsatisfactory'),
    (5, 'Recieved >90 days')
)
RETURN_REASON = (
    (1, 'Wrong Part'),
    (2, 'Sub-standard Condition'),
    (3, 'Late delivery, replacement sourced')
)


class Vehicle(models.Model):
    vehicle_id = models.CharField(primary_key=True, max_length=ID_LENGTH)  # e.g. GOL00032
    short_name = models.CharField(max_length=NAME_LENGTH)  # e.g. Golf
    long_name = models.CharField(max_length=200)
    # e.g. Golf GT TDI 2001-2003 Diesel 1.9l PD 130hp 5 door
    # Human readable 1 to 1 with Model ID
    # marque_id = models.ForeignKey(Marques)
    min_year = models.DecimalField(max_digits=4, decimal_places=0)
    max_year = models.DecimalField(max_digits=4, decimal_places=0)
    fuel_type = models.CharField(max_length=TYPE_LENGTH)
    body_type = models.CharField(max_length=TYPE_LENGTH)
    def __unicode__(self):
        return self.long_name


class VehiclePart(models.Model):
    gecko_part_number = models.CharField(primary_key=True, max_length=LONG_ID_LENGTH)  # e.g. VAGABC123456789
    manufacturer_part_number = models.CharField(max_length=32, null=True, blank=True)  # e.g. 1J0 145 762 BD
    vehicles = models.ManyToManyField(Vehicle)
    name = models.CharField(max_length=DESCRIPTION_LENGTH)  # e.g. intercooler duct; intercooler link
    tree_level_1 = models.CharField(max_length=NAME_LENGTH)  # e.g. Exterior
    tree_level_2 = models.CharField(max_length=NAME_LENGTH, null=True, blank=True)  # e.g. NULL or Doors
    tree_level_3 = models.CharField(max_length=NAME_LENGTH, null=True, blank=True)  # e.g. NULL or Front Right Door
    tree_level_4 = models.CharField(max_length=NAME_LENGTH, null=True, blank=True)  # e.g. NULL or Handle and Lock
    tree_level_5 = models.CharField(max_length=NAME_LENGTH, null=True, blank=True)  # e.g. NULL or Lock barrel
    def __unicode__(self):
        return self.name


class Listings(models.Model):
    listing_number = models.CharField(primary_key=True, max_length=LONG_ID_LENGTH)  # e.g. AA0000123456789
    gecko_part_number = models.ForeignKey(VehiclePart)
    description = models.CharField(max_length=DESCRIPTION_LENGTH, null=True, blank=True)
    date_listed = models.DateField()
    date_sold = models.DateField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    part_condition = models.IntegerField(max_length=1, choices=CONDITION_CHOICES, default=4)
    part_mileage = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)
    additional_info = models.CharField(max_length=DESCRIPTION_LENGTH, null=True, blank=True)
    reserved = models.BooleanField(default=False)
    delivery_status = models.IntegerField(max_length=1, choices=DELIVERY_STATUS, default=1)
    return_status = models.IntegerField(max_length=1, choices=RETURN_STATUS, null=True, blank=True)
    return_reason = models.IntegerField(max_length=1, choices=RETURN_REASON, null=True, blank=True)
    return_description = models.CharField(max_length=DESCRIPTION_LENGTH, null=True, blank=True)

class DonorVehicle(models.Model):
    donor_id = models.CharField(primary_key=True, max_length=LONG_ID_LENGTH)  # e.g.
    vehicle_id = models.ForeignKey(Vehicle)
    description = models.CharField(max_length=DESCRIPTION_LENGTH)
    mileage = models.DecimalField(max_digits=7, decimal_places=0)
    eol_reason = models.CharField(max_length=DESCRIPTION_LENGTH)
    colour_code = models.CharField(max_length=4)
    overall_condition = models.IntegerField(max_length=1, choices=CONDITION_CHOICES)
    bodywork_condition = models.IntegerField(max_length=1, choices=CONDITION_CHOICES)
    mechanical_condition = models.IntegerField(max_length=1, choices=CONDITION_CHOICES)
    interior_condition = models.IntegerField(max_length=1, choices=CONDITION_CHOICES)
