from PIL import Image

# Open the image file
with Image.open("photo me.jpg") as im:
    # Compress the image
    im.save("compressed_image.jpg", quality=50)
