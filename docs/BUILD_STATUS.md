# GST Mitra ERP build status

## Development branch

`unified-platform-foundation`

## Implemented in this phase

- Created a separate development branch from repository `main`.
- Added initial installable Frappe app metadata and package files.
- Added deployment architecture and installation notes for ERPNext and Docker.
- Removed the unrelated landing-page files and their asset registration; this branch is scoped to GST Mitra only.

## Existing ERP foundation

The repository README on `main` identifies its code as GST Mitra V3.4. The previously discussed V4.0 release-candidate ZIP was not available in the current project library at build time. Do not overwrite `main` or claim this branch is based on V4.0 until that artifact is supplied or the exact V4.0 commit is identified.

## Not yet implemented or verified

- Frappe/ERPNext runtime installation and site migration.
- Automated tests against a running supported Frappe/ERPNext version pair.
- India GST localization and live statutory workflow validation.
- Custom GST Mitra DocTypes and workflows beyond native ERPNext modules.
- Production Docker image build and deployment.
- HTTPS, backup/restore and security validation on the target server.

## Next engineering sequence

1. Confirm target Frappe/ERPNext major-version pair and build the Docker development environment.
2. Run app install, migration and smoke tests in Docker.
3. Configure company, Indian chart of accounts, taxes, GSTIN and fiscal year.
4. Validate sales, purchase, stock, manufacturing, projects and timesheets.
5. Add custom India GST workflows only where native ERPNext/localization is insufficient.
6. Add automated regression, permission, audit and backup/restore tests.
7. Deploy to private staging with HTTPS; only then plan production.
