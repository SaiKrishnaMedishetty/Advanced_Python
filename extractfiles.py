import zipfile
import os

def unzip_individual_file(zip_file, file_name, output_dir):
    """
    Extracts a specific file from the zip archive to the specified output directory.
    
    Parameters:
    zip_file (str): The path to the zip file.
    file_name (str): The name of the file to extract.
    output_dir (str): The directory where the file will be extracted.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        # Extract the specified file
        zipf.extract(file_name, output_dir)
    print(f"File '{file_name}' extracted to '{output_dir}'")

# Example usage
zip_file = 'path/to/your/archive.zip'  # Replace with the path to your zip file
file_name = 'file_to_extract.txt'  # Replace with the name of the file to extract
output_dir = 'path/to/output/directory'  # Replace with your desired extraction directory

# Extract the individual file
unzip_individual_file(zip_file, file_name, output_dir)
