__author__ = 'Clive'
from django.core.urlresolvers import reverse

class ListNode:
    def __init__(self, url_input, name_input, database_id, level):
        self.url = url_input  # String to contains the URL identifier to create the link for the node
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
                    self.url = node_url
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

    def build_html(self, vehicle_id):
        # returns prepared HTML for current node, and list of prepared HTML for child nodes
        #requires cleanup around url builder (DRY)
        if self.url != '':
            url = reverse('buyside:search2', kwargs={'search_id_1':vehicle_id, 'search_id_2':self.url})
            html = r'<a href="%s">%s</a> +' % (url, self.name)
        else:
            url = reverse('buyside:search', kwargs={'search_id_1':vehicle_id})
            html = r'<a href="%s">%s</a> +' % (url, self.name)


        if self.child_nodes.__len__() != 0:
            children = []
            for node in self.child_nodes:
                child_title, grandchildren = node.build_html(vehicle_id)
                children.append(child_title)
                if grandchildren is not None:
                    children.append(grandchildren)
        #elif self.child_nodes.__len__() == 0:
        else:
            children = None

        return html, children