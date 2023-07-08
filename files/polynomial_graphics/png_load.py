


import requests
import zipfile
import io

zip_url = "http://localhost/1.zip"

response = requests.get(zip_url)

if response.status_code == 200:
    zip_content = io.BytesIO(response.content)
    with zipfile.ZipFile(zip_content, 'r') as zip_ref:
        zip_ref.extractall('destination_folder')
        print("ZIP file extracted successfully.")


