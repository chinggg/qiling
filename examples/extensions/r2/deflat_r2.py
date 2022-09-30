#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import sys

sys.path.append('..')

from qiling import Qiling
from qiling.const import QL_VERBOSE
from qiling.extensions.r2 import R2, R2Deflator



if __name__ == "__main__":
    ql = Qiling(['../bins/test_fla_argv', '2'], 'rootfs/x86_linux', verbose=QL_VERBOSE.DEFAULT)
    r2 = R2(ql)
    # now r2 has only rbuf but no symbol info
    fcn = r2.get_fcn_at(0x08049190)
    print(fcn)
    r2.deflat(fcn)
    ql.run()
    r2.shell()
