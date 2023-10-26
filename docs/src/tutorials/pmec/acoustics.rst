Acoustic Effects
^^^^^^^^^^^^^^^^

The acoustic effects from the WEC array at PMEC can be evaluated using the Acoustic module in the SEAT GUI. This module reads in individual Paracousti model .nc files that correspond to wave conditions. 

Input
""""""

If you have not done so before you will need to create input files for the default files provided. To do so naviage to :file:`DEMO/DEMO DEMO paracousti/`. In that folder you will find a number of .default files. You need to open these and replace ``<input_folder>`` with the path to the DEMO unstructured folder on your machine and ``<style_folder>`` with the path to the style_files folder on your machine. If you use python a script titled ``localize_input_files.py`` will do this for you. You can run this script by navigating to the DEMO unstructured folder in a terminal and typing ``python localize_input_files.py``. If you do not have python you can open the files in a text editor and replace the text manually or with a find and replace feature. If changing via a text editor save the file as a .ini file.

Example use of the script is shown below. After running the script .ini files will appear in the DEMO unstructured folder. These are the files you will use to load the inputs into the SEAT GUI.

.. code_block::bash
   
   $ python localize_input_files.py 
   Where are your input files? C:\\Users\\sterl\\OneDrive\\Desktop\\DEMO\\DEMO DEMO paracousti
   Where is your style_files folder? C:\\Users\\sterl\\OneDrive\\Desktop\\DEMO\\style_files


With the *ini files created, use the **Load GUI Inputs** button located at the bottom left of the SEAT GUI. For this demonstrationwe navigate to :file:`DEMO/DEMO DEMO paracousti/demo_paracousti_with_receptor.ini`, and click OK to load the inputs. If you need detailed instructions on how to load inputs, please refer to the :ref:`save_load_config` section in the :ref:`gui` documention. Loading  ``DEMO structured/demo_paracousti_with_receptor.ini`` the input should resemble the following with your local paths:

.. figure:: ../../media/PMEC_acoustics_input_receptor.webp
   :scale: 100 %
   :alt: PMEC Acoustics Receptor Input


Output
""""""""

For a given probability of occurrence of each wave condition the combined annual acoustic effects can be estimated. SEAT generates a similar stressor layer consisting of the difference between the acoustic effects with and without the array. With a provided receptor file which consists of information regarding the species, threshold value, weighting, and variable used, a threshold map is generated as a percentage of time (based on the probability distribution) that a threshold will be exceeded. For demonstration purposes, an artificially low threshold is used to generate the percent exceeded threshold figure below.


.. list-table:: 
   :widths: 50 50
   :class: image-matrix

   * - .. image:: ../../media/PMEC_acoustics_stressor_layers.webp
         :scale: 70 %
         :alt: Layers
         :align: center

       .. raw:: html

          <div style="text-align: center;">Layers Legend</div>

     - .. image:: ../../media/PMEC_acoustics_calculated_stressor.webp
         :scale: 25 %
         :alt: Calculated Stressor
         :align: center

       .. raw:: html

          <div style="text-align: center;">Calculated Stressor</div>

   * - .. image:: ../../media/PMEC_acoustics_calculated_paracousti.webp
         :scale: 25 %
         :alt: Calculated Paracousti
         :align: center

       .. raw:: html

          <div style="text-align: center;">Calculated Paracousti</div>

     - .. image:: ../../media/PMEC_acoustics_threshold_exceeded_receptor.webp
         :scale: 25 %
         :alt: Threshold Exceeded Receptor
         :align: center

       .. raw:: html

          <div style="text-align: center;">Threshold Exceeded Receptor</div>

**Output Files**

Additional output files can be found in the specifed Output folder

.. code-block::

    Output
    └───Acoustics_with_receptor
        calculated_paracousti.csv
        calculated_paracousti.tif
        calculated_stressor.csv
        calculated_stressor.tif
        threshold_exceeded_receptor.csv
        threshold_exceeded_receptor.tif
        _20231025.log
