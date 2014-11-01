nasa_wrs_converter
==================

to convert from lat/lon to nasa wrs path/row

use the WRS-2_bound_world.csv file in the assets folder as input (or convert using kml2csv.py)

then use ll2Pr(lat,lon,csvFile) to retrieve the path/row

options are day only (1 by default)

at some point in the future will update it to calculate if the point is in multiple scenes and return tuple of tuples.
