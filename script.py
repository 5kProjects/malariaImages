import random
import shutil
import os

folders = ["./cell_images/Parasitized"] # list of folders

# create the destination folders
os.mkdir("Training")
os.mkdir("Test")

for folder in folders:
   contents = os.listdir(folder) # get contents of every folder
random.shuffle(contents) # shuffle the contents list
split_point = 4 * len(contents) // 5  # get ≈80% of the contents length (this is a splitting point)
for img in contents[: split_point]: # get≈ 80 % of the contents(first 80 % images)
	shutil.copy(os.path.join(folder, img), os.path.join("Training", img)) # and copy every file to the "Training"

for img in contents[split_point: ]: # get≈ 20 % of the contents(last 20 % images).
	shutil.copy(os.path.join(folder, img), os.path.join("Test", img)) # and copy every file to the "Test"

