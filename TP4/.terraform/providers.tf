terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 2.0"
    }
  }
}

provider "azurerm" {
  subscription_id = "765266c6-9a23-4638-af32-dd1e32613047"
  skip_provider_registration = true
  features {}
}