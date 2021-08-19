from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
import numpy as np
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
basedir = os.path.join(basedir,"watermarker")

def watermarker(filename,watermark,size):
    loc = os.path.join(basedir, "sample")
    saveloc = os.path.join(basedir, "watermarked")
    img = Image.open(os.path.join(loc,filename))
    cpyimg = img.copy()
    width,height = img.size

    draw = ImageDraw.Draw(cpyimg)

    margin = 10

    font = ImageFont.truetype('arial.ttf', size)
    textwidth, textheight = draw.textsize(watermark, font)

    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), watermark, font=font)

    cpyimg.save(os.path.join(basedir, "watermarked/"+"watermarked"+filename))

def waterimg(filename,watermark,size):
    loc = os.path.join(basedir, "sample")
    saveloc = os.path.join(basedir, "watermarked")
    img = Image.open(os.path.join(loc,filename))
    cpyimg = img.copy()
    width,height = img.size
    watermarkloc = os.path.join(basedir, "watermarker")
    watermarkimg = Image.open(os.path.join(basedir, "watermark/"+watermark))
    margin = 10
    pixel = 100

    size = (pixel,pixel)
    watermarkimg.thumbnail(size)

    watermarkwidth,watermarkheight = watermarkimg.size
    x = width - margin - watermarkwidth
    y = height - margin - watermarkheight

    cpyimg.paste(watermarkimg,(x,y))
    cpyimg.save(os.path.join(basedir, "watermarked/"+"watermarked"+filename))