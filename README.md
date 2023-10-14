To synthesize Verilog -> 74xx PCB

1. Install yosys & build from source - https://github.com/YosysHQ/yosys

2. Clone 74xx-liberty - https://github.com/pepijndevos/74xx-liberty/tree/maste (http://pepijndevos.nl/2019/07/18/vhdl-to-pcb.html)

3. Install SKiDL
pip install skidl

4. To synthesize pwmled.v:

cd stat
make pwmled.stat # synthesize and run stat
../ic_count.py pwmled.stat # count number of chips used
cd ../sim
make pwmled.vcd # synth to low-level verilog and simulate
gtkwave pwmled.vcd # show test bench results
cd ../kicad
make pwmled.net # generate kicad netlist


