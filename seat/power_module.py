# power_module.py
# Copyright 2023, Integral Consulting Inc. All rights reserved.
#
# PURPOSE: Calculate power output from device array
#
# PROJECT INFORMATION:
# Name: Marine Renewable Energy Assessment
# Number:C1308
#
# AUTHORS (Authors to use initals in history)
#  Timothy R. Nelson - tnelson@integral-corp.com
# NOTES (Data descriptions and any script specific notes)
# 1. .OUT files and .pol must be in the same folder
# 2. .OUT file is format sensitive
#
# Date		  Author                Remarks
# ----------- --------------------- --------------------------------------------
# 2022-08-01  TRN - File created
# 2023-08-05  TRN - Comments and slight edits
# ===============================================================================

import pandas as pd
import io
import re
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import ListedColormap
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import FormatStrFormatter

# %% Obstacle Polygon and Device Positions


def read_obstacle_polygon_file(power_device_configuration_file):
    """
    reads the obstacle polygon file

    Parameters
    ----------
    power_device_configuration_file : str
        filepath of .pol file.

    Returns
    -------
    Obstacles : Dict
        xy of each obstacle.

    """
    inf = io.open(power_device_configuration_file, "r")
    lines = inf.readlines()
    ic = 0
    Obstacles = {}
    while ic < len(lines)-1:
        if lines[ic].find('Obstacle') >= 0:
            # print(lines[ic])
            obstacle = lines[ic].strip()
            Obstacles[obstacle] = {}
            ic += 1  # skip to next line
            nrows, ncols = [int(i) for i in lines[ic].split()]
            ic += 1  # skip to next line
            x = []
            y = []
            for n in range(nrows):  # read polygon
                xi, yi = [float(i) for i in lines[ic].split()]
                x = np.append(x, xi)
                y = np.append(y, yi)
                ic += 1  # skip to next line
            Obstacles[obstacle] = np.vstack((x, y)).T
        else:
            ic += 1
    return Obstacles


def find_mean_point_of_obstacle_polygon(Obstacles):
    """
    claculates the center of each obstacle

    Parameters
    ----------
    Obstacles : Dict
        xy of each obstacle.

    Returns
    -------
    Centroids : array
        centroid of each obstacle.

    """
    Centroids = np.empty((0, 3), dtype=int)
    for ic, obstacle in enumerate(Obstacles.keys()):
        Centroids = np.vstack((Centroids, [ic, np.nanmean(
            Obstacles[obstacle][:, 0]), np.nanmean(Obstacles[obstacle][:, 1])]))
    return Centroids


def plot_test_obstacle_locations(Obstacles):
    """
    Creates a plot of the spatial distribution and location of each obstacle.

    Parameters
    ----------
    Obstacles : Dict
        xy of each obstacle.

    Returns
    -------
    fig : pyplot figure handle
        pyplot figure handle.

    """
    fig, ax = plt.subplots(figsize=(10, 10))
    for ic, obstacle in enumerate(Obstacles.keys()):
        ax.plot(Obstacles[obstacle][:, 0], Obstacles[obstacle]
                [:, 1], '.', markersize=3, alpha=0)
        ax.text(Obstacles[obstacle][0, 0], Obstacles[obstacle]
                [0, 1], f'{obstacle}', fontsize=8)
        ax.text(Obstacles[obstacle][1, 0], Obstacles[obstacle]
                [1, 1], f'{obstacle}', fontsize=8)
    fig.tight_layout()
    return fig


def centroid_diffs(Centroids, centroid):
    """
    Determines the closest centroid pair

    Parameters
    ----------
    Centroids : Dict
        DESCRIPTION.
    centroid : array
        single x,y.

    Returns
    -------
    pair : list
        index of closest centroid.

    """

    diff = Centroids[:, 1:] - centroid[1:]
    min_arg = np.nanargmin(np.abs(diff[:, -1]-diff[:, 0]))
    pair = [int(centroid[0]), int(Centroids[min_arg, 0])]
    return pair


