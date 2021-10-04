resource "google_compute_network" "testable_dagster" {
  name                    = var.network_name
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "testable_dagster" {
  name                     = "${google_compute_network.testable_dagster.name}-subnetwork"
  ip_cidr_range            = var.subnetwork_ip_cidr_range
  region                   = var.region
  private_ip_google_access = true
  network                  = google_compute_network.testable_dagster.name
}

resource "google_compute_firewall" "testable_dagster_iap" {
  name    = "testable-dagster-default-allow-iap"
  network = google_compute_network.testable_dagster.name

  allow {
    protocol = "tcp"
    ports    = ["22", "8080", "3000"]
  }

  source_ranges           = ["35.235.240.0/20"]
  target_service_accounts = [module.testable_dagster_service_account.email]
}

resource "google_compute_router" "testable_dagster" {
  name    = "${google_compute_network.testable_dagster.name}-router"
  region  = google_compute_subnetwork.testable_dagster.region
  network = google_compute_network.testable_dagster.id
}

resource "google_compute_router_nat" "testable_dagster" {
  name                               = "${google_compute_router.testable_dagster.name}-nat"
  router                             = google_compute_router.testable_dagster.name
  region                             = google_compute_router.testable_dagster.region
  nat_ip_allocate_option             = "AUTO_ONLY"
  source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"
}
