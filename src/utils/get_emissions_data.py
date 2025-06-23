import requests


def get_emissions_data(year:int)->dict: 
    url = "https://api.climatetrace.org/v6/country/emissions"

    params = {
        "sectors": "power,transportation,buildings,fossil-fuel-operations,manufacturing,mineral-extraction,agriculture,waste,fluorinated-gases,forestry-and-land-use",
        "groups":'unfccc_nonannex1,unfccc_annex1',
        "since": year,
        "to": year
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        emissions_data = {
            country['country']: country['emissions']['co2']
            for country in response.json()
        } 
    else:
        print(f"Error {response.status_code}: {response.text}")
        
    return emissions_data


if __name__ == '__main__':
    print(len(get_emissions_data(2015)))