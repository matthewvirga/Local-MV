import os
import glob
import shutil
from datetime import datetime

def copy_most_recent_files_matching_criteria(folder_path, criteria):
    # Construct the search pattern for CSV files
    search_pattern = os.path.join(folder_path, "*.csv")

    # Find all CSV files in the folder
    all_files = sorted(glob.glob(search_pattern), key=os.path.getctime, reverse=True)

    if not all_files:
        print(f"No CSV files found in {folder_path}.")
        return

    # Dictionary to hold the most recent file for each criterion
    most_recent_files = {}

    # Find the most recent file for each criterion
    for file in all_files:
        for crit in criteria:
            if crit in file and crit not in most_recent_files:
                most_recent_files[crit] = file
                break  # Break the inner loop once a file is found for a criterion

    # Copy the most recent files to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    for file in most_recent_files.values():
        shutil.copy(file, downloads_path)
        print(f"Copied {file} to {downloads_path}")

# Define the folder paths and criteria
emea_folder = "/Volumes/digitalsubscriptions_prod/EMEA"
latam_folder = "/Volumes/digitalsubscriptions_prod/Latam_reports"
criteria = ["Extract","20231118"]  # Modify as needed

# Call the function for each folder with the specified criteria
copy_most_recent_files_matching_criteria(emea_folder, criteria)
# copy_most_recent_files_matching_criteria(latam_folder, criteria)
