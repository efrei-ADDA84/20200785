resource "tls_private_key" "ssh_key"{
  algorithm = "RSA"
  rsa_bits = 4096
}

output "private_key"{
  value = tls_private_key.ssh_key.private_key_pem
  sensitive = true
}

output "public_key"{
  value = tls_private_key.ssh_key.public_key_openssh
  sensitive=true
}

resource "azurerm_network_interface" "example"{
  name                = "nic-20201085"
  location            = var.location
  resource_group_name = var.gpressources

  ip_configuration{
    name = "internal"
    subnet_id = "/subscriptions/765266c6-9a23-4638-af32-dd1e32613047/resourceGroups/ADDA84-CTP/providers/Microsoft.Network/virtualNetworks/network-tp4/subnets/internal"
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "vmdevops" {
  name = "devops-20201085"
  resource_group_name = var.gpressources
  location = var.location
  size = "Standard_D2s_v3"

  admin_username = "devops"

  admin_ssh_key{
    username   = "devops"
    public_key = tls_private_key.ssh_key.public_key_openssh
  }

  network_interface_ids=[azurerm_network_interface.example.id]

  os_disk {
    caching = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer = "UbuntuServer"
    sku = "18.04-LTS"
    version = "latest"
  }
}