"""
Maestro Schrodinger script which enables user to select desired conformers based on their Entry ID.
"""

#Name: Entry_selector
#Command: pythonrun Entry_selector.main

import pandas as pd
from schrodinger.maestro import maestro


def main():

    entries = pd.read_csv('path_to_csv_file_with_entries_id/docking_entries_id.csv') #this script is universal both for docking and DFT optimization files
    df = pd.DataFrame(entries)
    col = df.columns[0]

    pt = maestro.project_table_get()
    for entry in df[col]:
        maestro.command(f'entryselect entry {entry}')


main()
