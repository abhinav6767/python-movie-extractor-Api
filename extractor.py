import os
import sys
import time
from moviepy.editor import *

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import urllib.request
if  os.path.exists('./video_name.mp4'): 
	os.remove('./video_name.mp4');
if os.path.exists('./abc.mp3'):
	os.remove('./abc.mp3');
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print(sys.argv[1])
options = Options() 
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get(sys.argv[1])


try:
  element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "video")))
finally:
	y = driver.find_elements(By.TAG_NAME, "video")
	print("my y is ")
	for items in y:
		print(items.get_attribute("src"))
	urllib.request.urlretrieve(items.get_attribute("src"), 'video_name.mp4')  


def extract(video_path, audio_name, audio_format):
	"""
	Function that extract audio from video
	Assintotic: O(1)
	"""
	video = VideoFileClip(video_path)
	audio = video.audio
	audio.write_audiofile(audio_name + '.' + audio_format)
	


try:
	video_path = "./video_name.mp4"
	audio_name ="abc" 
	# input('\nAudio File Name:\n')
	# audio_option = input('\nChoose a format:\n'
	# 					+ '0 - MP3 (default)\n'
	# 					+ '1 - WAV\n')
	audio_format ='mp3'

	extract(video_path, audio_name, audio_format)
	print("processed")
	sys.stdout.flush()

except Exception as e: print(e)
