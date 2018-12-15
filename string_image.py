with open('decode.txt') as rd:
    decoded_image = rd.readlines()
fh = open("iamgeToSave.png", "wb")
fh.write(decoded_image[0].decode('base64'))
fh.close()
