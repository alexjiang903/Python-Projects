import colorgram

colors = colorgram.extract('painting.jpg', 40)
# can do any image saved on your computer as long as it is in the same folder as the python scripts

rgb_colors = []
for x in colors:
    rgb = x.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    color_tuple = (r, g, b)
    rgb_colors.append(color_tuple)

#removing white colors (not necessary)
rgb_colors.remove((231, 233, 237))
rgb_colors.remove((224, 233, 227))
rgb_colors.remove((233, 233, 232))
rgb_colors.remove((236, 231, 233))
