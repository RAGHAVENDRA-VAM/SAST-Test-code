provider "azurerm" {
  features {}
}

resource "azurerm_storage_account" "bad" {
  name                     = "badstorage12345"
  resource_group_name      = "rg-demo"
  location                 = "East US"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  allow_blob_public_access = true  # ❌ public
}

resource "azurerm_network_security_group" "bad_nsg" {
  name = "bad-nsg"

  security_rule {
    name                       = "AllowAll"
    access                     = "Allow"
    direction                  = "Inbound"
    priority                   = 100
    protocol                   = "*"
    source_address_prefix      = "*"
    destination_port_range     = "*"
  }
}