
# Touch Capacitive Sensor

## Introduction

<!-- FILL HERE -->
The UNIT Touch Capacitive Sensor transforms a simple touch into a precise digital signal—no buttons, no moving parts. Powered by the TTP223B capacitive sensing chip, this board continuously monitors its flat electrode pad and instantly reports “touch detected” via a clean HIGH logic output. Whether you’re building a sleek control panel, a wearable interface, or a touch-activated lamp, this sensor delivers reliable, debounce-free touch detection with minimal wiring and virtually zero power draw at rest.

<div align="center">
  <img src="hardware/resources/unit_top_V_0_0_1_ue0099_Sensor_Touch.png" width="500px" alt="Development Board">
  <p><em></em></p>
</div>


<div align="center">

### Quick Setup


[<img src="https://img.shields.io/badge/Product%20Wiki-blue?style=for-the-badge" alt="Product Wiki">](https://unit-electronics-mx.github.io/unit_touch_capacitive_sensor/mdbook/index.html)
[<img src="https://img.shields.io/badge/Datasheet-green?style=for-the-badge" alt="Datasheet">](https://unit-electronics-mx.github.io/unit_touch_capacitive_sensor/datasheet_professional.html)
[<img src="https://img.shields.io/badge/Buy%20Now-orange?style=for-the-badge" alt="Buy Now">](https://uelectronics.com/)
[<img src="https://img.shields.io/badge/Getting%20Started-purple?style=for-the-badge" alt="Getting Started">](https://unit-electronics-mx.github.io/unit_touch_capacitive_sensor/mdbook/software/getting-started.html)

</div>

## 📦 Overview

| Feature              | Description                                                                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Capacitive Sensing   | Utilizes the TTP223B IC to detect changes in capacitance on the large silver touch pad.                                                          |
| Signal Processing    | Internal auto-calibration and filtering circuitry remove noise and drift for reliable operation.                                                  |
| Digital Output       | OUT pin goes HIGH when touch is detected (capacitance exceeds threshold); remains LOW otherwise.                                                  |
| Mode Selection       | Solder jumper selects between Momentary mode (OUT is HIGH only while touched) and Toggle mode (OUT toggles state on each touch). |


## 🧪 Use Cases

- Touch-sensitive controls for user interfaces
- Proximity sensing for devices



## 📚 Resources

- [Schematic Diagram](https://github.com/UNIT-Electronics-MX/unit_touch_capacitive_sensor/blob/main/hardware/unit_sch_V_0_0_1_ue0099_Sensor_Touch.pdf)

- [Pinout Diagram](https://github.com/UNIT-Electronics-MX/unit_touch_capacitive_sensor/tree/main/hardware#-pinout)
- [Getting Started Guide](docs/getting_started.md)


  
## 📝 License

All hardware and documentation in this project are licensed under the **MIT License**.  
Please refer to [`LICENSE.md`](LICENSE.md) for full terms.



<div align="center">
  <sub>Template created by UNIT Electronics </sub>
</div>
