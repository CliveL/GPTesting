__author__ = 'Clive'
from django.core.urlresolvers import reverse
from buyside.models import Vehicle, VehiclePart
from django.template.defaultfilters import slugify


def BaseTree(vehicle_id):
    target_vehicle = Vehicle.objects.get(pk=vehicle_id)
    vehicle_parts = VehiclePart.objects.filter(vehicles=vehicle_id)
    parts = ListNode('', target_vehicle.long_name, vehicle_id, 0)
    for vehicle_part in vehicle_parts:
        # url, name, category list
        #if vehicle_part.tree_level_5 == '':
        #    print 'I am here'
        parts.add_node(
            vehicle_part.gecko_part_number,
            vehicle_part.name,
            [
                vehicle_part.tree_level_1,
                vehicle_part.tree_level_2,
                vehicle_part.tree_level_3,
                vehicle_part.tree_level_4,
                vehicle_part.tree_level_5
            ])
    return parts

def PartTree(vehicle_id, type_id):
    parts = BaseTree(vehicle_id)
    all_vehicle_parts = parts.build_html_tree(vehicle_id, type_id)
    return all_vehicle_parts

def PartList(vehicle_id):
    parts = BaseTree(vehicle_id)
    parts_list = parts.build_node_list(vehicle_id, parts.name)
    return parts_list

class ListNode:
    def __init__(self, url_input, name_input, database_id, level):
        self.part_number = url_input  # String to contains the URL identifier to create the link for the node
        self.name = name_input  # name to be displayed on the webpage
        self.child_nodes = []  # list to contain all the child nodes
        self.level = level
        self.database_id = database_id

    def add_node(self, node_url, node_name, category):
        # if current level category doesn't exist, add new node here
        node_exists = False
        # find current category in child node list if it is there
        for node in self.child_nodes:
            if node.database_id == category[self.level]:
                node_exists = True
                #if this is not final level go to current child node and run again.
                if category[self.level + 1] != '':
                    node.add_node(node_url, node_name, category)
                # if this is the final level check it is blank and add data
                else:
                    self.part_number = node_url
                    self.name = node_name
                break

        # if it does not exist, add node at this level
        if node_exists is False:
            # if this is not the final level, create blank node
            if category[self.level + 1] != '':
                new_node = ListNode('', category[self.level], category[self.level], self.level + 1)
                new_node.add_node(node_url, node_name, category)
            #if this is the final level, create node with data
            else:
                new_node = ListNode(node_url, node_name, category[self.level], self.level + 1)
            # add node to list
            self.child_nodes.append(new_node)


    def build_node_list(self, vehicle_id, parent_title):
        count = 0
        padding = ""
        while (count < self.level):
            padding = padding + "--"
            count += 1
        padding = padding + ">"

        form_data = []
        id_string = parent_title + "." + self.name
        id_string = id_string.replace(" ", "_")

        form_data[0] = parent_title.replace(" ", "_")
        form_data[1] = self.name.replace(" ", "_")
        form_data[2] = padding + self.name
        id_list = []
        id_list.append(form_data)
        if self.child_nodes.__len__() != 0:
            for node in self.child_nodes:
                #child_list = node.build_node_list(vehicle_id, self.name)
                id_list = id_list + node.build_node_list(vehicle_id, self.name)
        return id_list


    def build_html_tree(self, vehicle_id, html_type):
        # returns prepared HTML for current node, and list of prepared HTML for child nodes
        #requires cleanup around url builder (DRY)
        if html_type == 'shop':
            if self.part_number != '':
                url = reverse('buyside:search2', kwargs={'search_id_1': vehicle_id, 'search_id_2': self.part_number})
            else:
                url = reverse('buyside:search', kwargs={'search_id_1': vehicle_id})

            list_string = r'<a href="%s">%s</a> +' % (url, self.name)

        elif html_type == 'name':
            if self.name != '':
                list_string = self.name
            else:
                list_string = 'Un-named part'

        elif html_type == 'upload':
            if self.part_number != '':
                list_string = r'<label for="id_%s">%s</label><input id="id_%s" type="text" name="/>' \
                      % (self.part_number, self.name, self.part_number)
            else:
                list_string = 'no part number'


        if self.child_nodes.__len__() != 0:
            children = []
            for node in self.child_nodes:
                child_title, grandchildren = node.build_html_tree(vehicle_id, html_type)
                children.append(child_title)
                if grandchildren is not None:
                    children.append(grandchildren)
        else:
            children = None

        return list_string, children