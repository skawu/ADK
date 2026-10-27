# Technical Profile: Qt / QML

## Applicability

Select for projects using Qt Widgets, Qt Quick/QML, or mixed C++/QML applications. This Profile is guidance; the consuming project's Qt version, modules, compiler, platform, and architecture are authoritative.

## Inspect first

- Qt version and enabled modules; do not assume Qt 5 or Qt 6.
- Build system and presets, compiler, target OS, deployment packaging, and supported architectures.
- Existing C++/QML boundary, object ownership conventions, navigation/state model, and test setup.
- Threading model, event-loop assumptions, and any project-specific UI conventions.

## Review points

- Keep long-running I/O, blocking waits, and expensive computation off the UI thread.
- Respect QObject thread affinity. Do not access GUI objects from worker threads without a documented safe mechanism.
- Make ownership and lifetime of QObject instances, QML context properties, models, callbacks, and asynchronous results explicit.
- Check signal/slot connection lifetime, duplicate connections, re-entrancy, queued delivery, and cross-thread semantics.
- Prefer explicit properties, models, and stable interfaces over hidden global state or fragile context coupling.
- Ensure asynchronous completion handles cancellation, object destruction, stale results, and error reporting.
- Check QML bindings for accidental binding loops, unintended imperative overwrites, excessive recomputation, and avoidable object churn.
- Keep presentation, domain behavior, and device/service access separated according to the project's existing architecture.
- Consider accessibility, keyboard behavior, high-DPI scaling, localization, and resize behavior when relevant to the task.
- Use the project's supported Qt Test, QML tests, UI automation, and target runtime checks where available.

## Version-sensitive areas

Do not assume a class, module, QML type, CMake function, or API exists in every Qt release. Verify availability against the configured Qt version and project dependencies. Do not change Qt major/minor versions as an incidental part of a feature fix.

## Delivery evidence

Report the Qt version and build configuration used, relevant tests executed, and whether the change was verified only by static review, host build, UI test, or target deployment.
