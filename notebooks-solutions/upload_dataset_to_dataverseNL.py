import json
import sys
from pyDataverse.api import NativeApi
from pyDataverse.models import Datafile

def main():
    # Load configuration from JSON file
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print("config.json file not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error decoding config.json.")
        sys.exit(1)

    API_TOKEN = config.get('API_TOKEN')
    DATAVERSE = config.get('DATAVERSE')
    DOI = config.get('DOI')
    PATH_TO_FILE = config.get('PATH_TO_FILE')

    if not all([API_TOKEN, DATAVERSE, DOI, PATH_TO_FILE]):
        print("Configuration data missing in config.json.")
        sys.exit(1)

    # Initialize the API connection
    BASE_URL = DATAVERSE.split('/dataverse/')[0]
    api = NativeApi(BASE_URL, API_TOKEN)
    resp = api.get_info_version()
    if resp.json().get('status') == 'OK':
        print('Successful connection to DataverseNL API!!')
    else:
        print('Failed to connect to DataverseNL API.')
        sys.exit(1)

    # Upload the file to Dataverse
    df = Datafile()
    df.set({"pid": DOI, "filename": PATH_TO_FILE})
    resp = api.upload_datafile(DOI, PATH_TO_FILE)
    if resp.status_code == 200:
        print(f"File {PATH_TO_FILE} -> status: {resp.json()['status']}")
    else:
        print(f"Failed to upload {PATH_TO_FILE}. Error: {resp.content}")
        sys.exit(1)

if __name__ == "__main__":
    main()
