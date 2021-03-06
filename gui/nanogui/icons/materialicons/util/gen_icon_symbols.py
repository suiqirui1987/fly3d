import os

success = False

with open("../materialicons.go", "w") as output:
    output.write("""package materialicons

import "github.com/suiqirui1987/fly3d/gui/nanogui"

// generated by util/gen_icon_symbols.py

const (
""")
    for line in open("./codepoints").readlines():
        name, codepoint = line.split(" ")
        output.write("Icon%s nanogui.Icon = 0x%s" % (name.title().replace("_", ""), codepoint))
    output.write(")") 
    success = True

if success:
    os.system("go fmt ../materialicons.go")

