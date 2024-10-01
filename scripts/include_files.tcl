set sv_axil_library_dir [file dirname [file normalize [info script]]]
set sv_axil_library_dir ${sv_axil_library_dir}/..

add_files $sv_axil_library_dir/lib/verilog-axi/rtl
add_files $sv_axil_library_dir/syn