def extract_device_location(Obstacles, Device_index):
    """
    Creates a dictionary summary of each device location

    Parameters
    ----------
    Obstacles : TYPE
        DESCRIPTION.
    Device_index : TYPE
        DESCRIPTION.

    Returns
    -------
    Devices_DF : TYPE
        DESCRIPTION.

    """
    Devices = {}
    for device, [ix1, ix2] in enumerate(Device_index):
        key = f'{device+1:03.0f}'
        Devices[key] = {}
        xy = Obstacles[f'Obstacle {ix1+1}']
        xy = np.vstack((xy, Obstacles[f'Obstacle {ix2+1}']))
        # create polygon from bottom left to upper right assuming rectangular
        x = xy[:, 0]
        y = xy[:, 1]
        Devices[key]['polyx'] = [
            np.nanmin(x), np.nanmin(x), np.nanmax(x), np.nanmax(x)]
        Devices[key]['polyy'] = [
            np.nanmin(y), np.nanmax(y), np.nanmax(y), np.nanmin(y)]
        Devices[key]['lower_left'] = [np.nanmin(x), np.nanmin(y)]
        Devices[key]['centroid'] = [np.nanmean(x), np.nanmean(y)]
        Devices[key]['width'] = (np.nanmax(x) - np.nanmin(x))
        Devices[key]['height'] = (np.nanmax(y) - np.nanmin(y))
    Devices_DF = pd.DataFrame.from_dict(Devices, orient='index')
    return Devices_DF


def pair_devices(Centroids):
    """
    Determins the two intersecting obstacles to that create a device.

    Parameters
    ----------
    Centroids : TYPE
        DESCRIPTION.

    Returns
    -------
    Devices : TYPE
        DESCRIPTION.

    """
    Devices = np.empty((0, 2), dtype=int)
    while len(Centroids) > 0:
        # print(Centroids)
        # must have dimensions M,N with each M [index, x , y]
        pair = centroid_diffs(Centroids[1:, :], Centroids[0, :])
        Devices = np.vstack((Devices, pair))
        Centroids = Centroids[~np.isin(Centroids[:, 0], pair), :]
    return Devices

# # use https://stackoverflow.com/questions/10550477/how-do-i-set-color-to-rectangle-in-matplotlib
# # to create rectangles from the polygons above
# # scale color based on power device power range from 0 to max of array
# # This way the plot is array and grid independent, only based on centroid and device size, could make size variable if necessary.
#


def create_power_heatmap(DEVICE_POWER, crs=None):
    """
    Creates a heatmap of device location and power as cvalue.

    Parameters
    ----------
    DEVICE_POWER : dataframe
        DEVICE_POWER dataframe.
    crs : int
        Coordinate Reverence Systems EPSG number

    Returns
    -------
    fig : matplotlib figure handle
        matplotlib figure handle.

    """
    adjust_x = -360 if crs == 4326 else 0

    fig, ax = plt.subplots(figsize=(6, 4))
    lowerx = np.inf
    lowery = np.inf
    upperx = -np.inf
    uppery = -np.inf
    # cmap = ListedColormap(plt.get_cmap('Greens')(np.linspace(0.1, 1, 256)))  # skip too light colors
    cmap = ListedColormap(plt.get_cmap('turbo')(
        np.linspace(0.1, 1, 256)))  # skip too light colors
    # norm = plt.Normalize(DEVICE_POWER['Power [W]'].min(), DEVICE_POWER['Power [W]'].max())
    norm = plt.Normalize(
        0.9*DEVICE_POWER['Power [W]'].min()*1e-6, DEVICE_POWER['Power [W]'].max()*1e-6)
    for device_number, device in DEVICE_POWER.iterrows():
        # print(device)
        ax.add_patch(
            Rectangle((device.lower_left[0]+adjust_x, device.lower_left[1]),
                      np.nanmax([device.width, device.height]),
                      np.nanmax([device.width, device.height]),
                      color=cmap(norm(device['Power [W]']*1e-6))))
        lowerx = np.nanmin([lowerx, device.lower_left[0]+adjust_x])
        lowery = np.nanmin([lowery, device.lower_left[1]])
        upperx = np.nanmax(
            [upperx, device.lower_left[0]+adjust_x + device.width])
        uppery = np.nanmax([uppery, device.lower_left[1] + device.height])
    xr = np.abs(np.max([lowerx, upperx]) - np.min([lowerx, upperx]))
    yr = np.abs(np.max([lowery, uppery]) - np.min([lowery, uppery]))
    ax.set_xlim([lowerx-.05*xr, upperx+.05*xr])
    ax.set_ylim([lowery-.05*yr, uppery+.05*yr])

    cb = plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), ax=ax)
    cb.set_label('MW')
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.set_xlabel('Longitude [deg]')
    ax.set_ylabel('Latitude [deg]')
    ax.set_xticks(np.linspace(lowerx, upperx, 5))
    ax.set_xticklabels(ax.get_xticklabels(), ha="right", rotation=45)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%0.4f'))
    fig.tight_layout()
    return fig
