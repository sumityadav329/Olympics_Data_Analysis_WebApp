import os
import gdown
import zipfile

def download_and_extract_zip(file_id, file_name, data_dir='data'):
    """
    Downloads a ZIP file from Google Drive and extracts its contents to a specified directory.

    Parameters:
    - file_id: str, Google Drive file ID
    - file_name: str, the name to save the downloaded ZIP file as
    - data_dir: str, the directory to save the downloaded and extracted files
    """
    # Google Drive URL
    drive_url = f'https://drive.google.com/uc?id={file_id}'

    # Create the directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Full path to save the downloaded ZIP file
    zip_path = os.path.join(data_dir, file_name)

    # Download the ZIP file from Google Drive
    gdown.download(drive_url, zip_path, quiet=False)

    # Unzip the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)

    # Delete the ZIP file after extracting its contents
    os.remove(zip_path)

    print(f'Files extracted to {data_dir} and ZIP file deleted.')


