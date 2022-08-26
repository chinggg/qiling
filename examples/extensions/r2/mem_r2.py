#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import sys
sys.path.append('..')

from qiling import Qiling
from qiling.const import QL_VERBOSE
from qiling.extensions.r2 import R2


if __name__ == "__main__":
    # test shellcode mode
    ARM64_LIN = bytes.fromhex('420002ca210080d2400080d2c81880d2010000d4e60300aa01020010020280d2681980d2010000d4410080d2420002cae00306aa080380d2010000d4210400f165ffff54e0000010420002ca210001caa81b80d2010000d4020004d27f0000012f62696e2f736800')
    print("\nLinux ARM 64bit Shellcode with map_ptr")
    ql = Qiling(code=ARM64_LIN, archtype="arm64", ostype="linux", verbose=QL_VERBOSE.DEBUG)
    print("\nR2 Init")
    r2 = R2(ql)
    # list opened files
    print(r2._cmd('o'))
    # disassemble 32 instructions
    print(r2._cmd('pd 32'))
    ql.run()
