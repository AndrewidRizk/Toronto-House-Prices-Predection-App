import requests
import time
import json

# Corrected list of communities
communities = [
    'Agincourt North', 'Agincourt South-Malvern West', 'Alderwood', 'Annex',
    'Banbury-Don Mills', 'Bathurst Manor', 'Bay Street Corridor',
    'Bayview Village', 'Bayview Woods-Steeles', 'Bedford Park-Nortown',
    'Beechborough-Greenbrook', 'Bendale', 'Birchcliffe-Cliffside', 'Black Creek',
    'Blake-Jones', 'Briar Hill-Belgravia', 'Bridle Path-Sunnybrook-York Mills',
    'Broadview North', 'Brookhaven-Amesbury', 'Cabbagetown-South St. James Town',
    'Caledonia-Fairbank', 'Casa Loma', 'Centennial Scarborough', 'Church-Yonge Corridor',
    'Clairlea-Birchmount', 'Clanton Park', 'Cliffcrest', 'Corso Italia-Davenport',
    'Crescent Town', 'Danforth', 'Danforth Village-East York', 'Don Valley Village',
    'Dorset Park', 'Dovercourt-Wallace Emerson-Junction', 'Downsview-Roding-CFB',
    'Dufferin Grove', 'East End-Danforth', 'East York', 'Edenbridge-Humber Valley',
    'Eglinton East', 'Elms-Old Rexdale', 'Englemount-Lawrence', 'Eringate-Centennial-West Deane',
    'Etobicoke West Mall', 'Flemingdon Park', 'Forest Hill North', 'Forest Hill South',
    'Glenfield-Jane Heights', 'Greenwood-Coxwell', 'Guildwood', 'Henry Farm',
    'High Park North', 'High Park-Swansea', 'Highland Creek', 'Hillcrest Village',
    'Humber Heights', 'Humber Summit', 'Humberlea-Pelmo Park W4', 'Humberlea-Pelmo Park W5',
    'Humbermede', 'Humewood-Cedarvale', 'Ionview', 'Islington-City Centre West',
    'Junction Area', 'Keelesdale-Eglinton West', 'Kennedy Park', 'Kensington-Chinatown',
    'Kingsview Village-The Westway', 'Kingsway South', "L'Amoreaux", 'Lambton Baby Point',
    'Lansing-Westgate', 'Lawrence Park North', 'Lawrence Park South', 'Leaside',
    'Little Portugal', 'Long Branch', 'Malvern', 'Maple Leaf', 'Markland Wood',
    'Milliken', 'Mimico', 'Morningside', 'Moss Park', 'Mount Dennis', 'Mount Olive-Silverstone-Jamestown',
    'Mount Pleasant East', 'Mount Pleasant West', 'New Toronto', 'Newtonbrook East',
    'Newtonbrook West', 'Niagara', 'North Riverdale', 'North St. James Town',
    "O'Connor-Parkview", 'Oakridge', 'Oakwood-Vaughan', 'Palmerston-Little Italy',
    'Parkwoods-Donalda', 'Playter Estates-Danforth', 'Pleasant View', 'Princess-Rosethorn',
    'Regent Park', 'Rexdale-Kipling', 'Rockcliffe-Smythe', 'Roncesvalles',
    'Rosedale-Moore Park', 'Rouge E10', 'Rouge E11', 'Runnymede-Bloor West Village',
    'Rustic', 'Scarborough Village', 'South Parkdale', 'South Riverdale',
    'St. Andrew-Windfields', 'Steeles', 'Stonegate-Queensway', "Tam O'Shanter-Sullivan",
    'The Beaches', 'Thistletown-Beaumonde Heights', 'Thorncliffe Park', 'Trinity-Bellwoods',
    'University', 'Victoria Village', 'Waterfront Communities C1', 'Waterfront Communities C8',
    'West Hill', 'West Humber-Clairville', 'Westminster-Branson', 'Weston',
    'Weston-Pellam Park', 'Wexford-Maryvale', 'Willowdale East', 'Willowdale West',
    'Willowridge-Martingrove-Richview', 'Woburn', 'Woodbine Corridor', 'Woodbine-Lumsden',
    'Wychwood', 'Yonge-Eglinton', 'Yonge-St. Clair', 'York University Heights',
    'Yorkdale-Glen Park'
]

# Base URL for Nominatim API
nominatim_url = "https://nominatim.openstreetmap.org/search"

# Function to fetch coordinates from Nominatim
def get_coordinates(location):
    # Add "Toronto" and "Canada" to the query for more accurate results
    query = f"{location}, Toronto, Canada"
    params = {'q': query, 'format': 'json', 'limit': 1}
    headers = {'User-Agent': 'YourAppName/1.0 (your-email@example.com)'}  # Add your User-Agent and contact info
    try:
        response = requests.get(nominatim_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        if len(data) > 0:
            return data[0]['lat'], data[0]['lon']
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {location}: {e}")
        return None, None

# Loop through communities and get coordinates
coordinates = {}
for community in communities:
    lat, lon = get_coordinates(community)
    if lat and lon:
        coordinates[community] = {'lat': lat, 'lng': lon}
        print(f"Found coordinates for {community}: {lat}, {lon}")
    else:
        print(f"Coordinates not found for {community}")
    time.sleep(3)  # Increase delay between requests to avoid rate limiting

# Save results to a JSON file
output_file = "community_coordinates.json"
with open(output_file, "w") as f:
    json.dump(coordinates, f, indent=4)

print(f"\nCoordinates saved to {output_file}")
