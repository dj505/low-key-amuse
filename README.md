# low-key-amuse
A low-key e-amusement keypad for DDR cabs (and other cabs? :eyes:)

# Bill of Materials
|           Part           | Qty |              Description              |
|--------------------------|-----|---------------------------------------|
|MPR121                    |1    |Touch sensor                           |
|16 pin FFC                |1    |Reverse direction, 1mm pitch           |
|100nF capacitor           |2    |SMD, 0805 package                      |
|75k ohm resistor          |1    |SMD, 0805 package                      |
|4.2k ohm resistor         |2    |SMD, 0805 package                      |
|Raspberry Pi Pico         |1    |                                       |
|TE Connectivity 1-84952-6 |2    |FPC connector, 16 pin, bottom contacts |

**Notes:**
* Be sure the ribbon cables you purchase match the connectors. "Forward" direction ribbons will require you to use connectors with top contacts, however I would recommend "reverse" direction ribbons with bottom contact connectors.
* Some PCBA services might not carry 4.2k ohm resistors, or they may be difficult to find. Anything from 2k to 10k ohms should work. This is just what worked for me personally in testing.

# Required Libraries
All of the required libraries can be found in the [library bundle] for your installed version of CircuitPython. This project was built and tested with 8.x.x. The following should be placed in the `lib` folder on the `CIRCUITPY` drive:
* adafruit_bus_device
* adafruit_hid
* adafruit_mpr121.mpy
