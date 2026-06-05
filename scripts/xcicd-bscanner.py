
#!/usr/bin/env python3

import sys

from xcicd.bscanner import main

if __name__ == "__main__":
    if len(sys.argv) < 4:
        raise RuntimeError(
            "missing arguments:\n"
            "xcicd-bscanner PROJECT_ID CURRENT_BRANCH_NAME LAST_COMMIT"
        )
    try:
        main(sys.argv)
    except Exception as e:
        raise RuntimeError(e)
