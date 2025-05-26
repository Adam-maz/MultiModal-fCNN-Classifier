"""
Maestro Schrodinger script allowing the user to take screenshots of compounds in the workspace and save them to a selected directory.
"""

#Name: Screenshots_capturing_script
#Command: pythonrun Screenshots_capturing_script.main

import os
import time
from pathlib import Path
import pandas as pd
import schrodinger.ui.qt.entryselector
from schrodinger.maestro import maestro

def main_logic(directory_path):
    entries_list = schrodinger.ui.qt.entryselector.get_entries()
    df = pd.DataFrame(entries_list)
    df_list = df[df.columns[0]].to_list()

    if not directory_path:
        print("No directory specified")
        return  

    pt = maestro.project_table_get()
    for entry in df_list:
        entry_path = Path(directory_path) / entry
        os.makedirs(entry_path, exist_ok=True)
        maestro.command(f'changedirectory "{entry_path}"')
        maestro.command(f'entrywsincludeonly entry {entry}')
        maestro.command(f'entryselectonly entry {entry}')

        for row in pt.selected_rows:
            name = row.property['s_m_title']
            new_path = Path(directory_path) / f"{name}_{entry}"
            
            
            time.sleep(1)
            
            try:
                os.rename(entry_path, new_path)
            except PermissionError:
                print(f"PermissionError: Failes to rename {entry_path} to {new_path}. Try closing other programs using this directory.")
                continue

        for i in range(1, 5):
            maestro.command("rotate y=90")
            maestro.command(f"saveimage image_{name}_{entry}_{i}.png")
        
        for i in range(5, 8):
            maestro.command("rotate x=90")
            maestro.command(f"saveimage image_{name}_{entry}_{i}.png")
        
        maestro.command("rotate x=90")

def main():
    directory_path = "path_to_directory_for_screenshots"  
    main_logic(directory_path)

main()

