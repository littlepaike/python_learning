# from PIL import Image
#
# img1 = Image.open('bjsxt.png').convert(mode='RGB')
# img2 = Image.new('RGB', img1.size, 'red')
# # img2.show()
# Image.blend(img1, img2, alpha=0.5).show()

from PIL import Image

img1 = Image.open('bjsxt.png').convert(mode="RGB")
img2 = Image.new('RGB', img1.size, 'red')
Image.blend(img1, img2, alpha=0.5).show()
# img1.show()
