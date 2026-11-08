# GST Mitra + ERPNext unified platform

This repository is being extended as a GST Mitra Frappe app installed alongside ERPNext. ERPNext remains the source of truth for accounting, selling, buying, stock, manufacturing and projects; GST Mitra adds the branded public landing page and future India-focused workflows without forking ERPNext core.

## Architecture

- Frappe Framework: Python application framework, website routes, permissions and APIs.
- ERPNext: accounting, general ledger, receivables/payables, sales and purchase orders, stock/warehouses, BOM/work orders, and project/tasks/timesheets.
- GST Mitra app: custom website, branding, integrations and GST-specific extensions.
- Persistence: MariaDB.
- Background jobs/cache/realtime: Redis and Frappe workers.
- Runtime: Docker Compose using the official Frappe Docker project.
- Public route: `/vyapar-pc`.

## Recommended deployment foundation

Use the maintained official Docker setup rather than a hand-built imitation of the Frappe stack:

- https://github.com/frappe/frappe_docker
- https://frappe.github.io/frappe_docker/
- https://docs.frappe.io/framework/user/en/installation
- https://docs.erpnext.com/

The disposable `pwd.yml` setup is for evaluation only. For ongoing development use the documented devcontainer/development workflow. For production use the documented production compose configuration and HTTPS proxy overrides. Do not expose MariaDB or Redis publicly.

## Install the custom app on a Frappe bench

After the app is included in your bench (for example, by cloning this repository's app source into `apps/gst_mitra` and installing it with Bench), run:

```bash
bench --site <your-site> install-app erpnext
bench --site <your-site> install-app gst_mitra
bench --site <your-site> migrate
bench build --app gst_mitra
```

If ERPNext is already installed on the site, do not install it again. Always back up the site before migrations or upgrades.

## Local development outline

1. Install Docker Desktop / Docker Engine and Docker Compose v2.
2. Follow the official Frappe Docker development setup.
3. Configure a site and install ERPNext.
4. Add this app to the bench and install it on the site.
5. Open `/vyapar-pc` to review the public landing page.

The production stack requires persistent volumes, strong unique secrets, restricted database/cache networking, HTTPS, backups, restore drills, and a supported Frappe/ERPNext version pair.

## ERP capability mapping

| Business requirement | ERPNext capability |
|---|---|
| General ledger, cash flow, financial statements | Accounting |
| Sales orders, invoices, receivables | Selling + Accounts |
| Suppliers, purchase orders, payables | Buying + Accounts |
| Stock, warehouses, reorder levels | Stock |
| BOM, work orders, material consumption | Manufacturing |
| Projects, tasks, time logs | Projects |
| GST localization and statutory workflows | Verify compatible India compliance app and current statutory requirements before production use |

## Landing page

The public marketing page is served at `/vyapar-pc` from `gst_mitra/www/vyapar-pc.html`. It uses the white/red/blue design requested and links all download calls to Vyapar's official PC product page. Product metrics and plan details should be rechecked against the official page before each campaign launch.

## Current build boundary

This foundation does not claim that the full ERP is deployed, connected to a live GST portal, or production-ready. Next implementation stages are custom company defaults and Indian chart-of-accounts setup, GST workflow validation, role matrix, inventory/manufacturing/project fixtures, automated tests, backup/restore validation, and a production deployment review.
