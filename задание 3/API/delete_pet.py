import requests

delete_pet_headers = {
    "auth_key": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "pet_id": "0eb0016c-3a17-443b-9f14-d85a97b20efc"
}

delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "0eb0016c-3a17-443b-9f14-d85a97b20efc"


def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(delete_pet(DELETE_pet_link, delete_pet_params, delete_pet_headers))
