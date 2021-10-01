resource "google_compute_instance" "testable_dagster" {
  name         = var.dagster_name
  machine_type = var.dagster_machine_type

  metadata = {
    "block-project-ssh-keys" = "TRUE",
    "enable-oslogin"         = "TRUE",
    "enable-oslogin-2fa"     = "TRUE",
  }

  zone                      = var.zone
  tags                      = var.dagster_tags
  allow_stopping_for_update = true

  boot_disk {
    initialize_params {
      image = "cos-cloud/cos-stable"
      size  = 100
    }
  }

  network_interface {
    network    = google_compute_network.testable_dagster.name
    subnetwork = google_compute_subnetwork.testable_dagster.name
  }

  service_account {
    # email  = module.waze_pipeline_service_account.email
    scopes = ["cloud-platform", "https://www.googleapis.com/auth/drive.readonly"]
  }
}
