# Local Relief Model (LRM) Toolbox for ArcGIS Pro

A Python toolbox for generating Local Relief Models from Digital Elevation Models (DEMs) in ArcGIS Pro. Local Relief Models remove regional topographic trends to highlight subtle local variations, making them useful for archaeological prospection, geomorphological analysis, and landscape archaeology in general.

## What is a Local Relief Model?

A Local Relief Model (LRM) is a visualization technique that enhances subtle topographic features by removing broad-scale terrain trends. It subtracts a smoothed (low-pass filtered) version of a DEM from the original, revealing local elevation anomalies that might otherwise be hidden by regional slopes or major landforms.

## Features
- Simple one-step processing
- Adjustable neighborhood radius for different feature scales
- Works with any raster DEM format (.tif, .img, .asc, geodatabase rasters)

## Requirements
- **ArcGIS Pro** (any recent version)
- **Spatial Analyst Extension** (required)
- Python 3.x (included with ArcGIS Pro)

## Installation

### Quick Start (Using the Pre-Made Toolbox)

1. **Download the repository:**
   ```bash
   git clone https://github.com/yourusername/arcgis-lrm-toolbox.git
   ```
   Or click **Code → Download ZIP** on GitHub and extract

2. **Important: Keep files together**
   - Place `LRMToolbox.atbx` and `LocalReliefModel.py` in the **same folder**
   - Do not separate these files or the toolbox won't find the script

3. **Open the toolbox in ArcGIS Pro:**
   - In the Catalog pane, right-click **Folders** → **Add Folder Connection**
   - Navigate to the folder containing the downloaded files
   - Expand the folder to see `LRMToolbox.atbx`
   - Double-click the toolbox to open it

4. **If you see a script path error:**
   - Right-click the tool → **Properties** (or **Edit**)
   - Go to the **Execution** tab
   - Click the folder icon next to **Script File**
   - Navigate to `LocalReliefModel.py` in the same folder
   - Click OK
   - This only needs to be done once

### Alternative: Create Your Own Toolbox

If you prefer to build the toolbox from scratch or want to customize it:

1. **Download `LocalReliefModel.py`** from the repository

2. **Open ArcGIS Pro**

3. **Create a new toolbox:**
   - In the Catalog pane, right-click a folder
   - Select **New > Toolbox**
   - Name it whatever you prefer

4. **Add the script tool:**
   - Right-click the toolbox → **New > Script**
   - Configure as described in the detailed setup instructions below

## Tool Configuration

### General Tab
- **Name:** `Generate_Local_Relief_Model`
- **Label:** `Generate Local Relief Model`
- **Description:** Creates a local relief model by removing regional topographic trends from a DEM

### Parameters Tab

Add three parameters in this order:

| Label | Name | Data Type | Type | Direction | Default |
|-------|------|-----------|------|-----------|---------|
| Input DEM | `input_dem` | Raster Dataset | Required | Input | - |
| Neighborhood Radius (cells) | `neighborhood_radius` | Long | Required | Input | 10 |
| Output Local Relief Model | `output_lrm` | Raster Dataset | Required | Output | - |

### Execution Tab
- **Script File:** Browse to `LocalReliefModel.py` from this repository

## Tool Configuration
1. **Run the tool** from your toolbox
2. **Select your input DEM** (any raster format: .tif, .img, .asc, etc.)
3. **Set the neighborhood radius:**
   - Small (5-10 cells): Highlights very fine details
   - Medium (10-20 cells): Good for archaeological features (recommended starting point)
   - Large (20-50 cells): Removes broader landforms, highlights major earthworks
4. **Specify output location and name**
5. **Click Run**

### Choosing the Right Radius
The neighborhood radius determines what scale of topography is considered "regional" versus "local":
- **5-10 cells:** Fine-scale features, removes gentle slopes
- **10-20 cells:** Archaeological earthworks, structures, field boundaries (recommended)
- **20-50 cells:** Larger archaeological complexes, removes hillslopes
- **50+ cells:** Very large features, removes entire landforms

**Rule of thumb:** The radius should be larger than the features you want to detect.
For a 1m resolution DEM with radius = 15, this equals a 15-meter circular neighborhood.

## Visualization Tips
For best results when displaying the LRM:
1. **Stretch symbology** to ±1 or ±2 standard deviations
2. **Use a diverging color ramp** (blue-white-red) to show positive/negative values
3. **Combine with hillshade** for enhanced 3D effect
4. **Adjust transparency** to overlay on original DEM or aerial imagery

## Technical Details
### Algorithm
1. Apply Focal Statistics with circular neighborhood and MEAN statistic to create smoothed DEM
2. Subtract smoothed DEM from original: `LRM = Original - Smoothed`
3. Result contains positive values (local highs) and negative values (local lows)

## Citation
If you use this tool in published research, please cite:
```
Birkett, A. T. R. (2025). Local Relief Model Toolbox for ArcGIS Pro. 
GitHub repository: [https://github.com/atrbirkett/LRMToolboxArcGIS-Pro](https://github.com/atrbirkett/LRMToolboxArcGIS-Pro)
```

## Contact

- **Author:** [Alex Birkett]
- **Institution:** [University of Bristol, Department of Anthropology and Archaeology]
- 
## Version History

### v1.0.0 (2025)
- Initial release
- Basic LRM generation with adjustable neighborhood radius
- Error handling and progress messages
