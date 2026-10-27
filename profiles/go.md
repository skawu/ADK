# Technical Profile: Go

## Applicability

Select for Go applications, services, tools, and libraries. The module's Go version, supported operating systems, dependency policy, and deployment model are authoritative.

## Inspect first

- go.mod, toolchain version, package layout, build tags, generated code, and CI commands.
- Service lifecycle, context propagation, concurrency ownership, interfaces, and error conventions.
- External dependencies, network access, configuration, secrets, and shutdown behavior.

## Review points

- Propagate context cancellation and deadlines across request-scoped work.
- Define who owns each goroutine and how it exits; avoid goroutine leaks and abandoned background work.
- Check channel ownership, closure, blocking behavior, backpressure, and select cancellation paths.
- Handle errors explicitly and preserve useful context without leaking secrets.
- Avoid data races and unsynchronized shared state. Use go test -race where supported and relevant.
- Ensure graceful shutdown stops accepting work, cancels workers, and waits within a defined bound.
- Respect API compatibility and serialization contracts.
- Use the project's existing formatting, linting, test, and build conventions. Do not assume a tool is installed because it is common.

## Verification

Use the Go version and commands established by the repository. Record whether race detection, integration tests, cross-platform builds, and real service checks were actually run.
