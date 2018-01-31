from PIL import Image, ImageDraw, ImageFont


def add_num(img):
    draw = ImageDraw(img)
    myfont = ImageFont.truetype('/Library/Fonts/Arial Italic.ttf ', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0


if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)
