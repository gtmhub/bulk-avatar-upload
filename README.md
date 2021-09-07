# bulk-avatar-upload
Utility to automatically upload avatars in bulk

### Usage
1. Enter details for the account & path to where the profile images are that you want to upload.
ACCOUNT ID - This is the Gtmhub account id which can be found in the account settings.
AUTH_TOKEN - This is the Gtmhub auth token which can be found in the account settings.
PATH_TO_IMAGE_FOLDER - This is the path where all profile images to be checked against the account for upload are stored.

2. Run the script. There are print lines for debugging commented out, e.g. the response code (line 40) you receive when attempting to update the profile image.

### Current restrictions
Profile image names must match exactly the email account name on Gtmhub. For the customer I wrote this for, I did some straightforward replacing of the domain to ensure we were just checking the text before the domain as this matched, so it's possible that there are different domains (e.g. example1@domain.onmicrosoft.com vs example1@domain.com) or erroneous naming (some of the files I was uploading were named "example1@domain.com.jpg", for example). However, the script isn't set up to do that initially. To do that, you're going to want to edit line 52 with conditions that will remove text after the "@"

e.g. if img_file.startswith(user['email'].replace(".domain.com","")):
  
v0.1 is a rudimentary Python script to allow us to do this. By v1 I am aiming to have this distributed via a standalone downloadable webpage in a similar manner to the data importer tool.
