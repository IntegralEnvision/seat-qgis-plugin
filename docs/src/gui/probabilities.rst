Probabilities (optional)
------------------------

The probabilities file, while optional, serves to enhance your analysis, providing insights into the run order and the likelihood of each model condition unfolding. Adhere to the prescribed naming convention (as delineated in the device/baseline model section). Note that this file correlates with the return interval in years.

Shear Stress & Velocity
^^^^^^^^^^^^^^^^^^^^^^^

For these types of analyses:

- `run order`: Represents the sequence of each condition.
- `% of year`: Indicates the probability of a given condition arising within a year.
- While you may include optional columns such as `wave height` or `period`, they won't impact the analysis.

For added flexibility, you can incorporate an 'Exclude' column, enabling you to earmark certain runs for omission.

.. note::

   If you include the 'Exclude' column, the `% of year` won't adjust to total 100%.

.. figure:: ../media/probabilities_input.webp
   :scale: 100 %
   :alt: Interface depicting the Probabilities Input in SEAT's GUI.

**Example of a Probabilities Input**

+------+--------+--------+-------------+---------+-----------+---------+
| Hs[m]| Tp[s]  | Dp[deg]| % of dir bin| % of yr | run order | Exclude |
+------+--------+--------+-------------+---------+-----------+---------+
| 1.76 |   6.6  | 221.8  |    15.41    |   0.39  |    6      |         |
+------+--------+--------+-------------+---------+-----------+---------+
| 2.67 |   8.62 | 220.8  |    40.68    |   1.029 |   16      |         |
+------+--------+--------+-------------+---------+-----------+---------+
| 4.06 |  10.16 | 221.3  |    23.47    |   0.593 |   20      |         |
+------+--------+--------+-------------+---------+-----------+---------+
| 1.37 |  15.33 | 224    |    8.06     |   0.204 |    2      |         |
+------+--------+--------+-------------+---------+-----------+---------+
| 7.05 |  12.6  | 223.6  |    3.42     |   0.086 |   24      |    x    |
+------+--------+--------+-------------+---------+-----------+---------+

Key:

- 'Hs': Wave height.
- 'Tp': Wave period.
- 'Dp': Direction.
- '% of dir bin': Proportion within a direction bin.
- '% of yr': Percentage of the year.
- 'run order': Execution sequence.
- 'Exclude': Designation for excluding runs.

ParAcousti
^^^^^^^^^^

For ParAcousti analyses, the file format differs from that of shear stress and velocity.

**Required Columns**:

  1. ParAcousti File: Name of the ParAcousti .nc file.
  2. Species Percent Occurrence File: Accepts either a .csv or .tif format.
  3. Species Density File: Also, either a .csv or .tif format.
  4. % of yr: Denotes the percentage of the year.

**File Specifications**:

- If you're using .csv for the Species Percent Occurrence and Species Density Files, they must contain the essential columns: "latitude", "longitude", and either "percent" and/or "density". All supplementary columns will be overlooked.
- If you opt for a .tif format for the aforementioned files, ensure consistency in the EPSG code across them.

**Example of a ParAcousti Input**

+--------------------------+-----------------------------+------------------------+---------+
| ParAcousti File          | Species % Occurrence File   | Species Density File   | % of yr |
+--------------------------+-----------------------------+------------------------+---------+
| paracousti_data1.nc      | species_occurrence1.csv     | species_density1.csv   | 0.25    |
+--------------------------+-----------------------------+------------------------+---------+
| paracousti_data2.nc      | species_occurrence2.tif     | species_density2.tif   | 0.50    |
+--------------------------+-----------------------------+------------------------+---------+
| paracousti_data3.nc      | species_occurrence3.csv     | species_density3.csv   | 0.10    |
+--------------------------+-----------------------------+------------------------+---------+
| paracousti_data4.nc      | species_occurrence4.tif     | species_density4.tif   | 0.15    |
+--------------------------+-----------------------------+------------------------+---------+

Key:

- `ParAcousti File`: The name of the ParAcousti .nc file.
- `Species % Occurrence File`: Either a .csv or .tif file indicating species percent occurrence.
- `Species Density File`: Either a .csv or .tif file detailing species density.
- `% of yr`: Represents the percentage of the year.
