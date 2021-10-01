terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.70.0"
    }
  }
  backend "gcs" {
    bucket = "tm-dw-sandbox-testable-dagster-terraform"
    prefix = "state"
  }
}
