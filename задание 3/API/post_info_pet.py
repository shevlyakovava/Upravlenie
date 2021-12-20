import requests

post_new_pet_headers = {
    "auth_key": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "name": "Sharik",
    "animal_type": "Cat",
    "age": '3',
    "pet_photo": ""
}

post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('sharik.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))
