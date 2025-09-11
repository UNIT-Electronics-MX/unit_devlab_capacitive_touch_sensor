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

#### Mode & Level Selection

| Mode | Level | TOG | AHLB | Pad Q (CMOS)         | Pad OPDO (Open Drain)    | Behavior                        |
|------|-------|-----|------|----------------------|--------------------------|----------------------------------|
| 0    | 0     | 0   | 0    | Active high          | Open drain, active high  | Momentary, single pulse          |
| 0    | 1     | 0   | 1    | Active low           | Open drain, active low   | Momentary, inverted pulse        |
| 1    | 0     | 1   | 0    | Toggle, power-on=0   | Toggle, active high      | Toggle, touch to change state    |
| 1    | 1     | 1   | 1    | Toggle, power-on=1   | Toggle, active low       | Toggle, inverted                 |

*Mode and level solder jumpers set output type and behavior (momentary/toggle, active high/low).*

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

