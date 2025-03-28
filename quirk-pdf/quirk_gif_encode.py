from PIL import Image
import os

# Directory path containing the PNG files
directory = 'qrs'

# Create a list to store the image frames
images = []

# Consistent image size
target_size = (300, 300)

# Create a blank image with a white background of the target size
blank_img = Image.new('RGB', target_size, (255, 255, 255))

#Add an empty white image at the start, and then periodically
images.append(blank_img)

# Iterate over the PNG files in the directory
frame_count = 0
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.png'):
        # Open the image
        img = Image.open(os.path.join(directory, filename))

        # Convert the image to RGB mode
        img = img.convert('RGB')

        # Resize the image to a consistent size
        img = img.resize(target_size)

        # Add the current image to the list
        images.append(img)
        frame_count+=1

        # Add blank frame every 10 frames to allow for the decoder to keep pace
        if frame_count % 10 == 0:
          images.append(blank_img)

# Add an empty white image to the end, and then periodically
images.append(blank_img)

# Save the animated GIF
try:
    images[0].save('animated.gif', save_all=True, append_images=images[1:], duration=1000, loop=0)
except AttributeError as e:
    print("Error occurred with image:", images[0])
    raise e
