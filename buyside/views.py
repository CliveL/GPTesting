from django.shortcuts import render
#from django.views.generic import TemplateView

from forms import VehicleDetailForm
from idtests import is_vehicle_id, is_part_id, is_listing_id
from models import Vehicle, VehiclePart, Listings
from buyside.helpers.treebuilder import ListNode, PartTree, PartList


# Create your views here.


def search(request, search_id_1=None, search_id_2=None):
    # need to add error handling
    # what to do with numbers which are not ID values
    # what to do with numbers which are ID values, but not in the database.

    # create blank context dictionary to be updated in method
    context = {}
    # will only recognise a vehicle ID if it is the first of the search ID's
    if is_vehicle_id(search_id_1):
        target_vehicle = Vehicle.objects.get(pk=search_id_1)
        context.update({'target_vehicle': target_vehicle})
        #vehicle_parts = VehiclePart.objects.filter(vehicles=search_id_1)
        #parts = ListNode('', target_vehicle.long_name, search_id_1, 0)
        #for vehicle_part in vehicle_parts:
            # url, name, category list
            #if vehicle_part.tree_level_5 == '':
            #    print 'I am here'
        #    parts.add_node(
        #        vehicle_part.gecko_part_number,
        #        vehicle_part.name,
        #        [
        #            vehicle_part.tree_level_1,
        #            vehicle_part.tree_level_2,
        #            vehicle_part.tree_level_3,
        #            vehicle_part.tree_level_4,
        #            vehicle_part.tree_level_5
        #        ])
        all_vehicle_parts = PartTree(search_id_1, 'shop')
        context.update({'all_vehicle_parts': all_vehicle_parts})

        if search_id_2 is not None:
            if is_part_id(search_id_2):
                single_part = VehiclePart.objects.get(gecko_part_number=search_id_2).listings_set.all()
                context.update({'single_part': single_part})

            elif is_part_id(search_id_2) is False and is_listing_id(search_id_2):
                single_listing = Listings.objects.get(listing_number=search_id_2)
                context.update({'single_listing': single_listing})

            #elif search_id_2 is None:
            #    context.update({'single_part': vehicle_parts})

    elif is_vehicle_id(search_id_1) is False and is_part_id(search_id_1):
        single_part = VehiclePart.objects.get(gecko_part_number=search_id_1)
        context.update({'single_part': single_part})
        fits_vehicle = single_part.vehicles.all()
        context.update({'fits_vehicle': fits_vehicle})

        if search_id_2 is not None:
            if is_listing_id(search_id_2):
                single_listing = Listings.objects.get(listing_number=search_id_2)
                context.update({'single_listing': single_listing})

    elif search_id_2 is not None:
        if is_vehicle_id(search_id_1) is False and is_part_id(search_id_1) is False and is_part_id(search_id_2):
            single_part = VehiclePart.objects.get(gecko_part_number=search_id_2)
            context.update({'single_part': single_part})

    elif is_vehicle_id(search_id_1) is False and is_part_id(search_id_1) is False and is_listing_id(search_id_1):
        single_listing = Listings.objects.get(listing_number=search_id_1)
        context.update({'single_listing': single_listing})
        fits_vehicle = single_listing.gecko_part_number.vehicles.all()
        context.update({'fits_vehicle': fits_vehicle})
    # What to do on error:

    return render(request, 'buyside/search.html', context)


def homepage(request):
    return render(request, 'buyside/homepage.html')


def treelist(request):
    return render(request, 'buyside/treelist.html')

def vehicle_upload(request, vehicle_id):
    all_vehicle_parts = PartList(vehicle_id)
    context = {'all_vehicle_parts': all_vehicle_parts}
    return render(request, 'buyside/vehicleupload.html', context)

def upload_complete(request):
    return render(request, 'buyside/uploadcomplete.html')


def vehicle_confirm(request):
    reg = request.POST['registration']
    reg = reg.upper()
    reg = reg.replace(" ", "")
    if reg:
        #car_details = VehicleDetailForm(request.POST)

        car_details = {}
        if reg == "RE52TGO":
            car_details = VehicleDetailForm({
                'make': 'VW',
                'model': "Golf",
                'year': "2002"
            })
            #car_details.make = "VW"
            #car_details.model = "Golf"
            #car_details.year = "2002"
            #car_details.transmission = "Manual"
            #car_details.fuel = "diesel"
            #car_details.engine = "1.9 Ltr"
            #car_details.bodytype = "5 door"
            vehicle_id = 'GOL00001'
        elif reg == "Y276NLU":
            car_details = VehicleDetailForm({
                'make': 'Suzuki',
                'model': 'SV650s',
                'year': '2000',
                'fuel': '1'
            })
            #car_details.make = "Suzuki"
            #car_details.model = "SV650s"
            #car_details.year = "200"
            #car_details.transmission = "Manual"
            #car_details.fuel = "Petrol"
            #car_details.engine = "650cc"
            #car_details.bodytype = "Motorbike - Bikini faired"
            vehicle_id = 'SVS00001'

        return render(request, 'buyside/vehicle_confirm.html', {
            'car_details': car_details,
            'vehicle_id': vehicle_id
        })
    else:
        return render(request, 'buyside/search.html')