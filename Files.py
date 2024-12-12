import os 
lst=os.listdir('dir')
if lst[0].lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
  print("image")
