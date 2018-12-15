
#module base64
import base64
with open("file.png", "rb") as imageFile:
    #read the file and encode with base64
    decoded_image = base64.b64encode(imageFile.read())
    print decoded_image
