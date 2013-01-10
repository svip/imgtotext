from PIL import Image
import argparse

def tocss(r, g, b):
	s = "#%2x%2x%2x" % (r, g, b)
	return s.replace(" ", "0")

def createtext(imagefile):
	try:	
		im = Image.open(imagefile)
	except IOError:
		print "No such file."
		return None
	rgb_im = im.convert("RGB")
	s = ''
	for x in range(0, rgb_im.size[0]):
		for y in range(0, rgb_im.size[1]):
			if s != '':
				s += ' '
			r, g, b = rgb_im.getpixel((x, y))
			s += tocss(r, g, b)
	return s

def output(dest, text):
	if text==None:
		return
	if dest==None:
		print text
	else:
		f = open(dest, 'w')
		f.write(text)
		f.close()

def __main__():
	parser = argparse.ArgumentParser(description='Convert images to CSS colour codes.')
	parser.add_argument('imagefile', metavar='image',
	                    type=str, help='image to convert')
	parser.add_argument('output', default=None, type=str,
	                    nargs='?',
	                    help='text file to output (default: stdout)')
	# argument ideas:
	# * line break after each row
	# * define format
	# * decide which way to run
	args = parser.parse_args()
	s = createtext(args.imagefile)
	output(args.output, s)

__main__()
