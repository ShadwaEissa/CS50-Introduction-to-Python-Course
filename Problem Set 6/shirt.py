import sys
import csv
from PIL import Image, ImageOps

name1, extension1 = sys.argv[1].split(".")
name2, extension2 = sys.argv[2].split(".")

if len(sys.argv) == 3:
    if (extension1 == "jpg" or  extension1 == "jpeg" or extension1 == "png") and (extension2 == "jpg" or  extension1 == "jpeg" or extension1 == "png"):
        if extension1 == extension2:
            #open the image file
            try:
                image = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("Input does not exist")
            #open the shirt file
            shirtfile = Image.open("shirt.png")
            #get the size of the shirt to resize the image according to it
            size = shirtfile.size
            #resize the image to the size of the shirtfile
            muppet = ImageOps.fit(image, size)
            # paste the tshirt on the muppet file
            muppet.paste(shirtfile, shirtfile)
            #save the output function
            muppet.save(sys.argv[2])
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")