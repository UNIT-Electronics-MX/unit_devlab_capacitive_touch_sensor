# Hardware Overview

<div align="center">
    <a href="../resources/unit_sch_V_0_0_1_ue0099_Sensor_Touch.pdf">
        <img src="../resources/Schematics_icon.jpg?raw=false" width="450px"><br/> Schematics
    </a>
</div>

## 🔌 Pinout

<div align="center">

### **Pinout Diagram**

<div align="center">
    <a href="../resources/unit_sch_V_0_0_1_ue0099_Sensor_Touch.pdf">
        <img src="../resources/unit_pinout_v_0_0_1_ue0099_sensor_touch_en.jpg" width="500px"><br/> Schematics
    </a>
</div>
<br/>
<br/>

### **Pinout Details**

| Pin Label | Function     | Notes                           |
|-----------|--------------|---------------------------------|
| VCC       | Power Supply | 3.3V or 5V, depending on design  |
| GND       | Ground       | Common ground reference         |
| DOUT        | Data Signal  | Digital Output signal     |
| Mode Select | Solder Jumper | Select between Momentary or Toggle mode |
| Level Selection| Solder Jumper | Select between low and high sensitivity |

| Mode Selection | Level Selection | Description                              |
|----------------|-----------------|------------------------------------------|
| 0              | 0               | Single pulse, momentary                  |
| 0              | 1               | Single pulse, toggle (inverted pulse)    |
| 1              | 0               | Pulse latch, requires another touch to release |
| 1              | 1               | Pulse latch, requires another touch to release (inverted) |

## 📏 Dimensions

<div align="center">
<div align="center"><a href="../resources/unit_dimension_V_0_0_1_ue0099_Sensor_Touch.png"><img src="../resources/unit_dimension_V_0_0_1_ue0099_Sensor_Touch.png" style="max-width: 500px; height: auto;" alt="Dimensions"><br/> Dimensions</a></div>
</div>

## 📃 Topology

<div align="center">
<div align="center"><a href="../resources/unit_topology_V_0_0_1_ue0099_Sensor_Touch.png"><img src="../resources/unit_topology_V_0_0_1_ue0099_Sensor_Touch.png" style="max-width: 500px; height: auto;" alt="Topology"><br/> Topology</a></div>
<br/>
<br/>

| Ref. | Description                              |
|------|------------------------------------------|
| SW1  | Capacitive Touch Button                  |
| L1   | Built-In LED                             |
| IC1  | TTP223-BA6-TD Touch Detector             | 
| J1   | QWIIC Connector (JST 1 mm pitch) for I2C |
| SB1  | Solder Bridge for Mode Selection         | 
| SB2  | Solder Bridge for Logic Level Selector   |

</div>