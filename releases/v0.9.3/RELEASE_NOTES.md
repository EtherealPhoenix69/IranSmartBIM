# Release notes — v0.9.3

## Main fixes

### Estimation and statements use one calculation basis
- Statement line calculations now share the estimate calculation engine.
- Waste, transport, other direct costs and project coefficients are carried into statement amounts.
- Fixed direct costs are allocated pro-rata by executed quantity.
- At 100% completion, cumulative statement values reconcile to the estimate total.

### Current-period quantity and archive integrity
- Current-period executed quantity is entered separately from contract quantity.
- Previous, current and cumulative quantities are distinct.
- Cumulative execution cannot exceed the takeoff quantity.
- Statement rows retain snapshots of code, description, chapter, unit and cost assumptions.
- Deleting a takeoff item no longer erases historic statement rows.
- Older statements cannot be regenerated after later sequential statements exist.

### Database compatibility
- Restored full project contract fields and payment register.
- Migrates legacy payment date column `pay_date` to `payment_date` without dropping payment data.
- Preserves multi-project scoping for coefficients, statements and payments.

### Takeoff and pricebook
- Individual takeoff row editing/deletion is database-ID based.
- Amounts recalculate when quantity, unit price and cost inputs change.
- Editing is blocked when it would reduce the takeoff quantity below previously certified execution.
- Pricebook pagination supports the complete 1404 Abniyeh dataset.
- Rows without a valid unit price cannot be added accidentally.

### Windows packaging
- Added package-safe `launcher.py` entry point.
- PyInstaller spec resolves resources via `SPECPATH`.
- Build script checks exit status and actual EXE existence before reporting success.
- Bundles the supplied pricebook CSV and application icon.
- Uses a persistent user data location under Local AppData.
- GUI build runs windowed (no terminal window).

## Validation

- `python -m compileall -q src`: passed
- `python -m py_compile pyinstaller.spec`: passed
- `PYTHONPATH=src pytest -q`: **13 passed**
- Five-storey regression scenario: total estimate and total of 3 cumulative statements match exactly (0 Rial difference).

## Limitations
- The GUI was not launched in the Linux validation environment because PySide6 was unavailable there.
- A native Windows EXE build was not executed locally; use the included Windows PowerShell build script or GitHub Actions workflow.
- Legal/contractual percentages and indices must be supplied from the specific contract and valid circulars. No default sample value should be treated as legal advice.
