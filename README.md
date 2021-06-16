# GDRIVE_PDF_INTERPRETER
Interprets the img/json combo recieved when a pdf is loaded from Google Drive.

## INFO DUMP
**Basic URL Format**  
If viewing directly from within Google Drive or Google Classroom
```
https://drive.google.com/viewerng/<type>?<param>
```
If viewing from a new window
```
https://drive.google.com/viewer2/prod-00/<type>?<param>
```

\<type\> can be:  

"upload": lists other possible urls  
"meta": json file which includes total number of pages and max image resolution  
"img": pdf page as an image  
"presspage": json contianing text present in pdf as well as its location.

\<param\> can be:

"id":  Identifies resource when viewed within Google Drive or Google Classroom. Required.  
"ds": Identifies resource when viewed from a new window . Required  
"authuser": INT. Represents which account is used to authenticate (when logged into multiple google accounts). Required.  
"page": INT. Page number. Required for img and presspage.  
"w": INT. Horizontal resolution of image. Optional for img. Defaults to 800. Max value found in response to upload.  
"webp": TRUE|FALSE. Request image in webp format. Otherwise defaults to JPEG.   

All json responses contain `)]}'` on first line. Ignore it.

**TODO: RECORD INFO REGARDING PRESSPAGE JSON RESPONSE**
