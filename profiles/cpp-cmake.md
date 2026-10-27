# Technical Profile: C++ / CMake

## Applicability

Select for C++ projects and projects using CMake. The project's language standard, compiler, ABI, dependency policy, and supported platforms are authoritative.

## Inspect first

- C++ standard and compiler/toolchain versions.
- Top-level CMake configuration, presets/toolchain files, targets, options, and generated build directory conventions.
- Ownership model, error-handling policy, threading primitives, dependency management, and test framework.
- Cross-compilation and platform-specific constraints, if any.

## Review points

- Prefer RAII and explicit ownership; assess lifetime, move/copy behavior, and resource cleanup.
- Check bounds, integer conversions, nullability, iterator/reference invalidation, and object lifetime.
- Make error paths and exception-safety behavior consistent with the project.
- Inspect thread safety, lock ordering, deadlock potential, data races, and shutdown behavior.
- Avoid unnecessary raw owning pointers, global mutable state, hidden lifetime coupling, and unbounded resource use.
- Keep interfaces cohesive and dependencies explicit. Avoid broad refactors when a local change is sufficient.
- Respect the existing CMake target model and dependency declarations. Do not add global flags or weaken warnings to hide a defect.
- Verify generated code and platform-specific code paths where applicable.
- Use available unit tests, static analysis, sanitizers, and compiler warnings as appropriate to the project and environment.

## Compatibility

Do not impose C++17, C++20, a compiler, or a specific library merely because it is common. Confirm support in the project before using language or library features. For ABI-sensitive libraries, plugins, and public headers, consider binary and source compatibility.

## Delivery evidence

Record the actual configure/build/test commands and target configuration. Distinguish host-native results from cross-compiled or target-device validation.
