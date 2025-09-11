# Hardware


<div align="center">
    <a href="./unit_sch_V_0_0_1_ue0099_Sensor_Touch.pdf">
        <img src="resources/Schematics_icon.jpg?raw=false" width="450px"><br/> Schematics
    </a>
</div>


## 🔌 Pinout

<div align="center">

### **Pinout Diagram**

<div align="center">
    <a href="./unit_sch_V_0_0_1_ue0099_Sensor_Touch.pdf">
        <img src="resources/unit_pinout_v_0_0_1_ue0099_sensor_touch_en.jpg" width="500px"><br/> Schematics
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

### **Mode and Level Selection Table**

| Mode Selection | Level Selection | TOG | AHLB | Pad Q (CMOS Output)                     | Pad OPDO (Open Drain Output)                | Description                                |
|----------------|-----------------|-----|------|------------------------------------------|---------------------------------------------|--------------------------------------------|
| 0              | 0               | 0   | 0    | Direct mode, active high                 | Direct mode, open drain active high         | Single pulse, momentary                     |
| 0              | 1               | 0   | 1    | Direct mode, active low                  | Direct mode, open drain active low          | Single pulse, toggle (inverted pulse)       |
| 1              | 0               | 1   | 0    | Toggle mode, power-on state = 0          | Toggle mode, power-on = High-Z, active high | Pulse latch, requires another touch to release |
| 1              | 1               | 1   | 1    | Toggle mode, power-on state = 1          | Toggle mode, power-on = High-Z, active low  | Pulse latch, requires another touch to release (inverted) |

#### Notes on the integration:

The table below summarizes how the mode and level selection (left columns) determine the sensor's operative functionality. The TOG and AHLB columns represent the pad configuration bits as defined in the TTP223 datasheet. "Pad Q" and "Pad OPDO" show the output modes (CMOS or open drain), while the "Description" column provides a simplified explanation of the resulting behavior. This layout lets you quickly see how the functional mode (momentary/toggle), pad configuration, and output type relate to each other.

## 📏 Dimensions

<div align="center">
<a href="./resources/unit_dimension_V_0_0_1_ue0099_Sensor_Touch.png"><img src="./resources/unit_dimension_V_0_0_1_ue0099_Sensor_Touch.png" width="500px"><br/> Dimensions</a>
</div>

## 📃 Topology

<div align="center">
<a href="./resources/unit_topology_V_0_0_1_ue0099_Sensor_Touch.png"><img src="./resources/unit_topology_V_0_0_1_ue0099_Sensor_Touch.png" width="500px"><br/> Topology</a>
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

