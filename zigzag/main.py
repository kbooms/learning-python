# that anything like zug zug?

import time, sys

indent = 0      # How many spaces to indent
indentIncreasing = True     # Whether the indent is increasing or not
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.05)
        if indentIncreasing:
            # Increase the number of spaces
            indent += 1
            if indent == 20:
                # Change direction
                indentIncreasing = False
        else:
            # Decrease the number of spaces
            indent -= 1
            if indent == 0:
                # Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
