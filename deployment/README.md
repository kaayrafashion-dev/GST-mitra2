# GST Mitra — ERPNext deployment foundation

This repository is being extended as a GST Mitra Frappe app installed alongside ERPNext. ERPNext remains the source of truth for accounting, selling, buying, stock, manufacturing and projects; GST Mitra adds India-focused workflows and integrations without forking ERPNext core.

## Architecture

- Frappe Framework: Python application framework, website routes, permissions and APIs.
- ERPNext: accounting, general ledger, receivables/payables, sales and purchase orders, stock/warehouses, BOM/work orders, and project/tasks/timesheets.
- GST Mitra app: branding, integrations and GST-specific extensions.
- Persistence: MariaDB.
- Background jobs/cache/realtime: Redis and Frappe workers.
- Runtime: Docker Compose using the official Frappe Docker project.

## Recommended deployment foundation

Use the maintained official Docker setup:

- https://github.com/frappe/frappe_docker
- https://frappe.github.io/frappe_docker/
- https://docs.frappe.io/framework/user/en/installation
- https://docs.erpnext.com/

The disposable evaluation setup is for testing only. For ongoing development use the documented development workflow. For production use the documented production compose configuration and HTTPS proxy overrides. Do not expose MariaDB or Redis publicly.

## Install the custom app on a Frappe bench

After adding this app to your bench, run:

```bash
bench --site <your-site> install-app erpnext
bench --site <your-site> install-app gst_mitra
bench --site <your-site> migrate
bench build --app gst_mitra
```

If ERPNext is already installed, do not install it again. Back up the site before migrations or upgrades.

## Local development outline

1. Install Docker Engine/Desktop and Docker Compose v2.
2. Follow the official Frappe Docker development setup.
3. Configure a site and install ERPNext.
4. Add this app to the bench and install it on the site.
5. Configure GST Mitra defaults and validate the workflows below.

## ERP capability mapping

| Business requirement | ERPNext capability |
|---|---|
| General ledger, cash flow, financial statements | Accounting |
| Sales orders, invoices, receivables | Selling + Accounts |
| Suppliers, purchase orders, payables | Buying + Accounts |
| Stock, warehouses, reorder levels | Stock |
| BOM, work orders, material consumption | Manufacturing |
| Projects, tasks, time logs | Projects |
| GST localization and statutory workflows | Validate compatible India localization and current statutory requirements before production |

## Current build boundary

This foundation does not claim that the full ERP is deployed, connected to a live GST portal, or production-ready. Next stages are target-version selection, Docker-based app installation, company and Indian chart-of-accounts setup, GST workflow validation, role matrix, inventory/manufacturing/project fixtures, automated tests, backup/restore validation, and production deployment review.
