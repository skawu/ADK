# Technical Profile: Mixed / Multi-Component Systems

## Applicability

Select when a project combines multiple processes, services, languages, device firmware, desktop applications, or deployment targets.

## Inspect first

- Component inventory, owners, deployment boundaries, data flows, and source-of-truth documents.
- IPC/network protocols, schemas, versioning, retries, timeouts, authentication, and error semantics.
- Build and release dependencies, supported version combinations, and target environment constraints.
- Which tests validate a component alone versus the complete system.

## Review points

- Treat component interfaces as contracts; verify both producers and consumers when a contract changes.
- Check compatibility between independently deployed versions.
- Check startup ordering, readiness, retries, backpressure, resource limits, and shutdown.
- Avoid assuming local success implies integration success.
- Record the exact component versions and configuration used in an integration test.
- Preserve the distinction between simulator, host, staging, bench, and production evidence.
- Ensure failures have a clear owner and actionable diagnostics without exposing secrets.

## Delivery evidence

For cross-component changes, identify the affected components, interface changes, compatibility assumptions, integration tests, and any component or environment that was not available for validation.
