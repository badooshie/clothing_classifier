from PIL import Image
import os

target_size = (256, 256)
target_quality = 90

input_directory = "pre_images"
output_directory = "post_images"

if not os.path.exists(output_directory):
	os.makedirs(output_directory)

accepted_extensions = [".jpg", ".jpeg", ".png"]

existing_numbers = [
	int(filename.split("_")[1].split(".")[0])
	for filename in os.listdir(output_directory)
	if filename.endswith(tuple(accepted_extensions)) 
]

if existing_numbers:
	max_number = max(existing_numbers)
else:
	max_number = 0

for filename in os.listdir(input_directory):
	if any(filename.endswith(ext) for ext in accepted_extensions):
		image_path = os.path.join(input_directory, filename)
		image = Image.open(image_path)

		if image.mode != "RGB":
			image = image.convert("RGB")

		resized_image = image.resize(target_size)

		new_filename = f"shirt_{max_number + 1:03d}.jpg"
		output_path = os.path.join(output_directory, new_filename)
		
		max_number += 1
		
		resized_image.save(output_path, quality=target_quality)

		print("resized and saves {}".format(filename))

print("All images resized and saved")