# %%


def read_power_file(datafile):
    """
    Read power file and extract final set of converged data

    Parameters
    ----------
    datafile : file path
        path and file name of power file.

    Returns
    -------
    Power : 1D Numpy Array [m]
        Individual data files for each observation [m].
    Total_Power : Scalar
        Total power from all observations.

    """
    inf = io.open(datafile, "r")  # Read datafile
    for line in inf:  # iterate through each line
        if re.match('Iteration:', line):
            Power = []  # If a new iteration is found, initalize varialbe or overwrite existing iteration
        else:  # data
            # extract float variable from line
            power = float(line.split('=')[-1].split('W')[0].strip())
            Power = np.append(Power, power)  # append data for each observation
    Total_Power = np.nansum(Power)  # Total power from all observations
    return Power, Total_Power


def sort_data_files_by_runnumber(bc_data, datafiles):
    bc_data_sorted = sort_bc_data_by_runnumber(bc_data.copy())
    return [datafiles[i] for i in bc_data_sorted.original_order.to_numpy()]


def sort_bc_data_by_runnumber(bc_data):
    bc_data['original_order'] = range(0, len(bc_data))
    return bc_data.sort_values(by='run number')


def reset_bc_data_order(bc_data):
    if np.isin('original_order', bc_data.columns):
        bc_data = bc_data.sort()


def roundup(x, base=5):
    return base * round(x/base)


def calculate_power(power_files, probabilities_file, save_path=None, crs=None):
    """
    Reads the power files and calculates the total annual power based on hydrdynamic probabilities in probabilities_file. Data are saved as a csv files.
    Three files are output:
        1) Total Power among all devices for each hydrodynamic conditions BC_probability_Annual_SETS_wPower.csv
        2) Power per device per hydordynamic scenario. Power_per_device_per_scenario.csv
        3) Total power per device during a year, scaled by $ of year in probabilities_file

    Parameters
    ----------
    fpath : file path
        Path to bc_file and power output files.
    probabilities_file : file name
        probabilities file name with extension.
    save_path: file path
        save directory 

    Returns
    -------
    Devices : Dataframe
        Scaled power per device per condition.
    Devices_total : Dataframe
        Total annual power per device.

    """
    datafiles_o = [s for s in os.listdir(power_files) if s.endswith('.OUT')]
    bc_data = pd.read_csv(probabilities_file)
    datafiles = sort_data_files_by_runnumber(bc_data, datafiles_o)

    assert save_path is not None, "Specify an output directory"
    os.makedirs(save_path, exist_ok=True)

    Total_Power = []
    ic = 0
    for datafile in datafiles:
        p, tp = read_power_file(os.path.join(power_files, datafile))
        # print(p)
        if ic == 0:
            Power = np.empty((len(p), 0), float)
        Power = np.append(Power, p[:, np.newaxis], axis=1)
        Total_Power = np.append(Total_Power, tp)
        ic += 1

    Power_Scaled = bc_data['% of yr'].to_numpy() * Power
    Total_Power_Scaled = bc_data['% of yr'] * Total_Power

    # Summary of power given percent of year for each array
    # need to reorder Total_Power and Power to run roder in
    bc_data['Power_Run_Name'] = datafiles
    # bc_data['% of yr'] * Total_Power
    bc_data['Power [W]'] = Total_Power_Scaled
    bc_data.to_csv(os.path.join(
        save_path, 'BC_probability_wPower.csv'), index=False)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.bar(np.arange(np.shape(Total_Power_Scaled)[
           0])+1, np.log10(Total_Power_Scaled), width=1, edgecolor='black')
    ax.set_xlabel('Run Scenario')
    ax.set_ylabel('Power [$log_{10}(Watts)$]')
    ax.set_title('Total Power Annual')
    fig.tight_layout()
    fig.savefig(os.path.join(
        save_path, 'Total_Scaled_Power_Bars_per_Run.png'))

    foo = np.sqrt(np.shape(Power_Scaled)[1])
    fig, AX = plt.subplots(np.round(foo).astype(int), np.ceil(
        foo).astype(int), sharex=True, sharey=True, figsize=(12, 10))
    nr, nc = AX.shape
    AX = AX.flatten()
