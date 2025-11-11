# Hardware


<div align="center">
    <a href="./unit_sch_V_0_0_1_ue0099_Sensor_Touch.pdf">
        <img src="resources/Schematics_icon.jpg?raw=false" width="450px"><br/> Schematics
    </a>
</div>

## Key Technical Specifications

<div align="center">

| Symbol | Parameter                       | Min | Typ | Max | Unit |
|--------|---------------------------------|-----|-----|-----|------|
| VDD    | Operating Voltage               | 2.0 | 3   | 5.5 | V    |
| f      | System oscillator               | 16  | -   | 512 | kHz  |
| f_sen  | Sensor oscillator               | -   | 1   | -   | MHz  |
| V_IL   | Sensor Input Low Voltage        | 0   | -   | 0.2 | VDD  |
| V_IH   | Sensor Input High Voltage       | 0.8 | -   | 1.0 | VDD  |
| T_rf*   | Response Time at fast mode      | -   | -   | 60  | mS   |
| T_rl*   | Response Time at low power mode | -   | -   | 220 | mS   |

</div>
*The sensor is in low-power mode by default. When it detects a key touch it switches to fast mode. After the touch is released, the sensor returns to low-power mode in about 12 seconds.

## 🔌 Pinout


### Pinout Diagram

<div align="center">
    <a href="./unit_sch_V_0_0_1_ue0099_Sensor_Touch.pdf">
        <img src="resources/unit_pinout_v_0_0_1_ue0099_sensor_touch_en.jpg" width="500px"><br/> Schematics
    </a>
</div>
<br/>
<br/>

### Pinout Details

<div align="center">

| Pin Label | Function     | Notes                           |
|-----------|--------------|---------------------------------|
| VCC       | Power Supply | 3.3V or 5V, depending on design  |
| GND       | Ground       | Common ground reference         |
| DOUT        | Data Signal  | Digital Output signal     |
| Mode Select | Solder Jumper | Select between Momentary or Toggle mode |
| Level Selection| Solder Jumper | Select between low and high sensitivity |

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

## 📏 Dimensions

<div align="center">
<a href="./resources/unit_dimension_V_0_0_1_ue0099_Sensor_Touch.png"><img src="./resources/unit_dimension_V_0_0_1_ue0099_Sensor_Touch.png" width="500px"><br/> Dimensions</a>
</div>
