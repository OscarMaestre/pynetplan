import yaml

NETWORKD        = "networkd"
NETWORK_MANAGER = "NetworkManager"
VERSION         = 2

class NetplanGenerator(object):
        
    def __init__(self):
        self.root_dictionary=dict()
        self.root_dictionary["network"]=dict()
        self.root_dictionary["network"]["version"]=VERSION
        self.ethernets=None
    def set_renderer(self, renderer):
        self.root_dictionary["network"]["renderer"]=renderer

    def get_addresses(address_list):
        d=dict()
        d["addresses"]=address_list
        return d

    def add_wired_ethernet(self, wired_ethernet_card_name):
        if self.ethernets==None:
            ethernets=dict()
            self.root_dictionary["network"]["ethernets"]=ethernets
        card=dict()
        self.root_dictionary["network"]["ethernets"][wired_ethernet_card_name]=card

    def set_dhcp_by_card_name(self, card_name, ip_version=4, dhcp_as_boolean=False):
        try:
            boolean_string= "true" if dhcp_as_boolean  else "false"
            dhcp_version="dhcp4" if ip_version==4 else "dhcp6"
            self.root_dictionary["network"]["ethernets"][card_name][dhcp_version]=boolean_string
        except Exception as e:
            print(e)

    def set_single_ip_address_by_card_name(self, card_name, single_ip_address):
        try:
            self.root_dictionary["network"]["ethernets"][card_name]["addresses"]=single_ip_address
        except Exception as e:
            print(e)

    def set_multiple_ip_address_by_card_name(self, card_name, list_of_addresses):
        try:
            self.root_dictionary["network"]["ethernets"][card_name]["addresses"]=list_of_addresses
        except Exception as e:
            print(e)

    def add_default_route_by_card_name(self, card_name, default_route):
        try:
            self.root_dictionary["network"]["ethernets"][card_name]["routes"]
        except Exception as e:
            self.root_dictionary["network"]["ethernets"][card_name]["routes"]=list()
            self.root_dictionary["network"]["ethernets"][card_name]["routes"].append({"to":"default", "via":default_route})

    def set_simple_data(self, card_name, ip_address, ip_gateway):
        self.add_wired_ethernet(card_name)
        self.set_single_ip_address_by_card_name(card_name, ip_address)
        self.add_default_route_by_card_name(card_name, ip_gateway)
    def __str__(self) -> str:

        return yaml.dump(self.root_dictionary, default_flow_style=False, allow_unicode=True)



