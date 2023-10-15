import sys
from PIL import Image
import PIL
def main():
    if len(sys.argv) == 3:
        if sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) and sys.argv[
            2
        ].lower().endswith((".jpg", ".jpeg", ".png")):
            if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
                sys.exit("Input and Output have different extensions")
            shirtimage = Image.open("shirt.png")
            size = shirtimage.size
            try:
                input_image = Image.open(sys.argv[1])
                muppet = PIL.ImageOps.fit(input_image, size)
                # print(input_image.show())
                muppet.paste(shirtimage, shirtimage)
                muppet.save(sys.argv[2])
                # nm.show()
                print(input_image.size)
            except FileNotFoundError:
                raise
            print(shirtimage.size)
            print(sys.argv[1:])

        else:
            sys.exit("Invalid Input")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
