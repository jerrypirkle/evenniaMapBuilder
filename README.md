# evenniaMapBuilder
create evennia zone from a csv map

Input: A csv 'map'
Output: A batch file that creates a zone based on the locations on the 'map'

See:
- Python MUD/MUX/MUSH/MU* development system http://www.evennia.com
- https://github.com/evennia/evennia

## Files

- config.ini - configuration parameters, stores descriptive text
- locget.py - gets all locations in dictionary form and loads them into config.ini. descriptions in config.ini will used later to describe room locations.
- batchbld.py - generates a batch file that creates all locations in the csv and creates all connections between the locations (neighbors).
- locations.csv - sample file. the csv can be any size, but the first row should contain numbers
