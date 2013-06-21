import shutil
import os

for number in range(97,123):
	letter = chr(number)
	os.mkdir('./'+letter+'3')

for i in os.listdir('./original_files'):
	shutil.move('./original_files/' + i, './'+i[0]+'/')
