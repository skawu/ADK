# Technical Profile: Embedded / MCU / Firmware

## Applicability

Select for bare-metal firmware, RTOS-based MCU projects, embedded Linux device integration, or mixed host/firmware systems. The exact MCU, board revision, SDK, RTOS, toolchain, memory map, and hardware safety process must come from project evidence.

## Inspect first

- MCU/SoC, board revision, clocking, memory map, boot chain, SDK/HAL version, compiler, linker script, and flash layout.
- RTOS/task priorities, interrupt priorities, ISR rules, DMA/cache behavior, watchdog, reset causes, and low-power states.
- Communication protocols, message schemas, timing limits, fault states, and backward compatibility.
- Available host tests, hardware-in-the-loop rig, debugger, serial logs, and safe bench procedure.

## Review points

- Keep interrupt handlers bounded and non-blocking; defer lengthy work to an appropriate task or main-loop context.
- Check shared state between ISR and tasks, atomicity, memory barriers, critical sections, and interrupt masking duration.
- Check buffer bounds, stack use, static allocation, heap fragmentation, alignment, integer width, and overflow.
- Validate DMA buffer ownership, cache coherency, alignment, and completion/error handling when relevant.
- Treat watchdog behavior, reset recovery, brownout, communication timeout, and fail-safe outputs as explicit state transitions.
- For CAN/UART/SPI/I2C and custom protocols, verify framing, length, byte order, timeout, retries, sequence handling, and malformed input behavior.
- Avoid unbounded waits and blocking operations in time-critical paths.
- Check firmware update, bootloader, persistent configuration, and rollback compatibility.
- Do not assume a host test proves timing, electrical behavior, or hardware correctness.

## Hardware operation boundary

Compilation and static analysis may be performed within normal project permissions. Flash erase, firmware flashing, fuse/option-byte changes, bootloader changes, calibration, or operation on connected production equipment require explicit authorization and the project's safe procedure.

## Verification levels

Report separately: host unit tests, cross-compilation/link, static analysis, simulator tests, bench tests, hardware-in-the-loop tests, and field/production validation. Never promote one level's result to another.
