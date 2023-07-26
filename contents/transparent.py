from PIL import Image

def make_image_transparent(image_path):
    img = Image.open(image_path).convert("RGBA")
    data = img.getdata()

    # Create a new list to store the updated image data
    new_data = []
    for item in data:
        # Set the alpha value of each pixel to the corresponding alpha channel value
        new_data.append((item[0], item[1], item[2], item[3]))
    
    img.putdata(new_data)
    return img

# Example Usage:
image_path = "image_widgets/title.png"  # Use forward slashes instead of backslashes

transparent_image = make_image_transparent(image_path)
transparent_image.show()