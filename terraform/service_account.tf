module "testable_dagster_service_account" {
  source  = "terraform-google-modules/service-accounts/google"
  version = "4.0.2"

  project_id = var.google_project
  names      = [var.service_account_name]
  project_roles = [
    # "${var.google_project}=>roles/bigquery.dataEditor",
    # "${var.google_project}=>roles/bigquery.jobUser",
    # "${var.google_project}=>roles/bigquery.readSessionUser",
    # "${var.google_project}=>roles/secretmanager.secretAccessor",
    "${var.google_project}=>roles/storage.admin"

  ]
  display_name = "Testable Dagster Pipeline Service Account"
  description  = "Service account for the Testable Dagster Pipeline"
}
