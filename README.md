# IranSmartBIM

> Modular BIM and construction office platform focused on Iranian workflows.

IranSmartBIM is an open, modular platform for building design, quantity takeoff, cost estimation, project controls and construction-office workflows.

## Available application packages

### Office Professional v0.9.3

A Persian desktop application for quantity surveying and contractor-office workflows is available in [releases/v0.9.3](releases/v0.9.3/).

It includes:
- Multi-project and contract management
- Iran 1404 Abniyeh pricebook import/search
- Quantity takeoff and cost estimation
- Contract coefficients, waste, transport and direct costs
- Interim statement periods and archived statement snapshots
- Project payment register
- Excel/PDF reports
- Windows build scripts and CI workflows

See [the v0.9.3 release notes](releases/v0.9.3/RELEASE_NOTES.md) and [release package README](releases/v0.9.3/README.md).

**Validation:** 13 automated tests passed; the five-storey regression scenario reconciles estimate and cumulative statements with zero Rial difference. GUI launch and native Windows EXE generation still need validation on Windows.

## Existing modular platform skeleton

The repository's original modular architecture remains under `src/`, with tests and project documentation alongside it. The Office Professional desktop package is published separately under `releases/` to avoid silently replacing unrelated modules.

## License

MIT License
