from PIL import Image
from numpy import asarray

def occlusion_report(image_path):
	image = Image.open(image_path)
	arr_list = asarray(image)
	red = blue = green = 0
	for i in arr_list:
		for j in i:
			red = red + j[0]
			blue = blue + j[1]
			green = green + j[2]
	total = red + blue + green
	red = red / total * 100
	blue = blue / total * 100
	green = green / total * 100

	return [image_path, red, blue, green]

angles = [0, 45, 90, 135, 180]
for i in angles:
	print(occlusion_report("images/sample48_%s.png" % (str(i))))
