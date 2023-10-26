.. _prepare_style_files:

Setting Up Style Files
======================

In the demo we have provided style files fou you to use. Before you can use them you need to place the full file path to the style files in the csv files. To do this you must replace ``<style_folder>`` with the path to the style_folder on your machine. For example if you have placed the style files in ``C:\Users\USER\Desktop\DEMO\style_files`` you would replace ``<style_folder>`` with ``C:\Users\USER\OneDrive\Desktop\DEMO\style_files``. There is a script provided to do this for you is you have python you can call `localize_style_path.py` from the command line. If you do not have python you can open the csv files in a text editor and replace ``<style_folder>`` with the path to the style_folder on your machine.

.. code-block:: bash
    :caption: localize_style_path.py

    python localize_style_files.py
    Please enter the path to the directory containing default files:
    C:\Users\sterl\OneDrive\Desktop\DEMO\style_files

    Paths in default files in directory C:\Users\sterl\OneDrive\Desktop\DEMO\style_files have been updated and saved as CSV.


The below shows the initial contents of the style_files folder. You will need to convert each of these to  csv files as described above to use them in the demo.

..  code-block:: none
    :caption: style_files Folder Contents

    DEMO
    └───style_files
        │   Acoustics_blue_whale.default
        │   Acoustics_fake_whale.default
        │   Shear_Stress - Structured.default
        │   Shear_Stress - Unstructured.default
        │   Velocity.default
        │
        └───Layer Style
                acoustics_density_demo.qml
                acoustics_percent_demo.qml
                acoustics_stressor_bluewhale.qml
                acoustics_stressor_demo.qml
                acoustics_threshold_demo.qml
                receptor_blues.qml
                shear_stress_continuous.qml
                shear_stress_continuous_unstructured.qml
                shear_stress_receptor_classified.qml
                shear_stress_receptor_continuous.qml
                shear_stress_reclass.qml
                velocity_continuous_stressor_vik.qml
                velocity_continuous_stressor_with_receptor.qml
                velocity_motility_classification_vik.qml
