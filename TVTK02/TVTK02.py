from mayavi import mlab
import numpy as np
'''
n_mer, n_long = 6, 11
dphi = np.pi / 1000.0
phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
mu = phi * n_mer
x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
z = np.sin(n_long * mu / n_mer) * 0.5

l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius = 0.025, colormap = 'Spectral')
mlab.show()
'''
'''
def f(x,y):
    return np.sin(x - y) + np.cos(x + y)

x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
s = mlab.contour_surf(x, y, f)
mlab.show()
'''
'''
x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
scalars = x * x + y * y + z * z
obj = mlab.contour3d(scalars, contours=8, transparent=True)
mlab.show()
'''
'''
x, y, z = np.mgrid[-2:3, -2:3, -2:3]
r = np.sqrt(x ** 2 + y ** 2 + z ** 4)
u = y * np.sin(r) / (r + 0.001)
v = -x * np.sin(r) / (r + 0.001)
w = np.zeros_like(z)

obj = mlab.quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)
mlab.show()
'''
'''
x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100 * np.sin(x * y) / (x * y)

mlab.figure(bgcolor=(1, 1, 1))
surf = mlab.surf(z, colormap='cool')
lut = surf.module_manager.scalar_lut_manager.lut.table.to_array()
lut[:, -1] = np.linspace(0, 255, 256)
surf.module_manager.scalar_lut_manager.lut.table = lut
mlab.show()
'''
'''
######场景初始化######
figure = mlab.gcf()

# 用mlab.points3d建立红色和白色小球的集合
x1, y1, z1 = np.random.random((3, 10))
red_glyphs = mlab.points3d(x1, y1, z1, color=(1, 0, 0),
                           resolution=10)
x2, y2, z2 = np.random.random((3, 10))
white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9, 0.9, 0.9),
                             resolution=10)

# 绘制选取框，并放在第一个小球上
outline = mlab.outline(line_width=3)
outline.outline_mode = 'cornered'
outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
                  y1[0] - 0.1, y1[0] + 0.1,
                  z1[0] - 0.1, z1[0] + 0.1)

######处理选取事件#####
# 获取构成一个红色小球的顶点列表
glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()


# 当选取事件发生时调用此函数
def picker_callback(picker):
    if picker.actor in red_glyphs.actor.actors:
        # 计算哪个小球被选取
        point_id = int(picker.point_id / glyph_points.shape[0])  # int向下取整
        if point_id != -1:  # 如果没有小球被选取，则point_id = -1
            # 找到与此红色小球相关的坐标
            x, y, z = x1[point_id], y1[point_id], z1[point_id]
            # 将外框移到小球上
            outline.bounds = (x - 0.1, x + 0.1,
                              y - 0.1, y + 0.1,
                              z - 0.1, z + 0.1)


picker = figure.on_mouse_pick(picker_callback)
mlab.title('Click on red balls')
mlab.show()
'''
'''
x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)

mlab.contour3d(s)
mlab.show()
'''
'''
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s), plane_orientation='x_axes', slice_index=10,)
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),plane_orientation='y_axes', slice_index=10,)
mlab.outline()
'''
'''
x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x * y * z) / (x * y * z)

from mayavi import mlab
from mayavi.tools import pipeline

src = mlab.pipeline.scalar_field(s)
mlab.pipeline.iso_surface(src, contours=[s.min() + 0.1 * s.ptp(), ], opacity=0.1)
mlab.pipeline.iso_surface(src, contours=[s.max() - 0.1 * s.ptp(), ])
mlab.pipeline.image_plane_widget(src,
                                 plane_orientation='z_axes',
                                 slice_index=10,
                                 )
mlab.show()

'''
'''
x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
u = np.sin(np.pi * x) * np.cos(np.pi * z)
v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)
flow = mlab.flow(u, v, w, seed_scale=1, seed_resolution=5, integration_direction='backward')

#src = mlab.pipeline.vector_field(u, v, w)#
#magnitude = mlab.pipeline.extract_vector_norm(src)#
#mlab.pipeline.iso_surface(magnitude, contours=[2.0, 0.5])#
#mlab.pipeline.vector_cut_plane(src, mask_points=10, scale_factor=2.0)#
mlab.outline()
mlab.show()
'''
'''
import tarfile
from os.path import join
import shutil
dragon_tar_file = tarfile.open('dragon.tar.gz')
try:
    os.mkdir('dragon_data')
except:
    pass
dragon_tar_file.extractall('dragon_data')
dragon_tar_file.close()
dragon_ply_file = join('dragon_data', 'dragon_recon', 'dragon_vrip.ply')
mlab.pipeline.surface(mlab.pipeline.open(dragon_ply_file))
mlab.show()
shutil.rmtree('dragon_data')
'''

