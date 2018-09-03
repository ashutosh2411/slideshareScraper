from os import listdir
from fpdf import FPDF
from PIL import Image

def determine_size(w,h,W,H):
	ratio = min(W/w, H/h)*5
	w_ = ratio*w
	h_ = ratio*h
	return 0,0,w_,h_

pdf = FPDF()
imagelist = [f for f in listdir('images')]
# imagelist is the list with all image filenames

for i in range(1,len(imagelist)+1):
	image = str(i)+'.jpg'
	pdf.add_page()
	im = Image.open('images/'+image)
	w,h= im.size
	x ,y ,w, h = determine_size(w,h,pdf.w, pdf.h)
	pdf.image('images/'+image,0,0,w*.2,h*.2)
pdf.output("yourfile.pdf", "F")

