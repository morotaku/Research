from PIL import Image
import numpy as np
from matplotlib import pylab as plt
from scipy import ndimage
from matplotlib.colors import LinearSegmentedColormap


path="D:/vector_vortex/mode_figure/12 5_0001.png"
print(Image.open(path))
img = np.array(Image.open(path)) #画像のndarray化
img_n=img/(np.amax(img)) #強度規格化
print(img)
#列、行の数
col=img_n.shape[1]
lin=img_n.shape[0]
print(lin)
X=0
for i in range(col):
    for j in range(lin):
        X=X+i*img_n[j][i] #x方向のモーメント
Y=0
for j in range(lin):
    for i in range(col):
        Y=Y+j*img_n[j][i] #y方向のモーメント
print(X)
#画像強度合計
img_sum=np.sum(img_n)

#重心
X_g=int(X/img_sum)
Y_g=int(Y/img_sum)
#print('Xg=',X_g,"","Yg=",Y_g)

#切り取り範囲
L=100
X=0 #平行移動(左と上)
Y=0
array_cut=img_n[Y_g-L-Y:Y_g+L-Y,X_g-L-X:X_g+L-X]

#画像の設定
rb=LinearSegmentedColormap.from_list('name',['black','red'],N=5000) #カラースケール,N(色の段階)#DB631F(色)
fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)
ax.set_axis_off()

#画像表示
#plt.imshow(ar,interpolation = "none",cmap='hot') #元の画像
plt.imshow(array_cut,interpolation = "none",cmap='hot',vmax=0.5,vmin=0.08) #切取後

plt.imshow(img)

plt.show()