import requests
import os

ACCOUNT_ID = '<id>'
AUTH_TOKEN = 'Bearer <token>'
PATH_TO_IMAGE_FOLDER = "P:ath\\to\\pics\\"

def get_user_list():
    url = "https://app.gtmhub.com/api/v1/accounts/users"

    payload = {}
    headers = {
        'gtmhub-accountId': ACCOUNT_ID,
        'Authorization': AUTH_TOKEN
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    rj = response.json()
    user_list = rj['items']
    return user_list


def upload_image(user_id, path_to_images, file):
    url = "https://app.gtmhub.com/api/v1/fileserver/avatar/" + user_id

    payload = {}
    files = [
        ('file', (file,
                  open(path_to_images + file, 'rb'),
                  'image/jpeg'))
    ]
    headers = {
        'gtmhub-accountId': ACCOUNT_ID,
        'userId': user_id,
        'Authorization': AUTH_TOKEN
    }

    #print("Attempting to change user id " + user_id + " using " + path_to_images + file + ".")
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    #print("Response code: " + str(response.status_code))

if __name__ == '__main__':
    # Get a list of users that exist on the account
    users = get_user_list()

    # Get a list of the files that should be uploaded
    img_files = os.listdir(PATH_TO_IMAGE_FOLDER)

    for img_file in img_files:
        for user in users:
            #print(user['email'])
            if img_file.startswith(user['email']):
                #print(user['email'] + " & " + img_file + " match! [user id=" + user['id'] + "]")
                path_to_image = PATH_TO_IMAGE_FOLDER + img_file
                upload_image(user['id'], PATH_TO_IMAGE_FOLDER, img_file)
