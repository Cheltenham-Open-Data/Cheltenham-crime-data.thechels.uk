# import
from requests import get
import json
import pathlib
import os

lat1 = "51.9042"
lon1 = "-2.10141"
append = f"lat={lat1}&lng={lon1}"
endpoint1 = f"https://data.police.uk/api/crimes-street/stops-street?{append}"
endpoint2 = f"https://data.police.uk/api/crimes-street/all-crime?{append}"

def get_data(endpoint):
    print(endpoint)
    response = get(endpoint, timeout=20)
    if response.status_code >= 400:
        print(response.status_code)
        print(f"Request failed: { response.text }")
    return response.json()

# output
if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.parent.resolve()
    with open( root / "data/AA3_all_crime.json", 'r+') as filehandle:
        data = json.load(filehandle)
        new_data = get_data(endpoint1)
        filehandle.seek(0)
        json.dump(new_data, filehandle, indent=4)
