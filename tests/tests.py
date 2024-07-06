from pynetplan import NetplanGenerator

if __name__=="__main__":
    CARD_NAME="enp0s3"
    n=NetplanGenerator()
    
    n.set_renderer(NetplanGenerator.NETWORK_MANAGER)
    n.add_wired_ethernet(CARD_NAME)
    n.set_dhcp_by_card_name(CARD_NAME, 4, False)
    n.set_single_ip_address_by_card_name(CARD_NAME, "192.168.1.10/24")
    print(n)

    n=NetplanGenerator()
    
    n.set_renderer(NetplanGenerator.NETWORK_MANAGER)
    n.add_wired_ethernet(CARD_NAME)
    n.set_dhcp_by_card_name(CARD_NAME, 4, False)
    n.set_multiple_ip_address_by_card_name(CARD_NAME, ["192.168.1.10/24", "10.0.1.100/16"])
    n.add_default_route_by_card_name(CARD_NAME, "192.168.1.1")
    print(n)


    n=NetplanGenerator()
    n.set_simple_data("enp0s3", "192.168.1.10/24", "192.168.1.1")
    print(n)