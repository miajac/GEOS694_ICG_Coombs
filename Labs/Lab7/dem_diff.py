"""
dem_difference was created to difference dems that have differing grids, pixel 
sizes, horizontal coordinate systems, and vertical coordinate systems. It will 
also visually present the differenced dems and save a raster file of the 
differenced dem to the folder of your choosing.  
Eventually i want: 
To call this file:

    $ python dem_diff.py dem1 dem2 folder_out file_type vcrs hcrs

where:
    dem1, dem2: the dems to be differenced 
    folder_out: the folder the differenced dems should be saved in
    file_type: the file type the differenced dems should be saved as; options 
    include: geotiffs, etc.
    vcrs: the vertical coordinate reference system you want all dems to be 
    projected to
    hcrs: the horizontal coordinate reference system you want all dems projected
    to

Requirements: sys, geoutils, xdem
"""
import sys
import geoutils as gu
import xdem

# Load DEMs
dem1 = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/ArcticDEM_strips_20170923_EPSG_4326_2m.tif')
dem2 = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Canwell_4Aug25_DTM.tif')

dem1.plot(cmap="RdYlBu", vmin=0, vmax=2000, cbar_title="DEM 2017 (m)")

# Get info on each dem
print("Before corrections:")
print(dem1.info())
print(dem2.info())

# Set vertical CRS 
dem1.set_vcrs("Ellipsoid")  
dem2.set_vcrs("Ellipsoid")  

# Convert vertical coordinate system to EGM96
dem1.to_vcrs("EGM96") 
dem2.to_vcrs("EGM96")

# Reproject so that both dems have the same bounds, resolution, and coordinate system 
dem1_reproj = dem1.reproject(dem2)

print('After corrections DEM 1:', dem1_reproj.info())
print('After corrections DEM 2:', dem2.info())

# Difference the DEMs
diff_dem = dem2 - dem1_reproj

diff_dem.info(stats=True)

# Plot the differenced DEMs
diff_dem.plot(cmap="RdYlBu", vmin=-20, vmax=20, cbar_title="Elevation differences (m)")

# Save the DEMs to a file
diff_dem.save("2025lidar_2017arcticdem.tif")