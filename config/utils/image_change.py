from PIL import Image


def crop_square_and_resize(image_path, height: int, width: int):

    img = Image.open(image_path)
    img_width, img_height = img.size

    if img_width != img_height:
        crop_width = min(img.size)
        crop_height = min(img.size)
        crop_image = img.crop(
            (
                (img_width - crop_width) // 2,
                (img_height - crop_height) // 2,
                (img_width + crop_width) // 2,
                (img_height + crop_height) // 2,
            )
        )
        crop_image.thumbnail((height, width))
        return crop_image
    img.thumbnail((height, width))
    return img
