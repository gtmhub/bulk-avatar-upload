# bulk-avatar-upload
Python utility to automatically upload avatars in bulk

### Usage
1. Enter authentication details for the account & path to where the profile images are that you want to upload.  
**ACCOUNT ID** - This is the Gtmhub account id which can be found at "Settings -> Api Tokens".  
**AUTH_TOKEN** - This is the Gtmhub auth token which can be found at "Settings -> Api Tokens".  
**PATH_TO_IMAGE_FOLDER** - This is the path where all profile images to be checked against the account for upload are stored.  
  *e.g.* **Windows:** C:\Users\<user>\Pictures\bulk-upload\\\
         **GNU/Linux, Unix:** /usr/share/images/bulk-upload/
2. The script compares the name of the image file (e.g. "alice.smith@example.org") to the current list of Gtmhub users that it gets via an API call.  
2.a. **Skip to step 3 if:** Your full **user email addresses** in Gtmhub all **match exactly the filenames** in the image folder ready for upload (e.g. image file name is *exactly* name.name@example.org - not including the file extension)  
2.b. If your user email addresses in Gtmhub contain a mix of different domains, e.g. "alice.smith@example.onmicrosoft.com" and "bob.smith@example.org", one minor alteration to the script is needed on line 64.  
Using Python's *replace* function, we can remove text from after the "@" sign from the Gtmhub user email.
In this case, line 64 would change from <code>email_starts_with_text = user['email']</code> to <code>email_starts_with_text = user['email'].replace('example.onmicrosoft.com','').replace('example.org',''</code>  
This would result in the text coming from the user list as "alice.smith" and "bob.smith" which is then compared to the starting text of the image file.  

3. Run the script. The script will print out when the upload has been successful, and an error encountered if it is not.
