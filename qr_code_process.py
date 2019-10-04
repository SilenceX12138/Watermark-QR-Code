from PIL import Image

def add_qr_code(qr_name,im_name):
    qr = Image.open(qr_name+'.png')
    im = Image.open(im_name+'.png')

    layer = Image.new('RGBA', im.size, (255, 255, 255, 0))  # 创建透明图片
    qr_pos = (layer.size[0]-qr.size[0], layer.size[1]-qr.size[1])  # 左上角为原点
    layer.paste(qr, qr_pos)  # 新图层上绘制二维码(mask参数必须是有透明部分的图像)

    im_after = Image.composite(layer, im, layer)
    im_after.show()
    im_after.save('qr_finished.png')

qr_name=input('Please input the code\'s name(with out suffix)')
im_name=input('Please input the photo\'s name(with out suffix)')
add_qr_code(qr_name,im_name)