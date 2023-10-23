import os
import glob
import shutil
from datetime import datetime


def copy_most_recent_files(folder_path):
    # Step 2: Specify the naming conventions
    naming_convention = "*_Payment_Failures_*.csv"

    # Step 3: Navigate to the specific folder
    search_path = os.path.join(folder_path, naming_convention)
    files = sorted(glob.glob(search_path), key=os.path.getctime, reverse=True)

    if not files:
        print(f"No files found with the specified naming convention in {folder_path}.")
        return

    # Filter out the most recent 'Detail' and 'Summary' files
    most_recent_detail = None
    most_recent_summary = None
    for file in files:
        file_date = datetime.fromtimestamp(os.path.getctime(file)).date()
        if (
            "Detail" in file
            and not most_recent_detail
            and (file_date == today or not most_recent_detail)
        ):
            most_recent_detail = file
        elif (
            "Summary" in file
            and not most_recent_summary
            and (file_date == today or not most_recent_summary)
        ):
            most_recent_summary = file

        # Stop the loop if we've found both
        if most_recent_detail and most_recent_summary:
            break

    # Step 4: Copy the files to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    if most_recent_detail:
        shutil.copy(most_recent_detail, downloads_path)
        print(f"Copied {most_recent_detail} to {downloads_path}")

    if most_recent_summary:
        shutil.copy(most_recent_summary, downloads_path)
        print(f"Copied {most_recent_summary} to {downloads_path}")


# Define the folder paths
emea_folder = "/Volumes/digitalsubscriptions_prod/EMEA"
latam_folder = "/Volumes/digitalsubscriptions_prod/Latam_reports"

# Get today's date
today = datetime.now().date()

# Call the function for each folder
copy_most_recent_files(emea_folder)
copy_most_recent_files(latam_folder)