'''
import zipfile


# 读取压缩文件
hgt = zipfile.ZipFile('N36W113.hgt.zip').read('N36W113.hgt')
data = np.fromstring(hgt, '>i2')
data.shape = (3601, 3601)
data = data.astype(np.float32)
data = data[:1000, 900:1900]
data[data == -32768] = data[data > 0].min()

# 渲染地形hgt的数据data
mlab.figure(size=(400, 320), bgcolor=(0.16, 0.28, 0.46))
mlab.surf(data, colormap='gist_earth', warp_scale=0.2,
          vmin=1200, vmax=1610)

# 清空内存
del data
# 创建交互式的可视化窗口
mlab.view(-5.9, 83, 570, [5.3, 20, 238])
mlab.show()

'''

# 城市经纬度数据
cities_data = """
Bei Jing, 116.23,39.54
Shang Hai, 121.52, 30.91
Hong Kong,114.19,22.38
Delhi,77.21,28.67
Johannesburg,28.04,-26.19
Doha,51.53,25.29
Sao Paulo,-46.63,-23.53
Toronto,-79.38,43.65
New York,-73.94,40.67
San Francisco,-122.45,37.77
Dubai,55.33,25.27
Sydney,151.21,-33.87
"""
########## 读取数据#########
# 建立城市-城索引的字典、城市经纬度的列表
import csv

cities = dict()
coords = list()
for line in list(csv.reader(cities_data.split('\n')))[1:-1]:
    name, long_, lat = line
    cities[name] = len(coords)
    coords.append((float(long_), float(lat)))

########## 坐标转换##########
# 将经纬度的位置转换为三维坐标

coords = np.array(coords)
lat, long = coords.T * np.pi / 180
x = np.cos(long) * np.cos(lat)
y = np.cos(long) * np.sin(lat)
z = np.sin(long)

##########建立窗口##########

mlab.figure(bgcolor=(0.48, 0.48, 0.48), size=(400, 400))

##########绘制地球##########
# 绘制半透明球体表示地球
sphere = mlab.points3d(0, 0, 0, scale_factor=2,
                       color=(0.67, 0.77, 0.93),
                       resolution=50,
                       opacity=0.7,
                       name='Earth')

# 调整镜面反射参数
sphere.actor.property.specular = 0.45
sphere.actor.property.specular_power = 5
# 设置背面剔除，以更好的显示透明效果
sphere.actor.property.backface_culling = True

##########绘制城市##########
# 绘制城市位置
points = mlab.points3d(x, y, z, scale_factor=0.03, color=(0, 0, 1))
# 绘制城市名称
for city, index in cities.items():
    label = mlab.text(x[index], y[index], city,
                      z=z[index], color=(0, 0, 0),
                      width=0.016 * len(city), name=city)

##########绘制大洲边界##########
from mayavi.sources.builtin_surface import BuiltinSurface

continents_src = BuiltinSurface(source='earth', name='Continents')
# 设置LOD为2
continents_src.data_source.on_ratio = 1
continents = mlab.pipeline.surface(continents_src, color=(0, 0, 0))

##########绘制赤道##########
theta = np.linspace(0, 2 * np.pi, 100)  # 平分360为100份
x = np.cos(theta)
y = np.sin(theta)
z = np.zeros_like(theta)
mlab.plot3d(x, y, z, color=(1, 1, 1), opacity=0.2, tube_radius=None)
##########显示可交互窗口##########
mlab.view(100, 60, 4, [-0.05, 0, 0])
mlab.show()







