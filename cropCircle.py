from PIL import Image, ImageDraw


def crop_to_circle(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)

    # Create a mask in the shape of a circle
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.width, img.height), fill=255)

    # Apply the circular mask to the image
    result = Image.new('RGBA', img.size, (0, 0, 0, 0))
    result.paste(img, mask=mask)

    # Save the result
    result.save(output_image_path)


# Example usage
input_path = 'Text.jpeg'
output_path = 'image_circle.png'
crop_to_circle(input_path, output_path)
