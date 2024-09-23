from pathlib import Path
import sys
import random

import vunit_common

# NOTE: This assumes the location of the ./rtl and ./workspace directory relative to where this is run from
WORKSPACE = Path(__file__).parent / "workspace" / "modelsim"
LIB_ROOT = Path(__file__).parent / ".." / "lib"
SYN_ROOT = Path(__file__).parent / ".." / "syn"
SIM_ROOT = Path(__file__).parent / ".." / "sim"

vu, lib = vunit_common.init(WORKSPACE)

vunit_common.add_source(lib, LIB_ROOT / "./verilog-axi/rtl/axil_ram.v")
vunit_common.add_source(lib, SYN_ROOT / "./axil_if/axil_if.sv")
vunit_common.add_source(lib, SYN_ROOT / "./axil_ram_wrapper/axil_ram_wrapper.sv")
vunit_common.add_source(lib, SIM_ROOT / "./axil_bfm/axil_bfm.sv")
vunit_common.add_source(lib, SIM_ROOT / "./axil_ram_wrapper/axil_ram_wrapper_tb.sv")

# Create testbench
tb = lib.test_bench("axil_ram_wrapper_tb")

tb.add_config("TEST", parameters={
    "PIPELINE_OUTPUT"   : 0,
    "ADDR_WIDTH"        : 16,
    "DATA_WIDTH"        : 32,
    "ADDRESS_1"         : 132,
    "ADDRESS_2"         : 78,
    "DATA_1"            : 88943,
    "DATA_2"            : 1332,
    "USE_RANDOM_WAIT"   : 0
    })

vu.main()