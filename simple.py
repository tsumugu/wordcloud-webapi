"""
Thanks to wordcloud Minimal Example (https://amueller.github.io/word_cloud/auto_examples/simple.html)
"""

import os
from os import path
from wordcloud import WordCloud
import sys
import json

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# convert JSON to Space Splited String
#ex)
#  {"test": 5, "fizz": 2, "buzz": 3} => "test test test test test fizz fizz buzz buzz buzz"
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

# generate wordcloud
font_path = path.join(d, 'NotoSansJP-Light.otf')
wordcloud = WordCloud(background_color='white',
                      font_path = font_path,
                      min_font_size=15,
                      max_font_size=200,
                      collocations=False,
                      width=1280,
                      height=720)
image = wordcloud.generate(text).to_image()
image.save(path.join(d, 'test.jpg'), quality=100)
