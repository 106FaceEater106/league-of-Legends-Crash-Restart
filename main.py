from PIL import ImageGrab
#from compare import compare_images, mse
from compare import compareimage
import time

while True:
    time.sleep(120)
    snapshot = ImageGrab.grab()
    save_path_original = "original.jpg"
    snapshot.save(save_path_original)
    print("Start")
    time.sleep(15*60)
    snapshot = ImageGrab.grab()
    save_path_mod = "modified.jpg"
    snapshot.save(save_path_mod)

    compareimage("original.jpg", "modified.jpg")

