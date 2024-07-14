import sys
from pprint import pprint

import tiltbrush.tilt

if __name__ == '__main__':
    path = " ".join(sys.argv[1:])
    try:
        tilt = tiltbrush.tilt.Tilt(path)
        pprint(tilt.metadata['CameraPaths'])
    except Exception as e:
        print("ERROR: %s" % e)
