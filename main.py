import os
import shutil
import zipfile
from pathlib import Path


def process_csv_files(directory_path):
    """
    Process CSV files in the directory:
    - Find matching Chemistry2e.csv and Sample2e.csv pairs
    - Copy and rename header file for each pair
    - Zip them together
    """
    # Convert to Path object for easier handling
    dir_path = Path(directory_path)

    # Source header file
    source_header = "12-013-053-26W4M.AGAT.17E232483.Header.xml"
    source_header_path = dir_path / source_header

    # Check if source header exists
    if not source_header_path.exists():
        print(f"Error: Source header file '{source_header}' not found!")
        return

    # Find all Chemistry2e.csv files
    chemistry_files = list(dir_path.glob("*Chemistry2e.csv"))

    # Process each Chemistry file
    for chem_file in chemistry_files:
        # Extract the base name (everything before "Chemistry2e.csv")
        base_name = chem_file.name.replace("Chemistry2e.csv", "")

        # Look for matching Sample2e.csv file
        sample_file = dir_path / f"{base_name}Sample2e.csv"

        if sample_file.exists():
            # Create header file name
            header_file_name = f"{base_name}Header.xml"
            header_file_path = dir_path / header_file_name

            # Copy and rename header file
            shutil.copy2(source_header_path, header_file_path)
            print(f"Created header: {header_file_name}")

            # Create zip file name
            zip_file_name = f"{base_name}Archive.zip"
            zip_file_path = dir_path / zip_file_name

            # Create zip file with all three files
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Add Chemistry file
                zipf.write(chem_file, chem_file.name)
                # Add Sample file
                zipf.write(sample_file, sample_file.name)
                # Add Header file
                zipf.write(header_file_path, header_file_name)

            print(f"Created archive: {zip_file_name}")
            print(f"  - Contains: {chem_file.name}")
            print(f"  - Contains: {sample_file.name}")
            print(f"  - Contains: {header_file_name}")
            print()
        else:
            print(f"Warning: No matching Sample file for {chem_file.name}")


# Usage
directory = r"Y:\Gibson Energy\GB-04 Acheson terminal\soil data from McElhanney (June 11'25 email from Roger)\2016\2016 EDDs\2016 EDDs"  # Replace with your actual directory path
process_csv_files(directory)