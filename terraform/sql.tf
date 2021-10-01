module "sql-db_postgresql" {
  source  = "GoogleCloudPlatform/sql-db/google//modules/postgresql"
  version = "6.0.0"

  name                 = var.cloud_sql_name
  database_version     = "POSTGRES_13"
  tier                 = "db-custom-1-3840"
  random_instance_name = true
  deletion_protection  = false

  project_id = var.google_project
  region     = var.region
  zone       = var.zone

  db_name       = "testable-dagster"
  user_name     = "testable-dagster-user"
  user_password = var.cloud_sql_password
  ip_configuration = {
    ipv4_enabled        = false
    private_network     = google_compute_network.testable_dagster.self_link
    require_ssl         = true
    authorized_networks = []
  }

  module_depends_on = [module.sql-db_private_service_access.peering_completed]

  depends_on = [google_compute_network.testable_dagster]
}

module "sql-db_private_service_access" {
  source      = "GoogleCloudPlatform/sql-db/google//modules/private_service_access"
  version     = "6.0.0"
  project_id  = var.google_project
  vpc_network = google_compute_network.testable_dagster.name

  depends_on = [google_compute_network.testable_dagster]
}
