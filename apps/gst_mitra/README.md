# GST Mitra — Frappe application

GST Mitra is the custom Indian-business layer for the unified ERP platform. ERPNext remains the source of truth for accounting, stock, selling, buying, manufacturing, projects, and HR workflows; this app adds GST-focused workflows and the public Vyapar PC information page.

## Compatibility

- Target: Frappe / ERPNext v15 initially. Pin compatible image tags before production.
- Python package: `gst_mitra`
- Website route: `/vyapar-pc`

## Install in a bench

```bash
bench get-app https://github.com/kaayrafashion-dev/GST-mitra2 --branch unified-erp-vyapar-foundation --resolve-deps
bench --site your-site.example install-app gst_mitra
bench build --app gst_mitra
bench --site your-site.example clear-cache
```

## Notes

Do not modify ERPNext core. Extend it through custom DocTypes, hooks, reports, workspaces and APIs. Before production, pin exact Frappe/ERPNext patch versions, run migrations on a restored staging backup, and complete the security checklist in `/docs/SECURITY.md`.
