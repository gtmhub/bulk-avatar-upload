import requests
import os

# CONFIGURATION
ACCOUNT_ID = '<Account ID from Settings -> API Tokens>'
AUTH_TOKEN = 'Bearer <Token from Settings -> API Tokens>'
PATH_TO_IMAGE_FOLDER = '<path\\to\\images\\' # Path must end with trailing forward/backward slash, depending on OS used. e.g. /usr/share/images/ for GNU/Linux & Unix vs C:\Users\<UserName>\Pictures\ for Windows

def get_user_list():
    url = 'https://app.gtmhub.com/api/v1/accounts/users'
    payload = {}
    headers = {
        'gtmhub-accountId': ACCOUNT_ID,
        'Authorization': AUTH_TOKEN
    }

    try:
        response = requests.request('GET', url, headers=headers, data=payload)
        rj = response.json()
        user_list = rj['items']
        return [True, user_list]
    except Exception as error:
        return [False, "Error text: " + str(error)]

def upload_image(user_id, path_to_images, file):
    url = 'https://app.gtmhub.com/api/v1/fileserver/avatar/' + user_id

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

    try:
        # print("Attempting to change user id " + user_id + " using " + path_to_images + file + ".")
        response = requests.request('POST', url, headers=headers, data=payload, files=files)
        # print("Response code: " + str(response.status_code))
        response_code = str(response.status_code)
        if response_code == '200':
            print('User id "' + user_id + '" updated.')
        else:
            print('Received a response code ' + response_code + ' for user id "' + user_id + '".')
    except Exception as img_upload_error:
        print('Error uploading image for user id ' + user_id + ', error text: ' + str(img_upload_error))

if __name__ == '__main__':
    users = get_user_list()

    if users[0] is False:
        print('Error loading users, error text:' + users[1])
    elif users[0] is True:
        # Get a list of the image files that should be uploaded
        img_files = os.listdir(PATH_TO_IMAGE_FOLDER)

        for img_file in img_files:
            for user in users[1]:
                # print(user['email'])
                email_starts_with_text = user['email']
                if img_file.startswith(email_starts_with_text):
                    # print(user['email'] + " & " + img_file + " match! [user id=" + user['id'] + "]")
                    path_to_image = PATH_TO_IMAGE_FOLDER + img_file
                    upload_image(user['id'], PATH_TO_IMAGE_FOLDER, img_file)
