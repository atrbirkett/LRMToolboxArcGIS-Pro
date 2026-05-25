"""
Local Relief Model (LRM) Generator for ArcGIS Pro
This script creates a local relief model by subtracting a low-pass filtered 
(smoothed) DEM from the original DEM to highlight local topographic variations.
"""

import arcpy
from arcpy.sa import *
import os

# Set up parameters
input_dem = arcpy.GetParameterAsText(0)  # Input DEM
neighborhood_radius = arcpy.GetParameterAsText(1)  # Neighborhood radius in cells
output_lrm = arcpy.GetParameterAsText(2)  # Output LRM raster

try:
    # Check out Spatial Analyst extension
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
    else:
        raise Exception("Spatial Analyst extension is not available")
    
    arcpy.AddMessage("Starting Local Relief Model generation...")
    arcpy.AddMessage(f"Input DEM: {input_dem}")
    arcpy.AddMessage(f"Neighborhood radius: {neighborhood_radius} cells")
    
    # Convert radius to integer
    radius = int(neighborhood_radius)
    
    # Create neighborhood object (circular)
    neighborhood = NbrCircle(radius, "CELL")
    
    arcpy.AddMessage("Calculating focal statistics (mean filter)...")
    # Apply focal statistics to create smoothed DEM
    smoothed_dem = FocalStatistics(input_dem, neighborhood, "MEAN", "DATA")
    
    arcpy.AddMessage("Calculating Local Relief Model...")
    # Subtract smoothed DEM from original to get LRM
    lrm = Raster(input_dem) - smoothed_dem
    
    # Save the output
    arcpy.AddMessage(f"Saving output to: {output_lrm}")
    lrm.save(output_lrm)
    
    arcpy.AddMessage("Local Relief Model generation complete!")
    arcpy.AddMessage(f"Output saved to: {output_lrm}")
    
    # Check in extension
    arcpy.CheckInExtension("Spatial")
    
except arcpy.ExecuteError:
    arcpy.AddError(arcpy.GetMessages(2))
    
except Exception as e:
    arcpy.AddError(str(e))
    
finally:
    # Ensure extension is checked back in
    if arcpy.CheckExtension("Spatial") == "CheckedOut":
        arcpy.CheckInExtension("Spatial")
