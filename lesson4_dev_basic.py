from PIL import Image

image = Image.open("monro.jpg")
r_image, g_image, b_image = image.split()

crop_left = (100, 0, r_image.width, r_image.height)
crop_right = (0, 0, 596, r_image.height)
crop_mid = (50, 0, 646, r_image.height)

r_left = r_image.crop(crop_left)
r_mid = r_image.crop(crop_mid)
r_imp = Image.blend(r_left, r_mid, 0.5)

b_right = b_image.crop(crop_right)
b_mid = b_image.crop(crop_mid)
b_imp = Image.blend(b_right, b_mid, 0.5)

g_mid = g_image.crop(crop_mid)

art_monro = Image.merge("RGB", (r_imp, g_mid, b_imp))
art_monro.save("art_monro.jpg")

art_monro.thumbnail((80, 80))
art_monro.save("art_monro_icon.jpg")
