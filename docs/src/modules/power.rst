
Power Module
------------

The SEAT power module evaluates the power generated by a MEC array. Power is calculated for individual arrays, for a single hydrodynamic scenario, as well as for the entire scenario defined by the hydrodynamic probabilities file.  

Input 
^^^^^^
The input for the power module is the turbine power generation and location output from the MHKit-friendly tools (i.e., SNL-SWAN, SNL-Delft3D-CEC). Obstacles make up a device, and intersecting obstacles are considered to be one device. Separate obstacles are considered to be separate devices.

The files include:

- Model output (.OUT files): Formatted file that has the power data for each obstacle. A device can consist of multiple obstacles.
- Polygon files (.pol files): Polygon configurations for each obstacle.
- \*Model Probability Condition file (CSV): Contains model weights, used to weight different run scenarios.

\* Optional input files

Input File Sources
""""""""""""""""""""""
The power module is only designed to read output from the MHKit friendly tools (i.e., SNL-SWAN, SNL-Delft3D-CEC). 


Output 
^^^^^^^
Both CSVs and PNGs are generated for each run scenario. 
The CSVs contain the power generated for each device and obstacle, while the PNGs provide visualizations of the power generated for each device and obstacle. 

CSV
""""

  - **BC_probability_wPower.csv** : probabilities input file with appended power generated for each scenario
  - **Obstacle_Matching.csv** : Obstacle pairs corresponding to a single device and centroid X,Y.
  - **Power_per_device_annual.csv** : Total power generated (Watts) per device over the annual timespan (probabilities file).
  - **Power_per_device_per_scenario.csv** : Table of total power generated (Watts) with device (row), and power file (column).

PNG
""""

  - **Scaled_Power_per_device_per_scenario.png** : subplots of bar graph of power generated for each run per device.
  - **Scaled_Power_per_device_per_obstacle.png** : subplots of bar graph of power generated for each run per obstacle.
  - **Total_Scaled_Power_Bars_per_Run.png** : Bar graph of total power generated for each run scenario (probabilities file).
  - **Total_Scaled_Power_Bars_per_obstacle.png** : Bar graph of total power generated for each obstacle.
  - **Total_Scaled_Power_per_Device.png** : Bar graph of total power generated for each device
  - **Obstacle_Locations.png** : Spatial plot of XY coordinates for each obstacle endpoint.
  - **Device Number Locations.png** : Spatial plot of XY coordinates for each device.
  - **Device_Power.png**: Spatial heat map of total power generated (mega watts) for each device.


Core Functions
^^^^^^^^^^^^^^^

+--------------------------------------------+------------------------------------------------------------------+
| Function                                   | Description                                                      |
+============================================+==================================================================+
| ``read_obstacle_polygon_file()``           | Reads the obstacle polygon file to obtain xy coordinates of each |
|                                            | obstacle.                                                        |
+--------------------------------------------+------------------------------------------------------------------+
| ``find_mean_point_of_obstacle_polygon()``  | Calculates the center of each obstacle based on xy coordinates.  |
+--------------------------------------------+------------------------------------------------------------------+
| ``plot_test_obstacle_locations()``         | Creates a plot showing the spatial distribution and location of  |
|                                            | each obstacle.                                                   |
+--------------------------------------------+------------------------------------------------------------------+
| ``centroid_diffs()``                       | Determines the closest centroid pair among obstacles.            |
+--------------------------------------------+------------------------------------------------------------------+
| ``extract_device_location()``              | Creates a dictionary summary of each device location.            |
+--------------------------------------------+------------------------------------------------------------------+
| ``pair_devices()``                         | Determines the two intersecting obstacles that create a device.  |
+--------------------------------------------+------------------------------------------------------------------+
| ``create_power_heatmap()``                 | Creates a heatmap visualizing device location and power output.  |
+--------------------------------------------+------------------------------------------------------------------+
| ``read_power_file()``                      | Reads power file and extracts final set of converged data.       |
+--------------------------------------------+------------------------------------------------------------------+
| ``sort_data_files_by_runorder()``          | Sorts data files by run order based on boundary conditions data. |
+--------------------------------------------+------------------------------------------------------------------+
| ``sort_bc_data_by_runorder()``             | Sorts boundary condition data by run order.                      |
+--------------------------------------------+------------------------------------------------------------------+
| ``reset_bc_data_order()``                  | Resets the order of boundary condition data.                     |
+--------------------------------------------+------------------------------------------------------------------+
| ``calculate_power()``                      | Reads the power files, calculates the total annual power based   |
|                                            | on hydrodynamic probabilities, and saves data and visualizations.|
+--------------------------------------------+------------------------------------------------------------------+
