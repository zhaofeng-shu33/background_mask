# background_mask
Utility for adding alpha channel for white background region of a picture.

## How to use
Make sure you install `Pillow` first. Then type `python background_mask.py [--threshold 240] input_image_file_name` and you get the generated image named with `..._mask.png`.

## Situtation for usage
When you download an image from Internet, the alpha channel does not exist. Use this utility script can make the whilte region of the picture transparent.
