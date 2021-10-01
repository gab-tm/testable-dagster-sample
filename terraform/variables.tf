variable "google_project" {
  type        = string
  description = "Google Project ID"
}

variable "region" {
  type        = string
  description = "Region value to use for creating resources"
  default     = "us-central1"
}

variable "zone" {
  type        = string
  description = "Zone value to use for creating resources"
  default     = "us-central1-a"
}

variable "service_account_name" {
  type        = string
  description = "Service Account Name"
}

variable "gcp_service_list" {
  type        = list(string)
  description = "List of API services to enable"
}

variable "network_name" {
  type        = string
  description = "VPC Network Name"
}

variable "subnetwork_ip_cidr_range" {
  type        = string
  description = "Subnetwork IP CIDR range for VPC network"
  default     = "10.0.0.0/16"
}

variable "dagster_name" {
  type        = string
  description = "Dagster Instance Name"
}

variable "dagster_machine_type" {
  type        = string
  description = "Dagster Instance Machine Type"
  default     = "n1-standard-1"
}

variable "dagster_tags" {
  type        = list(string)
  description = "Dagster Instance Tags"
}

variable "cloud_sql_name" {
  type        = string
  description = "Cloud SQL Instance Name"
  default     = "dagster_postgres"
}

variable "cloud_sql_password" {
  type        = string
  description = "Cloud SQL Password"
}