#    mxy = roundup(np.log10(Power_Scaled.max().max())) + 5
    mxy = roundup(np.log10(Power_Scaled.max().max()), 2)
    ndx = np.ceil(Power_Scaled.shape[0]/6)
    for ic in range(Power_Scaled.shape[1]):
        # fig,ax = plt.subplots()
        AX[ic].bar(np.arange(np.shape(Power_Scaled)[0])+1,
                   np.log10(Power_Scaled[:, ic]), width=1, edgecolor='black')
#        AX[ic].text(Power_Scaled.shape[0]/2, mxy-1, f'{datafiles[ic]}', fontsize=8, ha='center', va='top')
        AX[ic].set_title(f'{datafiles[ic]}', fontsize=8)
        AX[ic].set_ylim([0, mxy])
        AX[ic].set_xticks(np.arange(0, Power_Scaled.shape[0]+ndx, ndx))
        AX[ic].set_xlim([0, Power_Scaled.shape[0]+1])
    AX = AX.reshape(nr, nc)
    for ax in AX[:, 0]:
        ax. set_ylabel('Power [$log_{10}(Watts)$]')
    for ax in AX[-1, :]:
        ax.set_xlabel('Obstacle')
    fig.tight_layout()
    fig.savefig(os.path.join(
        save_path, 'Scaled_Power_Bars_per_run_obstacle.png'))

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.bar(np.arange(np.shape(Power_Scaled)[
           0])+1, np.log10(np.sum(Power_Scaled, axis=1)), width=1, edgecolor='black')
    ax.set_xlabel('Obstacle')
    ax.set_ylabel('Power [$log_{10}(Watts)$]')
    ax.set_title('Total Obstacle Power for all Runs')
    fig.tight_layout()
    fig.savefig(os.path.join(
        save_path, 'Total_Scaled_Power_Bars_per_obstacle.png'))

    power_device_configuration_file = [s for s in os.listdir(power_files) if (
        s.endswith('.pol') | s.endswith('.Pol') | s.endswith('.POL'))]
    if len(power_device_configuration_file) > 0:

        assert len(
            power_device_configuration_file) == 1, "More than 1 *.pol file found"

        # Group arrays to devices and calculate power proportionally for each scenario (datafile), such that the sum of each scenario for each device is the yearly totoal power for that device
        Obstacles = read_obstacle_polygon_file(os.path.join(
            power_files, power_device_configuration_file[0]))
        fig = plot_test_obstacle_locations(Obstacles)
        fig.savefig(os.path.join(save_path, 'Obstacle_Locations.png'))

        Centroids = find_mean_point_of_obstacle_polygon(Obstacles)
        Centroids_DF = pd.DataFrame(
            data=Centroids, columns=['obstacle', 'X', 'Y'])
        Centroids_DF['obstacle'] = Centroids_DF['obstacle'].astype(int)
        Centroids_DF = Centroids_DF.set_index(['obstacle'])
        Device_index = pair_devices(Centroids)
        DeviceindexDF = pd.DataFrame({'Device_Number': range(Device_index.shape[0]),
                                      'Index 1': Device_index[:, 0],
                                      'Index 2': Device_index[:, 1],
                                      'X': Centroids_DF.loc[Device_index[:, 0], 'X'],
                                      'Y': Centroids_DF.loc[Device_index[:, 0], 'Y']})
        DeviceindexDF['Device_Number'] = DeviceindexDF['Device_Number']+1
        DeviceindexDF = DeviceindexDF.set_index('Device_Number')
        DeviceindexDF.to_csv(os.path.join(save_path, 'Obstacle_Matching.csv'))

        fig, ax = plt.subplots(figsize=(10, 10))
        for device in DeviceindexDF.index.values:
            ax.plot(DeviceindexDF.loc[device, 'X'],
                    DeviceindexDF.loc[device, 'Y'], '.', alpha=0)
            ax.text(DeviceindexDF.loc[device, 'X'],
                    DeviceindexDF.loc[device, 'Y'], device, fontsize=8)
        fig.savefig(os.path.join(save_path, 'Device Number Location.png'))

        device_power = np.empty((0, np.shape(Power)[1]), dtype=float)
        for ic0, ic1 in Device_index:
            device_power = np.vstack(
                (device_power, Power[ic0, :] + Power[ic1, :]))

        # device_power = Power[0::2, :] + Power[1::2, :]

        Devices = pd.DataFrame({})
        device_power_year = device_power * bc_data['% of yr'].to_numpy()
        for ic, name in enumerate(datafiles):
            Devices[name] = device_power_year[:, ic]
        Devices['Device'] = np.arange(1, len(Devices)+1)
        Devices = Devices.set_index('Device')
        Devices.to_csv(os.path.join(
            save_path, 'Power_per_device_per_scenario.csv'))

        foo = np.sqrt(Devices.shape[1])
        fig, AX = plt.subplots(np.round(foo).astype(int), np.ceil(
            foo).astype(int), sharex=True, sharey=True, figsize=(12, 10))
        nr, nc = AX.shape
        AX = AX.flatten()
