import requests
from tafa.settings import API_URL, ORG_ID, TWIN_ID, ACCESS_TOKEN

HEADERS = {
    'X-Organization': ORG_ID,
    'X-Twin': TWIN_ID,
    'Content-Type': 'application/vnd.api+json',
    'Authorization': f"Token {ACCESS_TOKEN}"
}

def create_asset():
 
    response = requests.post(f"{API_URL}/assets/", headers=HEADERS)

    print(response.status_code)
    print(response.json())

    return response.json()["data"]

def update_asset(asset_id, attributes):
    new_data = {
        "data": {
            "type": "assets",
            "id": f"{asset_id}",
            "public": True,
            "attributes": {
                "attributes": attributes
            },
        }
    }
    print(new_data)

    response = requests.patch(f"{API_URL}/my/assets/{asset_id}", json=new_data, headers=HEADERS)

    print(response.status_code)
    print(response.json())

    return response.json()

def delete_asset(asset_id):

    response = requests.delete(f"{API_URL}/my/assets/{asset_id}", headers=HEADERS)
    print(response.status_code)
    print(response.json())
