#!/usr/bin/env python3
"""
Read a csv 'map' and pull all locations
"""

__author__ = "╰(｡•́‿•̀｡)つ──★*:・ﾟ"
__version__ = "0.1.0"
__license__ = "MIT"

# Import modules
import pandas as pd
from datetime import datetime
import pprint
pp = pprint.PrettyPrinter(indent=4)

import configparser
configF = 'config.ini'
parser = configparser.ConfigParser()
parser.read(configF)

# Set global variables
# set data file
data = pd.read_csv(parser.get('conf', 'data'))
# set zone
zone = parser.get('conf', 'zone')
dt = datetime.now()
desctimestamp = dt.strftime("%m/%d/%y - %H:%M:%S")
descriptions = {}


def main():
    """
    > Main entry point of the app
    Get the dimensions of the dataframe and assign them to variables
    Then, write variables to config
    """
    x,y = list(range(data.shape[0])), list(range(data.shape[1]))

    # Get all possible coordinates
    cords = [(l,r) for l in x for r in y]

    # Hit every item in the dataframe
    for p in cords:
        location = (p[0],p[1])
        #p is a coordiante tuple (x,y) from the list of all coordinates
        room = data.iloc[location]
        x,y = location                            # assign location coordinates to variables
        if room != 'empty':
            parser.set('desc', f"{zone} - {room}", "")

    with open(configF, "w+") as configfile:
            parser.write(configfile)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
