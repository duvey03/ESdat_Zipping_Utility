# CSV File Organizer Script

## Overview

This Python script automates the organization and archiving of CSV files and their associated header files. It processes pairs of related CSV files (Chemistry and Sample files), creates appropriate header files for each pair, and packages them together into ZIP archives.

## Purpose

The script addresses a specific file organization need where:
- Multiple CSV files exist in a directory with specific naming patterns
- Files come in pairs: one "Chemistry2e.csv" file and one "Sample2e.csv" file
- Each pair needs to be archived together with a properly named header file
- A template header file exists that needs to be copied and renamed for each pair

## How It Works

### 1. File Detection
The script scans the specified directory for all files ending with `Chemistry2e.csv`. For each Chemistry file found, it extracts the base filename (everything before "Chemistry2e.csv") and looks for a matching Sample file with the same base name.

### 2. Header File Creation
For each matched pair, the script:
- Copies an existing header template file (`12-013-053-26W4M.AGAT.17E232483.Header.xml`)
- Renames the copy to match the naming pattern of the CSV pair
- Places the renamed header file in the same directory

### 3. Archive Creation
The script creates a ZIP archive for each file set containing:
- The Chemistry CSV file
- The Sample CSV file  
- The newly created header XML file

## File Naming Convention

Given files like:
```
25110069300.12-13-053-26W4M.AGAT.17E275662.Chemistry2e.csv
25110069300.12-13-053-26W4M.AGAT.17E275662.Sample2e.csv
```

The script will:
1. Create a header file: `25110069300.12-13-053-26W4M.AGAT.17E275662.Header.xml`
2. Create an archive: `25110069300.12-13-053-26W4M.AGAT.17E275662.Archive.zip`

## Requirements

- Python 3.6 or higher
- Standard Python libraries (no external dependencies):
  - `os` - Operating system interface
  - `shutil` - File operations
  - `zipfile` - ZIP archive creation
  - `pathlib` - Path manipulation

## Usage

### Basic Usage

1. Place the script in any location on your computer
2. Update the `directory` variable in the script to point to your target directory:
   ```python
   directory = r"C:\path\to\your\directory"
   ```
3. Run the script:
   ```bash
   python organize_files.py
   ```

### Example

```python
# Set your directory path
directory = r"C:\Users\YourName\Documents\CSVFiles"
process_csv_files(directory)
```

## Script Output

The script provides console output to track its progress:

```
Created header: 25110069300.12-13-053-26W4M.AGAT.17E275662.Header.xml
Created archive: 25110069300.12-13-053-26W4M.AGAT.17E275662.Archive.zip
  - Contains: 25110069300.12-13-053-26W4M.AGAT.17E275662.Chemistry2e.csv
  - Contains: 25110069300.12-13-053-26W4M.AGAT.17E275662.Sample2e.csv
  - Contains: 25110069300.12-13-053-26W4M.AGAT.17E275662.Header.xml
```

## Error Handling

The script includes basic error handling for:
- Missing source header file
- Unmatched CSV files (Chemistry files without corresponding Sample files)

Error messages will appear in the console:
```
Error: Source header file '12-013-053-26W4M.AGAT.17E232483.Header.xml' not found!
Warning: No matching Sample file for [filename]
```

## File Structure

### Before Running Script
```
Directory/
├── 12-013-053-26W4M.AGAT.17E232483.Header.xml (template)
├── 25110069300.12-13-053-26W4M.AGAT.17E275662.Chemistry2e.csv
├── 25110069300.12-13-053-26W4M.AGAT.17E275662.Sample2e.csv
├── [additional CSV pairs...]
```

### After Running Script
```
Directory/
├── 12-013-053-26W4M.AGAT.17E232483.Header.xml (template - unchanged)
├── 25110069300.12-13-053-26W4M.AGAT.17E275662.Chemistry2e.csv
├── 25110069300.12-13-053-26W4M.AGAT.17E275662.Sample2e.csv
├── 25110069300.12-13-053-26W4M.AGAT.17E275662.Header.xml (created)
├── 25110069300.12-13-053-26W4M.AGAT.17E275662.Archive.zip (created)
├── [additional files and archives...]
```

## Important Notes

1. **Non-destructive**: The script does not delete or modify original files
2. **Overwrites**: If header files or archives already exist with the same names, they will be overwritten
3. **Case-sensitive**: File matching is case-sensitive on Unix-like systems
4. **Template Required**: The template header file must exist in the directory before running

## Customization

To adapt the script for different file patterns, modify these elements:

1. **File patterns**: Change `"Chemistry2e.csv"` and `"Sample2e.csv"` to match your naming convention
2. **Header template**: Update the `source_header` variable to use a different template file
3. **Archive name**: Modify the `zip_file_name` construction to use a different naming pattern

## Troubleshooting

### Common Issues

1. **"Source header file not found"**
   - Ensure the template header file exists in the directory
   - Check the filename matches exactly (including extension)

2. **"No matching Sample file"**
   - Verify both Chemistry and Sample files exist for each set
   - Check that filenames match exactly (case-sensitive)

3. **Permission errors**
   - Ensure you have read/write permissions for the directory
   - Close any files that might be open in other programs

### Debug Mode

To see more detailed information about what files are being processed, you can add debug prints:

```python
# Add after finding chemistry_files
print(f"Found {len(chemistry_files)} Chemistry files")
for f in chemistry_files:
    print(f"  - {f.name}")
```

## License

This script is provided as-is for file organization purposes. Feel free to modify and distribute as needed for your use case.