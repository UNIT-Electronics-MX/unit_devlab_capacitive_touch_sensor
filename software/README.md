# Getting Started

## Quick Setup

### 1. Hardware Connections

- **VCC** → 3.3V or 5V supply
- **GND** → Ground  
- **OUT** → Digital input pin on your microcontroller

Compatible with a JST 1 mm pitch QWIIC connector for easy I2C integration (power only, D0 must be connected separately).


### 2. Basic Operation

The sensor provides a simple digital output:
- **HIGH** = Touch detected
- **LOW** = No touch

### 3. Mode Selection

Use the onboard jumper to select operation mode:
- **Momentary**: Output HIGH only while touched
- **Toggle**: Output toggles state with each touch


#### Mode & Level Selection

| Mode | Level | TOG | AHLB | Pad Q (CMOS)         | Pad OPDO (Open Drain)    | Behavior                        |
|------|-------|-----|------|----------------------|--------------------------|----------------------------------|
| 0    | 0     | 0   | 0    | Active high          | Open drain, active high  | Momentary, single pulse          |
| 0    | 1     | 0   | 1    | Active low           | Open drain, active low   | Momentary, inverted pulse        |
| 1    | 0     | 1   | 0    | Toggle, power-on=0   | Toggle, active high      | Toggle, touch to change state    |
| 1    | 1     | 1   | 1    | Toggle, power-on=1   | Toggle, active low       | Toggle, inverted                 |

*Mode and level solder jumpers set output type and behavior (momentary/toggle, active high/low).*

### 4. Sensitivity Adjustment

Adjust the onboard potentiometer:
- **Clockwise**: Increase sensitivity
- **Counter-clockwise**: Decrease sensitivity

## Next Steps

1. Test with a simple digital read
2. Implement in your project
3. Fine-tune sensitivity as needed