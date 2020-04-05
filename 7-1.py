from PIL import Image
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8,8))
plt.suptitle("图像基本操作",fontsize = 20,color = "b")
img = Image.open("lena.tiff")
img_r,img_g,img_b = img.split()
plt.subplot(221)
plt.axis("off")
R = img_r.resize((50,50))
plt.imshow(R,cmap = "gray")
plt.title("R-缩放",fontsize = 14)
plt.subplot(222)
G = img_g.transpose(Image.FLIP_LEFT_RIGHT)
G = img_g.transpose(Image.ROTATE_270)
plt.imshow(G,cmap = "gray")
plt.title("G-镜像+旋转",fontsize = 14)
plt.subplot(223)
plt.axis("off")
B = img_b.crop((0,0,150,150))
plt.imshow(B,cmap = "gray")
plt.title("B-裁剪",fontsize = 14)
plt.subplot(224)
plt.axis("off")
RGB = Image.merge("RGB",[img_r,img_g,img_b])
RGB.save("test.png")
plt.imshow(RGB,cmap = "gray")
plt.title("RGB",fontsize = 14)


