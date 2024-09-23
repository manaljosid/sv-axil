# SystemVerilog AXI-Lite Components
## Introduction
A collection of AXI-Lite bus components consisting of wrappers of [verilog-axi](https://github.com/alexforencich/verilog-axi), test infrastructure and custom modules and interfaces. All test benches utilise [VUnit](https://github.com/VUnit/vunit) and Modelsim.

## Testing
To run the testbench open the `python` directory and run the python file relevant for each testbench using for example `python axil_ram_wrapper_tb.py`. To run with a gui use `python axil_ram_wrapper_tb.py -g`. If you wish to run specific tests within each testbench you append the command with the test name.
