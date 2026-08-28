# GST Mitra V3.4 — GST Workflow + GSTR-2B / ITC Workspace

V3.4 builds on the V3.3 red-team hardened baseline.

## Added
- GSTR-2B record import API with duplicate protection via SHA-256 source hash.
- Tenant-isolated GSTR-2B ledger by return period.
- Tax-total validation for imported records (IGST + CGST + SGST must reconcile to total tax within ₹0.01).
- Reconciliation engine matching GSTR-2B records to purchase records by GSTIN, period, taxable value and tax total.
- Match states: unmatched, matched, mismatch, blocked (blocked reserved for future workflow controls).
- ITC workspace summary: GSTR-2B tax, matched tax, book eligible ITC, blocked/reversed ITC and potential mismatch.
- Audit events for imports and reconciliation.
- Existing HTTPS/session, tenant isolation, billing, inventory, invoice PDF and print utilities retained.

## API
- `GET /api/gst/gstr2b?period=YYYY-MM`
- `POST /api/gst/gstr2b/import`
- `POST /api/gst/gstr2b/reconcile?period=YYYY-MM`
- `GET /api/gst/itc-workspace?period=YYYY-MM`

## Validation status
- Python compile: PASS
- Existing regression suite: 7/7 PASS
- V3.4 GSTR-2B endpoint smoke test: PASS

## Important
This is a GST compliance-preparation/reconciliation feature, not an assertion that GST portal data is fetched automatically. Production import should be connected to an authorized GST/GSP data source and its schema/authorization controls verified before live use.
