import data
import sender_stand_request



def get_new_user_token():

    # Создание новой переменной для поля user_body из data

    user_body = data.user_body

    # Получение регистрация пользователя через данные в sender_stand_request

    response_user = sender_stand_request.post_new_user(user_body)

    # Возврат ответа токена нового пользователя

    return response_user.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
#создание набора
    kit_body = get_kit_body(name)
    response_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

#проверить код ответа и имя в запросе
    assert response_kit.status_code == 201
    print()
    print(response_kit.status_code)
    assert response_kit.json()["name"] == kit_body["name"]


# Функция для негативной проверки
def negative_assert_code_400(name):
    kit_body=get_kit_body(name)
    resp = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert resp.status_code == 400

# Функция для негативной проверки, когда в ответе ошибка: Не передан параметр name
def negative_assert_delete_parametr():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")

    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "Не все необходимые параметры были переданы"



def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#В Постман тоже 201 код - не пройден
def test_create_kit_zero_letter_in_name_get_negative_response():
    negative_assert_code_400("")

#В Постман тоже 201 код - не пройден
def test_create_kit_512_letter_in_name_get_negative_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")

def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")

def test_create_kit_simbols_in_name_get_success_response():
    positive_assert("№%,")

def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("Человек и КО")

def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

#Переспросить у Алены
def test_create_kit_no_parameters_in_name_get_negative_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_delete_parametr()

#Переспросить у Алены
def test_create_kit_another_parameters_in_name_get_negative_response():
    kit_body=get_kit_body(123)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 400