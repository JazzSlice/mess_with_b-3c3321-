import urllib.parse
import requests
import json

def createBUFolder (name='backup_folder', path='/'):
    info = ''
    url = 'https://cloud-api.yandex.net/v1/disk/resources?'
    path += name
    request_params = {
        'path': path,
    }
    request_header = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': token
    }
    response = requests.put(url, headers=request_header, params=request_params)
    u = 'User error.\n'
    s = 'Server error.\n'
    match response.status_code:
        case 201:
            info += f'Folder {path} created - SUCCESS'
        case 400:
            info += f'{u}Error while creation:\n{response.text["description"]}'
        case 401:
            info += f'{u}User not authorized'
        case 403:
            info += f'{u}API usage not availale. Your disk overweighted'
        case 404:
            info += f'{u}Required resourse not found'
        case 406:
            info += f'{u}Resourse could not be present in required format'
        case 409:
            info += f'{u}Folder {path} already exist\nWould you like to use existed resourse'
        case 413:
            info += f'{u}File is too large. Please, upload less weighted data'
        case 423:
            info += f'{u}Service is under technical updated.\nNow you can only download files'
        case 429:
            info += f'{u}Too much requests. Take a rest!'
        case 503:
            info += f'{s}Service not available now'
        case 507:
            info += f'{s}Not enought free psace'
    print(info)
    print(response.text)


token = 'your AUTH-token'
# url = 'https://cloud-api.yandex.net/v1/disk/resources?'

# request_header = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Authorization': token
# }

# request_params = {
#     'path': '/',
# }

# response = requests.get(url, headers=request_header, params=request_params)

# print(response.status_code, response.text)
createBUFolder()