from PIL import Image

def image_resizer(size_1, size_2):

    image = Image.open("Human_faces.jpg")

    print(f"The current_size of the image is {image.size}")

    resize_image = image.resize((size_1, size_2))

    resize_image.save("new_output.jpg")

