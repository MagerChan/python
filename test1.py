from PIL import Image,ImageDraw

def main():
	im=Image.new('RGBA',(800,800))
	draw=ImageDraw.Draw(im)
	draw.rectangle((0,0,200,200),fill=(255,0,0,128))
	draw.rectangle((400,400,600,600),fill=(255,0,0))
	im.show()

#main()

base_layer=Image.open('F:\\python\\images\\1.png')
color_layer = Image.new('RGBA', base_layer.size, (255,0,0))
alpha_mask = Image.new('L', base_layer.size, 0)
alpha_mask_draw = ImageDraw.Draw(alpha_mask)
alpha_mask_draw.polygon(self.outline, fill=(255,0,0))
base_layer = Image.composite(color_layer, base_layer, alpha_mask)
base_layer.save('F:\\python\\images\\out.png')


# base_layer=Image.open('F:\\python\\images\\1.png')
# color_layer = Image.new('RGBA', base_layer.size, fill_rgb)
# alpha_mask = Image.new('L', base_layer.size, 0)
# alpha_mask_draw = ImageDraw.Draw(alpha_mask)
# alpha_mask_draw.polygon(self.outline, fill=fill_alpha)
# base_layer = Image.composite(color_layer, base_layer, alpha_mask)