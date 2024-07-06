# pynetplan

This package provides a class ``NetplanGenerator`` to help create Netplan configuration files. For example, to generate a ``netplan`` file that sets an IP address and a gateway for the ``enp0s3`` interface use this code:

```
n=NetplanGenerator()
n.set_simple_data("enp0s3", "192.168.1.10/24", "192.168.1.1")
```

Which generates this:

```
network:
  ethernets:
    enp0s3:
      addresses: 192.168.1.10/24
      routes:
      - to: default
        via: 192.168.1.1
  version: 2
```