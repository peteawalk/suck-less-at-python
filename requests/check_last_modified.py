from datetime import datetime
from sys import argv
import requests

now = datetime.now()
mon_day_year = '%m/%d/%Y'
today = now.strftime(mon_day_year)
uri = str(argv[1])
param_validate = len(argv) # check if param passed to script

def check_last_modified(uri):
    try:
        response = requests.get(uri)

        if response.status_code == 200:
            headers = response.headers
            print(headers)
            server_timestamp = headers['last-modified']
            print(f'server timestamp: {server_timestamp}')

            date_format = '%a, %d %b %Y %H:%M:%S %Z' # Typical server_timestamp format
            server_timestamp_convert_date = datetime.strptime(server_timestamp, date_format) # converts string to date timestamp
            stringify_server_timestamp = server_timestamp_convert_date.strftime(mon_day_year)
            
            return stringify_server_timestamp
        
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if param_validate == 2:
    file_date = check_last_modified(uri)
    if today == file_date:
        print(f'Page data has been updated as of {now} at: {uri}')
    else:
        print(f'Page data has NOT been updated as of {now} at {uri}')
else:
    print('pass a URI to the script')
    SystemExit
