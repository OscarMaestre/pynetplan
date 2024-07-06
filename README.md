# pynetplan

This package provides a class ``NetplanGenerator`` to help create Netplan configuration files. 

```
n=NetplanGenerator()
n.set_renderer(NetplanGenerator.NETWORK_MANAGER)
n.add_wired_ethernet(CARD_NAME)
n.set_dhcp_by_card_name(CARD_NAME, 4, False)
n.set_single_ip_address_by_card_name(CARD_NAME, "192.168.1.10/24")



```