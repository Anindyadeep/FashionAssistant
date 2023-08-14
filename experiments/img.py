from PIL import Image

# Open the original image
original_image = Image.open("back.jpeg")

# Resize the image to the desired dimensions (1024x1024)
resized_image = original_image.resize((896, 1152),Image.Resampling.LANCZOS)

# Save the resized image to a new file
resized_image.save("back_resized.jpeg")

# Close the images
original_image.close()
resized_image.close()