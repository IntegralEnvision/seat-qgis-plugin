Larval Transport Analysis (Velocity)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of inputs evaluates the impact on larval motility given a single critical velocity receptor in a CSV file.

Input
""""""
At this point you should have already setup the input files as detailed in :ref:`preparing_input_files`. To run this demonstration, use the **Load GUI Inputs** button located at the bottom left of the SEAT GUI, navigate to :file:`DEMO unstructured/velocity_with_receptor_demo.ini`, and click OK to load the inputs. If you need detailed instructions on how to load inputs, please refer to the :ref:`save_load_config` section in the :ref:`gui` documention.

"DEMO unstructured/velocity_with_receptor_demo.ini"

Refer to :ref:`unstructured_files` for details on the model data which consists of individual .nc files for each flow return period. The period within the .nc filename determines the probability of occurrence.

.. Important::
   Ensure to reset the complete path to match the location on your machine. Your paths will be different than the ones shown in the example below.

.. figure:: ../../media/tanana_velocity_with_receptor_input.webp
   :scale: 100 %
   :alt: Tanana sedimentation example input

Output
""""""
  
For this case the velocity with devices is compared to the velocity without devices and a difference (stressor) is calculated.


.. list-table:: 
   :widths: 50 50
   :class: image-matrix

   * - .. image:: ../../media/tanana_velocity_layers.webp
         :scale: 70 %
         :alt: Layers
         :align: center

       .. raw:: html

          <div style="text-align: center;">Layers Legend</div>

     - .. image:: ../../media/tanana_velocity_stressor_reclassified.webp
         :scale: 25 %
         :alt: Calculated Stressor Reclassified
         :align: center

       .. raw:: html

          <div style="text-align: center;">Calculated Stressor Reclassified</div>

   * - .. image:: ../../media/tanana_velocity_stressor_with_receptor.webp
         :scale: 25 %
         :alt: Stressor with Receptor
         :align: center

       .. raw:: html

          <div style="text-align: center;">Stressor with Receptor</div>

     - .. image:: ../../media/tanana_velocity_stressor.webp
         :scale: 25 %
         :alt: Calculated Stressor
         :align: center

       .. raw:: html

          <div style="text-align: center;">Calculated Stressor</div>

**Output Files**

Additional output files can be found in the specifed Output folder.

.. code-block::

    Output
    └───Velocity_with_Receptor
            calcualted_velocity_without_devices.tif
            calcualted_velocity_with_devices.tif
            calculated_stressor.csv
            calculated_stressor.tif
            calculated_stressor_at_receptor.csv
            calculated_stressor_reclassified.csv
            calculated_stressor_reclassified.tif
            calculated_stressor_reclassified_at_receptor.csv
            calculated_stressor_with_receptor.csv
            calculated_stressor_with_receptor.tif
            receptor.tif
            _20231025.log      