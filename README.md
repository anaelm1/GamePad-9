# GamePad 9

GamePad 9 is a 9 key macropad with a rotary encoder, an OLED Display. It uses KMK firmware

It is made as a dedicated macropad which can be used to play games(first person or racing etc).

## Features:
- 3D printed body with a honeycomb design to show the PCB. 
- 128x32 OLED Display.
- EC11 Rotary encoder to increase/decrease the volume, and skip to the next song.
- 9 Keys (Tab, W, E, A, S, D, Shift, Space, Control).


## CAD Model:
The pcb is attached to the base at a height of 2mm using 4 M3 screws for optimal support. The top plate is attached to the body using M3 screws and heat inserts in the 4 corners. 

It has 2 separate printed pieces. The base where the PCB sits, and the top cover. The project name and my name is engraved on the top plate as well.

<img src=assets/Pic.png alt="Model" />

Made in Fusion360. 


## PCB
Here's my PCB! It was made in KiCad.

Schematic
<img src=assets/Finalschema.PNG alt="Schematic" width = 300/>

PCB
<img src=assets/PCB.PNG alt="Schematic" width =300 />
<img src=assets/PCBB.PNG alt="Schematic" width =300 />

## Firmware Overview
This hackpad uses KMK firmware for everything. 

- the rotary encoder changes volume. press to next song.
- The 9 keys are Tab, W, E, A, S, D, Shift, Space, Control.
- The OLED is text. (Will change to an animation in the future)


## BOM:
These are the components used in the GamePad 9:

- 9x Cherry MX Switches.
- 9x DSA Keycaps.
- 4x M3x5x4 Heatset inserts.
- 8x M3x16mm Screws. (These might be changed if other screw sizes suit better)
- 9x 1N4148 DO-35 Diodes.
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (2 printed parts)

## Info:
This macropad is made as part of the Hack Club Hackpad program! 
