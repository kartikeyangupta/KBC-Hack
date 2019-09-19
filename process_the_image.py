import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import pytesseract
import mechanize
import nltk
from bs4 import BeautifulSoup
from html2text import html2text
import re
from googlesearch import search

pytesseract.pytesseract.tesseract_cmd = 'C://Users//Mr-Robot//Desktop//KBC-Hack//Tesseract-OCR/tesseract'

def word_count(str,A,B,C,D):
    cnt_a = str.count(A)
    cnt_b = str.count(B)
    cnt_c = str.count(C)
    cnt_d = str.count(D)
    max= cnt_a+cnt_b+cnt_c+cnt_d
    print("-----------The answer probabilty--------")
    print("A : ",A,int((cnt_a/max)*100),"%")
    print("B : ",B,int((cnt_b/max)*100),'%')
    print("C : ",C,int((cnt_c/max)*100),'%')
    print("D : ",D,int((cnt_d/max)*100),'%')


def clean_html(html):
    # First we remove inline JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # Then we remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # Next we can remove the remaining tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Finally, we deal with whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()

def text_proceesor(text):
        string = ''
        text = text.lower()
        l = text.splitlines()
        for i in l:
            string = string + i + ' '
        return string

img = Image.open('kbc image 1.jpeg')
draw = ImageDraw.Draw(img)
draw.rectangle(((60,437), (475,263)),fill=None)#question
draw.rectangle(((54,551), (482,473)),fill=None)#A
draw.rectangle(((54,662), (482,588)),fill=None)#B
draw.rectangle(((54,777), (482,699)),fill=None)#C
draw.rectangle(((54,890), (482,814)),fill=None)#D
#img.save("with_boundaries.png")
question = img.crop((60,263,475,437))#question_cropped
#question.save("question.png")
A = img.crop((54,473,475,551))#option_A_cropped
#A.save("option_A.png")
B = img.crop((60,588,475,662))#option_B_cropped
#B.save("option_B.png")
C = img.crop((60,699,475,777))#option_C_cropped
#C.save("option_C.png")
D = img.crop((60,814,475,890))#option_D_cropped
#D.save("option_D.png")
# A.show()
# B.show()
# C.show()
# D.show()
text = pytesseract.image_to_string(question)
question = text_proceesor(text)
A=pytesseract.image_to_string(A)
A = text_proceesor(A)
B=pytesseract.image_to_string(B)
B = text_proceesor(B)
C=pytesseract.image_to_string(C)
C = text_proceesor(C)
D=pytesseract.image_to_string(D)
D = text_proceesor(D)
# print(A,B,C,D,sep="\n")
x = search(question, tld="com", num=10, stop=1, pause=2)
for i in x:
    url = i
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]
    html = br.open(url).read().decode('utf-8')
    cleanhtml = clean_html(html)
    text = html2text(cleanhtml)
    text = text_proceesor(text)
    soup = BeautifulSoup(html,features="lxml")
    text2 = soup.get_text()
    #I haven't used BeatifulSoup for text as its text is not clean but its a better method
    word_count(text,A,B,C,D)
    #print(text)
