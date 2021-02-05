import os
from os import path
from wordcloud import WordCloud
from PIL import Image
from PIL import ImageFilter
import numpy as np
import sys
import json
import uuid

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# gen text
text = ""
try:
  json_dict = json.loads(sys.argv[1])
  for k in json_dict:
    tmp_str = k
    tmp_count = int(json_dict[k])
    for i in range(tmp_count):
      text += tmp_str+" "
except:
  print('Error!')
  exit()

# Generate a word cloud image
font_path = path.join(d, 'NotoSansJP-Light.otf')
mask = np.array(Image.open(path.join(d, "mask2.png")))
wordcloud = WordCloud(background_color='white',
                      #background_color='black',
                      font_path = font_path,
                      min_font_size=15,
                      max_font_size=200,
                      mask=mask,
                      contour_width=1,
                      contour_color='gray',
                      #contour_color='white',
                      collocations=False,
                      width=1280,
                      height=720)

image = wordcloud.generate(text).to_image()
if(len(sys.argv) == 3):
  imgfile_name = str(uuid.uuid4()) if sys.argv[2] == "?uid?" else sys.argv[2]
else:
  imgfile_name = str(uuid.uuid4())
image_path = '/var/www/html/wordcloud/imgs/'+imgfile_name+'.jpg'
image.save(image_path, quality=100)
print(image_path)
