import pytest
import requests

# параметры

# post pet
post_simple_headers = {
    "auth_key": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "name": "Sharik",
    "animal_type": "Cat",
    "age": '1'
}
post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"

# get API key
get_key_headers = {
    "email": "shevlyakovava@gmail.com",
    "password": "shevlyakova"
}
get_key_params = get_key_headers
api_key_link = "https://petfriends1.herokuapp.com/api/key"

# get pet list
get_headers_my_pets = {
    "auth_key ": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "filter": "my_pets"
}
get_params_my_pets = get_headers_my_pets
my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"

# post info pet
post_new_pet_headers = {
    "auth_key": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "name": "Sharik",
    "animal_type": "Cat",
    "age": '2',
    "pet_photo": ""
}
post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"

# post set photo
post_set_photo_headers = {
    "auth_key": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "pet_id": "0eb0016c-3a17-443b-9f14-d85a97b20efc"
}
post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "0eb0016c-3a17-443b-9f14-d85a97b20efc"

# delete pet
delete_pet_headers = {
    "auth_key": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "pet_id": "0eb0016c-3a17-443b-9f14-d85a97b20efc"
}
delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "0eb0016c-3a17-443b-9f14-d85a97b20efc"

# put info
put_info_headers = {
    "auth_key": "a33271bdc13d918276a8c449d98a03c1b56da8458f382ce070466e48",
    "pet_id": "0eb0016c-3a17-443b-9f14-d85a97b20efc"
}
put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "0eb0016c-3a17-443b-9f14-d85a97b20efc"


# фикстуры
@pytest.fixture
def post_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )
    return response.ok


@pytest.fixture
def get_api_key(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        return True


@pytest.fixture
def post_info_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('sharik.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('sharik.jpg', 'rb')}
                             )
    return response.ok


@pytest.fixture
def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        return True


@pytest.fixture
def put_info():
    response = requests.put(put_info_link,
                            params=put_info_params,
                            headers=put_info_headers
                            )
    return response.ok


# тесты
@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # post_pet
                             (create_pet_simple_POST_link, post_simple_params, post_simple_headers, True),

                             # post_info_pet
                             (new_pet_POST_link, post_new_pet_params, post_new_pet_headers, False),

                             # post_set_photo
                             pytest.param(set_photo_POST_link, post_set_photo_params, post_set_photo_headers, True,
                                          marks=pytest.mark.xfail),
                         ]
                         )
def test_post(link, params, header, expected_result):
    response = requests.post(link,
                             params=params,
                             headers=header
                             )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [  # get_api_key
                             (api_key_link, get_key_params, get_key_headers, True),

                             # get_pets_list
                             (my_pets_link, get_params_my_pets, get_headers_my_pets, True)
                         ]
                         )
def test_get(link, params, header, expected_result):
    response = requests.get(link,
                            params=params,
                            headers=header
                            )
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (DELETE_pet_link, delete_pet_params, delete_pet_headers, True)
                         ]
                         )
def test_delete(link, params, header, expected_result):
    response = requests.delete(link,
                               params=params,
                               headers=header
                               )
    assert response.ok == expected_result


def test_put(put_info):
    assert put_info == True
