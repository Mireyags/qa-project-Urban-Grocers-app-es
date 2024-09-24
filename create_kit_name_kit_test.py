import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name

def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

def positive_assert(kit):
    kit_body = get_kit_body(kit)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["auth_Token"] != ""



def negative_assert_code_400(kit):
    kit_body = get_kit_body(kit)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. "\
                                          "El nombre supera los caracteres permitidos, "\
                                          "El nombre debe tener al menos 1 caracter"

def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["message"] == "El número de caracteres es menor que la cantidad permitida"

# Pruebas
def test_create_1_letter_in_name_kit_body():
    positive_assert("a")

def test_create_511_letter_in_name_kit_body():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_name_empty_in_kit_body():
    kit_body = get_kit_body("")
    negative_assert_no_name(kit_body)

def test_create_512_letter_in_name_kit_body():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_special_symbol_in_name_kit_body():
    positive_assert("\"№%@\",")

def test_create_kit_name_use_space_in_name_kit_body():
    positive_assert("A Aaa ")

def test_create_kit_name_use_numbers_in_name_kit_body():
    positive_assert("123")

def test_create_kit_no_name_param():
    negative_assert_code_400({})

def test_create_use_number_type_in_name_kit_body():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

def test_create_no_name_in_kit_body():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)