# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csv_info, header, csvpath):
    """Saves the data in to a CSV file.

    Args:
        csv_info: A list to be added to the csv file.
        header: Adds headers for this data.
        csvpath: The name of the new file you wish to create.
    """
    csvpath = csvpath + ".csv"
    # Adding .csv to the end of the file name

    output_path = Path(csvpath)

    print("Writing this informaiton to a CSV file...")
    print()

    with open(output_path, "w", newline="") as csvfile:
    # newline="" to prevent 'them' inserting random blank lines

        csvwriter = csv.writer(csvfile, delimiter=",")
        # delimiter to put commas after each item.

        csvwriter.writerow(header)
        for line in csv_info:
            csvwriter.writerow(line)

    print(f"Your data has been saved to a CSV file({csvpath}).")