from PIL import Image, ImageDraw, ImageFont


def add_watermark(content, im_name, fontsize):
    text = content
    my_font = ImageFont.truetype(
        r'C:\Windows\Fonts\Dengl.ttf', fontsize)  # 设置字体和大小

    im = Image.open(im_name+'.png')
    layer = im.convert('RGBA')  # 将图像转换为4通道格式
    text_overlayer = Image.new(
        'RGBA', layer.size, (255, 255, 255, 0))  # 创建透明图片
    im_draw = ImageDraw.Draw(text_overlayer)  # 新图层用于画text

    text_size_x, text_size_y = im_draw.textsize(text, font=my_font)  # 获取text尺寸
    text_pos = (layer.size[0]-text_size_x, layer.size[1]-text_size_y)  # 左上角为原点

    im_draw.text(text_pos, text, font=my_font,
                 fill=(0, 255, 255, 255))  # RGBA设置颜色

    after = Image.alpha_composite(layer, text_overlayer)  # 将后一个图像复合到第一个图像上
    after.show()
    after.save('watermark_finished.png')


while True:
    try:
        content = input('Please input the watermark you want to add:')
        fontsize = input('Please input the watermark\'s fontsize:')
        im_name = input('Please input the photo\'s name(with out suffix):')
        add_watermark(content, im_name, int(fontsize))
        break
    except ValueError:
        print('Please input a num for fontsize!')
