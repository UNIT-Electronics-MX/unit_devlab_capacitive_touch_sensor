---
title: "Touch Capacitive Sensor"
version: "1.0"
modified: "2025-04-30"
output: "touch_capacitive_sensor"
subtitle: "Easy-to-use breakout module based on the TTP223B capacitive touch IC"
---

<!--
# README_TEMPLATE.md
This file serves as an input to generate a datasheet-style technical PDF.
Fill in each section without deleting or modifying the existing headings.
-->

# Touch Capacitive Sensor

![alt text](../../hardware/resources/unit_top_V_0_0_1_ue0099_Sensor_Touch.png) <!-- FILL HERE: replace image if needed -->

## Introduction

<!-- FILL HERE -->
The UNIT Touch Capacitive Sensor transforms a simple touch into a precise digital signal—no buttons, no moving parts. Powered by the TTP223B capacitive sensing chip, this board continuously monitors its flat electrode pad and instantly reports “touch detected” via a clean HIGH logic output. Whether you’re building a sleek control panel, a wearable interface, or a touch-activated lamp, this sensor delivers reliable, debounce-free touch detection with minimal wiring and virtually zero power draw at rest.

## Functional Description

<!-- FILL HERE -->
1. **Capacitive Sensing**: The TTP223B IC measures changes in capacitance on the large silver touch pad.  
2. **Signal Processing**: Internal auto-calibration and filtering remove noise and drift.  
3. **Digital Output**: When the measured capacitance exceeds the threshold, the OUT pin goes HIGH; otherwise, it remains LOW.  
4. **Mode Selection**: A small solder jumper lets you choose between:  
   - **Momentary mode (L)**: OUT is HIGH only while the pad is being touched.  
   - **Toggle mode (T)**: OUT toggles state on each touch (like a latching switch).

## Electrical Characteristics & Signal Overview

<!-- FILL HERE -->
- **Wide supply range**: 2.0 V to 5.5 V, compatible with 3.3 V and 5 V systems.  
- **Low power**: < 1 μA in standby mode.

## Applications

<!-- FILL HERE -->
- User interfaces for wearables and handheld devices

- Touch-activated lamps, buzzers or relays

- Capacitive keyboards and remote controls

- Home automation touch panels

- Interactive art installations

## Features

<!-- FILL HERE -->
- **Touch-only sensing**: No physical press required – reacts to proximity of a finger.    
- **Fast response**: < 80 ms touch detection time.  
- **Auto-calibration**: Compensates for environmental changes and drift.  
- **Selectable modes**: Momentary or toggle output (via solder-jumper on the board).  
- **On-board pull-up/down**: Ensures clean digital output.  
- **Mounting holes**: Two M3 screw holes for easy panel integration.  
- **JST PH-2.0 connector**: Quick-disconnect cable interface.

## Pin & Connector Layout

| Group     | Available Pins | Suggested Use                          |
|-----------|----------------|----------------------------------------|
| GPIO      | <!-- FILL -->  | <!-- FILL -->                          |
| UART      | <!-- FILL -->  | <!-- FILL -->                          |
| TouchPad  | <!-- FILL -->  | <!-- FILL -->                          |
| Analog    | <!-- FILL -->  | <!-- FILL -->                          |
| SPI       | <!-- FILL -->  | <!-- FILL -->                          |

## Settings

### Interface Overview

| Interface  | Signals / Pins         | Typical Use                              |
|------------|------------------------|------------------------------------------|
| UART       | <!-- FILL -->          | <!-- FILL -->                             |
| I2C        | <!-- FILL -->          | <!-- FILL -->                             |
| SPI        | <!-- FILL -->          | <!-- FILL -->                             |
| USB        | <!-- FILL -->          | <!-- FILL -->                             |

### Supports

| Symbol | I/O         | Description                        |
|--------|-------------|------------------------------------|
| VCC    | Input       | <!-- FILL -->                      |
| GND    | GND         | <!-- FILL -->                      |
| IO     | Bidirectional | <!-- FILL -->                   |

## Block Diagram

![Function Diagram](images/pinout.png) <!-- FILL HERE: replace image if needed -->

## Dimensions

![Dimensions](../../hardware/resources/unit_dimension_V_0_0_1_ue0099_Sensor_Touch.png) <!-- FILL HERE: replace image if needed -->

## Usage

<!-- FILL HERE -->
Mention supported development platforms and toolchains 

- (e.g., Arduino IDE, ESP-IDF, PlatformIO, etc.)

## Downloads

<!-- FILL HERE -->
- [Schematic PDF](docs/schematic.pdf)
- [Board Dimensions DXF](docs/dimensions.dxf)
- [Pinout Diagram PNG](docs/pinout.png)

## Purchase

<!-- FILL HERE -->
- [Buy from vendor](https://example.com)
- [Product page](https://example.com/product/template-board)
