# bulk-avatar-upload
Utility to upload avatars in bulk

### Usage
**1. CONFIGURATION**  
 Enter authentication details for the account & path to where the profile images are that you want to upload.  
 
*ACCOUNT ID* - This is the Gtmhub account id which can be found at "Settings -> Api Tokens".  
*AUTH_TOKEN* - This is the Gtmhub auth token which can be found at "Settings -> Api Tokens". Please ensure this token has rights for updateing profile images.  
*PATH_TO_IMAGE_FOLDER* - This is the path where all profile images to be checked against the account for upload are stored in the system running the script.  
  *e.g.   Windows:* C:\Users\<user>\Pictures\bulk-upload\\\
         *GNU/Linux, Unix:** /usr/share/images/bulk-upload/

**2. PAIRING IMAGE NAMES TO EMAILS**  
The script compares the name of the image file (e.g. "alice.smith@example.org") to the current list of Gtmhub users that it retreives via an API call. If this matches, it will attempt to update the profile image using a further API call.

**Skip to step 3 if:** Your full **user email addresses** in Gtmhub all **match exactly the filenames** in the image folder ready for upload (e.g. user email and the image file name is *exactly* firstname.lastname@example.org - not including the file extension)  

Image filename matches Gtmhub user email.  
![Alt text](/img/alice.smith.PNG "Filename")![Alt text](/img/asg.png "Gtmhub user email")  
If this is the case for all filenames, they are ready for upload.

*Rare case:* If your user email addresses in Gtmhub contain a mix of different domains, e.g. "alice.smith@example.onmicrosoft.com" and "bob.smith@example.onmicrosoft.com", a small alteration in how the files are compared before upload is necessary (line 64, where we declare the text we use to match the two files up).

Using Python's [replace](https://docs.python.org/3/library/stdtypes.html) function, we can remove differing text from after the "@" sign from the Gtmhub user email.
As above, I have users in Gtmhub with 2 varying domain extensions. "@example.onmicrosoft.com", and "@example.org".

In this case, to ensure that the email address in Gtmhub, and the image file name matches up, line 64 would change from  
<code>email_starts_with_text = user['email']</code>  
to  
<code>email_starts_with_text = user['email'].replace('example.onmicrosoft.com','').replace('example.org','')</code>  

This would result in the text coming from the user list as "alice.smith" and "bob.smith" which is then compared to the starting text of the image file, allowing edge cases like the below not to affect the bulk upload of users.  
![Alt text](/img/bob.smith.PNG "Filename")![Alt text](/img/bsg.PNG "Gtmhub user email")  
Above, we see that the upload script will compare "bob.smith" from the user list, match the beginning of the image file "bob.smith@example.org", and upload the image correctly.

**3. RUN THE SCRIPT**  
The script will alert the user to any issues when a match is found and an upload is not successful. The error text will be printed to the console for further debugging.
