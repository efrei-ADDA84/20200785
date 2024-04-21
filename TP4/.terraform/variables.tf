variable "location" {
    description = "Emplacement des ressources"
    type = string
    default="france central"
}


variable "gpressources" {
  description = "nom du groupe de ressources"
  type = string
  default = "ADDA84-CTP"
}


variable "vnetwork" {
  description = "nom du réseau"
  type = string
  default = "network-tp4"
}