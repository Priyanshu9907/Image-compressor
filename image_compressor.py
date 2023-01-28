from PIL import Image

# Open the image file
with Image.open("photo.jpg") as im:
    # Compress the image
    im.save("compressed_image.jpg", quality=50)
