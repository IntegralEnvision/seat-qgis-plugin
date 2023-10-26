import os
import csv
import argparse


def replace_path_in_csv(default_file, old_path, new_path):
    """
    Replace the old_path with new_path in the given default file and save as a csv file.
    """
    with open(default_file, 'r', newline='') as file:
        rows = file.readlines()

    # Modify the path in the default content
    for i, row in enumerate(rows):
        if old_path in row:
            rows[i] = row.replace(old_path, new_path)

    # Change the file extension to csv and write the modified content back
    csv_file = os.path.splitext(default_file)[0] + '.csv'
    with open(csv_file, 'w', newline='') as file:
        file.writelines(rows)


if __name__ == '__main__':
    dir_path = input(
        "Please enter the path to the directory containing default files: ")
    old_path = "<style_folder>"

    for filename in os.listdir(dir_path):
        if filename.endswith('.default'):
            full_file_path = os.path.join(dir_path, filename)
            replace_path_in_csv(full_file_path, old_path, dir_path)

    print(
        f"Paths in default files in directory {dir_path} have been updated and saved as CSV.")
