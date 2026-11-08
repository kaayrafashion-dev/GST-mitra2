# GST Mitra Frappe App

Custom Frappe application intended to run alongside ERPNext.

## Current scope

- Public Vyapar PC billing landing page at `/vyapar-pc`.
- Responsive white, red and blue design system.
- Official Vyapar download CTA.
- No fork of ERPNext core.

## Install

Add this app to a Frappe bench and run:

```bash
bench --site <site-name> install-app gst_mitra
bench --site <site-name> migrate
bench build --app gst_mitra
```

See [deployment README](../../deployment/README.md) for Docker guidance.
