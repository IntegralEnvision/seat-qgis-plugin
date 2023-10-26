
PMEC Site
----------

.. toctree::
   :maxdepth: 1
   :hidden:

   sedimentation.rst
   acoustics.rst 

The Pacific Marine Energy Center (PMEC) is a designated area for marine energy testing on the coast of Oregon. This site has been the focus of model development and SEAT application. A coupled hydrodynamic and wave model was developed using SNL-SWAN and Delft3D-Flow. A range of site conditions is listed in the Model Probabilities File. This site includes information regarding sediment grain size, device power generation, and acoustic effects.

**Accessing Demonstration Files**

To access the demonstration files relevant to this analysis, please refer to the section :ref:`tutorial-files-access`. This demonstration utilizes the :file:`DEMO unstructured` and :file:`style_files` folders as detailed in :ref:`DEMO_files`. A comprehensive list of files contained in the unstructured folder is available in :ref:`pmec_files`.




**List of Tutorial Files**

.. _pmec_files:

.. code-block:: none
   :caption: DEMO PMEC Tutorial Files

   DEMO
   ├───DEMO paracousti
   │   │   demo_paracousti_without_species.default
   │   │   demo_paracousti_without_species.ini
   │   │   demo_paracousti_with_receptor.default
   │   │   demo_paracousti_with_receptor.ini
   │   │
   │   ├───paracousti_files
   │   │       PacWave_3DSPLs_Hw0.5.nc
   │   │       PacWave_3DSPLs_Hw1.0.nc
   │   │       PacWave_3DSPLs_Hw1.5.nc
   │   │       PacWave_3DSPLs_Hw2.0.nc
   │   │       PacWave_3DSPLs_Hw2.5.nc
   │   │       PacWave_3DSPLs_Hw3.0.nc
   │   │       PacWave_3DSPLs_Hw3.5.nc
   │   │       PacWave_3DSPLs_Hw4.0.nc
   │   │       PacWave_3DSPLs_Hw4.5.nc
   │   │       PacWave_3DSPLs_Hw5.0.nc
   │   │       PacWave_3DSPLs_Hw5.5.nc
   │   │       PacWave_3DSPLs_Hw6.0.nc
   │   │       PacWave_3DSPLs_Hw6.5.nc
   │   │       PacWave_3DSPLs_Hw7.0.nc
   │   │
   │   ├───probability
   │   │       boundary_conditions.csv
   │   │
   │   ├───receptor
   │   │       Acoustic_Receptor - BlueWhale - Copy.csv
   │   │       Acoustic_Receptor - BlueWhale.csv
   │   │       Acoustic_Receptor - Harassment _Whale-IA-AVD-10.csv
   │   │       Acoustic_Receptor - Harassment _Whale.csv
   │   │
   │   └───species
   │           WhaleWatchPredictions_2021_01.csv
   │           WhaleWatchPredictions_2021_02.csv
   │           WhaleWatchPredictions_2021_03.csv
   │           WhaleWatchPredictions_2021_04.csv
   │           WhaleWatchPredictions_2021_05.csv
   │           WhaleWatchPredictions_2021_06.csv
   │           WhaleWatchPredictions_2021_07.csv
   │           WhaleWatchPredictions_2021_08.csv
   │           WhaleWatchPredictions_2021_09.csv
   │           WhaleWatchPredictions_2021_10.csv
   │           WhaleWatchPredictions_2021_11.csv
   │           WhaleWatchPredictions_2021_12.csv
   │
   └───DEMO structured
      │   shear_stress_without_receptor.default
      │   shear_stress_without_receptor.ini    
      │   shear_stress_with_receptor.default   
      │   shear_stress_with_receptor.ini       
      │   velocity_without_receptor.default    
      │   velocity_without_receptor.ini        
      │   velocity_with_receptor.default       
      │   velocity_with_receptor.ini
      │
      ├───devices-not-present
      │       trim_sets_flow_inset_allruns.nc  
      │       trim_sets_flow_inset_allruns.nc.aux.xml
      │
      ├───devices-present
      │       trim_sets_flow_inset_allruns.nc
      │
      ├───Output
      │   └───ShearStress_with_receptor
      │           _20231023.log
      │
      ├───power_files
      │   ├───16x6
      │   │       POWER_ABS_001.OUT
      │   │       POWER_ABS_002.OUT
      │   │       POWER_ABS_003.OUT
      │   │       POWER_ABS_004.OUT
      │   │       POWER_ABS_005.OUT
      │   │       POWER_ABS_006.OUT
      │   │       POWER_ABS_007.OUT
      │   │       POWER_ABS_008.OUT
      │   │       POWER_ABS_009.OUT
      │   │       POWER_ABS_010.OUT
      │   │       POWER_ABS_011.OUT
      │   │       POWER_ABS_012.OUT
      │   │       POWER_ABS_013.OUT
      │   │       POWER_ABS_014.OUT
      │   │       POWER_ABS_015.OUT
      │   │       POWER_ABS_016.OUT
      │   │       POWER_ABS_017.OUT
      │   │       POWER_ABS_018.OUT
      │   │       POWER_ABS_019.OUT
      │   │       POWER_ABS_020.OUT
      │   │       POWER_ABS_021.OUT
      │   │       POWER_ABS_022.OUT
      │   │       POWER_ABS_023.OUT
      │   │       POWER_ABS_024.OUT
      │   │       rect_16x6.obt
      │   │       rect_16x6.pol
      │   │
      │   └───4x4
      │           POWER_ABS_001.OUT
      │           POWER_ABS_002.OUT
      │           POWER_ABS_003.OUT
      │           POWER_ABS_004.OUT
      │           POWER_ABS_005.OUT
      │           POWER_ABS_006.OUT
      │           POWER_ABS_007.OUT
      │           POWER_ABS_008.OUT
      │           POWER_ABS_009.OUT
      │           POWER_ABS_010.OUT
      │           POWER_ABS_011.OUT
      │           POWER_ABS_012.OUT
      │           POWER_ABS_013.OUT
      │           POWER_ABS_014.OUT
      │           POWER_ABS_015.OUT
      │           POWER_ABS_016.OUT
      │           POWER_ABS_017.OUT
      │           POWER_ABS_018.OUT
      │           POWER_ABS_019.OUT
      │           POWER_ABS_020.OUT
      │           POWER_ABS_021.OUT
      │           POWER_ABS_022.OUT
      │           POWER_ABS_023.OUT
      │           POWER_ABS_024.OUT
      │           rect_4x4.obt
      │           rect_4x4.pol
      │
      ├───probabilities
      │       probabilities.csv
      │
      ├───receptor
      │       grainsize_receptor.tif
      │       grainsize_receptor.tif.aux.xml
      │       grain_size_receptor.csv
      │       velocity_receptor.csv
      │
      └───_plugin-config-files
            cgrant_4x4.ini
            cgrant_test.ini
            oregon_wec_config.ini
            oregon_wec_config_16x6.ini
            oregon_wec_config_4x4.ini