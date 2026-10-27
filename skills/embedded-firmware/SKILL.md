---
name: embedded-firmware
description: Implement and review embedded Linux, RTOS, bare-metal, and MCU firmware changes with explicit hardware identity, timing, memory, protocol, and safe-operation boundaries.
---

# Embedded Firmware Development

## Purpose

Make embedded changes that account for real-time constraints, limited resources, hardware state, communication failure, and safe recovery.

## Use when

- Changing MCU firmware, RTOS tasks, interrupts, DMA, boot/startup, device drivers, or embedded Linux integration.
- Modifying CAN, UART, SPI, I2C, or custom device protocols.
- Changing watchdog, reset, firmware update, persistent configuration, or fault behavior.
- Preparing a change that needs host, cross-compile, simulator, bench, or hardware-in-the-loop evidence.

Use the Embedded/MCU Profile and the project's hardware-operation procedure.

## Inputs and prerequisites

Establish the exact MCU/SoC and board revision, SDK/HAL/RTOS, compiler/linker configuration, memory map, protocol contract, timing requirements, build/flash commands, test hardware, and authorization boundary.

## Procedure

1. Read project instructions, hardware safety procedures, target configuration, relevant driver/state-machine code, protocol definitions, and existing tests.
2. Separate host-side logic, cross-compiled firmware, simulator behavior, bench validation, and production/field behavior.
3. Keep interrupt handlers bounded and non-blocking. Check shared ISR/task state, critical sections, atomicity, and interrupt latency.
4. Check stack/heap use, buffer bounds, alignment, integer widths, overflow, DMA/cache coherency, and resource lifetime where applicable.
5. Model timeout, retry, malformed input, watchdog, reset, brownout, communication loss, and fail-safe behavior explicitly.
6. For device protocols, verify framing, lengths, byte order, sequence handling, timeouts, retries, and compatibility with existing peers.
7. Add host tests or simulation for deterministic logic where practical, then use the project's canonical cross-build and target validation path.
8. Do not flash, erase, change bootloader/fuses/option bytes, calibrate, or operate connected production equipment without explicit authorization and the approved safe procedure.
9. Record exact target/toolchain/artifact identity and the verification level actually reached.

## Outputs

A reviewable firmware change, relevant tests, target-aware evidence, and an explicit statement of unverified hardware behavior.

## Failure handling

If board identity, target toolchain, safety procedure, or operation authorization is unclear, do not perform irreversible hardware actions. Continue with safe analysis or host-side checks and report the exact missing prerequisite.

## Completion criteria

The change respects timing, memory, protocol, fault, and hardware safety boundaries; verification levels are reported separately; and no unverified target behavior is represented as proven.