#        mxy = roundup(np.log10(Devices.max().max())) + 5
        mxy = roundup(np.log10(Devices.max().max()), 2)
        ndx = np.ceil(Devices.shape[0]/6)
        for ic, col in enumerate(Devices.columns):
            # fig,ax = plt.subplots()
            AX[ic].bar(np.arange(np.shape(Devices[col])[0])+1,
                       np.log10(Devices[col].to_numpy()), width=1.0, edgecolor='black')
#            AX[ic].text(Devices.shape[0]/2, mxy-1, f'{col}', fontsize=8, ha='center', va='top')
            AX[ic].set_title(f'{col}', fontsize=8)
            AX[ic].set_ylim([0, mxy])
            AX[ic].set_xticks(np.arange(0, Devices.shape[0]+ndx, ndx))
            AX[ic].set_xlim([0, Devices.shape[0]+1])
        AX = AX.reshape(nr, nc)
        for ax in AX[:, 0]:
            ax. set_ylabel('Power [$log_{10}(Watts)$]')
        for ax in AX[-1, :]:
            ax.set_xlabel('Device')
        AX = AX.flatten()
        fig.tight_layout()
        fig.savefig(os.path.join(
            save_path, 'Scaled_Power_per_device_per_scenario.png'))

        # power per scenario per device

        # Sum power for the entire years (all datafiles) for each device
        Devices_total = pd.DataFrame({})
        Devices_total['Power [W]'] = device_power_year.sum(axis=1)
        Devices_total['Device'] = np.arange(1, len(Devices_total)+1)
        Devices_total = Devices_total.set_index('Device')
        Devices_total.to_csv(os.path.join(
            save_path, 'Power_per_device_annual.csv'))

        fig, ax = plt.subplots(figsize=(9, 6))
        ax.bar(Devices_total.index, np.log10(
            Devices_total['Power [W]']), width=1, edgecolor='black')
        ax. set_ylabel('Power [$log_{10}(Watts)$]')
        ax.set_xlabel('Device')
        fig.savefig(os.path.join(
            save_path, 'Total_Scaled_Power_per_Device_.png'))

        DEVICE_POWER = extract_device_location(Obstacles, Device_index)
        DEVICE_POWER['Power [W]'] = Devices_total['Power [W]'].values
        fig = create_power_heatmap(DEVICE_POWER, crs=crs)
        fig.savefig(os.path.join(save_path, 'Device_Power.png'), dpi=150)
        # plt.close(fig)
    return None
