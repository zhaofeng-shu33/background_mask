# author: zhaofeng-shu33
# usage: python background_mask.py img_name
# purporse: change white background to transparent state
import argparse
from PIL import Image
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('img_name', help='input image name')
    parser.add_argument('--threshold', type=int, default=240, help='threshold for transparency mask')
    args = parser.parse_args()
    threshold = args.threshold
    try:
        img = Image.open(args.img_name)
    except FileNotFoundError as e:
        raise e        
    if(img.mode == 'CMYK'):
        img = img.convert('RGB')
    has_alpha = (img.mode == 'RGBA')
    if not has_alpha:        
        red, green, blue = img.split()
        alpha = Image.new(mode='L', size=red.size)
    else:
        red, green, blue, alpha = img.split()
    pixels = alpha.load()
    width, height = red.size
    for i in range(0, width):
        for j in range(0, height):
            r = red.getpixel((i,j))
            g = green.getpixel((i,j))
            b = blue.getpixel((i,j))
            if(r>threshold and g>threshold and b>threshold):
                pixels[i,j] = 0
            else:
                pixels[i,j] = 255
    img.putalpha(alpha)
    img.save(args.img_name.split('.')[0] + '_mask.png')
                
            