# The main project of the day
# Involved extract a set of colors from an image
import colorgram

# Extract colors from the image
colors = colorgram.extract('hirstimg.jpg', 30)
rgb_colors = [(col.rgb.r, col.rgb.g, col.rgb.b) for col in colors]
real_colors = rgb_colors[3:]