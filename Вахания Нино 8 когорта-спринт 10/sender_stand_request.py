import configuration
import requests
import data


#Запрос на создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())


#Запрос на создание набора для пользователя
def post_new_client_kit(body, authToken):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + authToken
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KIT, json=body,
                         headers=headers_dict)
