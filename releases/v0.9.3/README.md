# IranSmartBIM Office Professional v0.9.3

Persian desktop-oriented quantity surveying, cost estimation and contractor office workflow application.

## Download

The complete source package is stored in this directory:

- `IranSmartBIM_Office_Professional_v0.9.3.zip`

The archive includes the PySide6 application, SQLite database layer and migrations, Iran 1404 Abniyeh pricebook import data, Excel/PDF reporting, tests, Windows launch/build scripts, and GitHub Actions workflows.

## Verified in the development environment

- Python compile check: passed
- PyInstaller spec syntax check: passed
- Test suite: **13 passed**
- Five-storey regression scenario: estimate and cumulative statements reconcile; difference = **0 Rial**
- Legacy payment date migration (`pay_date` -> `payment_date`): covered by tests
- Deleting a takeoff row preserves archived statement snapshots: covered by tests

## Important verification limits

The development environment used for this release was Linux and did not have PySide6 or PowerShell. Therefore a real desktop GUI launch and a native Windows EXE build were **not** locally executed. The repository workflows are included to run tests and create a Windows build on GitHub Actions.

Pricebook records are imported from the user's supplied Iran 1404 Abniyeh workbook. The application does not claim that the sample unit prices or contract deduction percentages are current legal values; contract-specific values must be checked against the governing documents.
