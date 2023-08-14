import base64
import os
import requests

product_type = "hoodie"
product_side = "back"

positive_prompt = f"""
You are an awesome phtographer and an editor who likes to take professional garment photos or turns out simple photos to be an awesome garment photo.
Given a picture of a {product_side} side {product_type}. You are required to enhance the image of the {product_type} by doing the following. First make enhance the color of the {product_type} but keeping
the actual color same. And then remove the background and replace it with a professional asthetic background such that the generated image of the {product_type} turns 
out to be like the one we see in ecommerce website. The lighting, backghround and the angle should be set such that it becomes a professional garment photo that
people will like at instagram. make the image as  realistic as possible. Keep the images that are there inside the {product_type}
"""

negative_prompt = f"""
Do not change the actual content of the {product_type}. The logo, the structure of the hoddie should not be changed. The lighting and the angle of capture and all the 
other essential photoghraphy styles should be maintained so that the image can be listed in the ecommerce website. Do not cartoonize the image. Do not delete or modify 
the inner content or the pictures inside of the {product_type}.
"""


pos = f"""
Fix the lighting and the background the {product_side} side of the {product_type}. The background should be in mono color and the lighting should make the same 
{product_type} more professinal. And do not change what is inside the hoodie, keep it as it is. 
"""

neg = f"""
DO NOT CHANGE WHAT IS DRAWN INSIDE OR WHAT IS WRITTEN INSIDE THE {product_type}. 
"""

response = requests.post(
    "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"sk-COvjg2INAWjwbDgx4EMdKeZH946IJWvOlRIayIiEenpbzxsa"
    },
    files={
        "init_image": open("./back_resized.jpeg", "rb")
    },
    data={
        "init_image_mode": "IMAGE_STRENGTH",
		"image_strength": 0.35,
		"samples": 2,
		"steps": 50,
		"seed": 0,
		"cfg_scale": 7,
		"style_preset": "enhance",
		"text_prompts[0][text]": pos,
		"text_prompts[0][weight]": 1,
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    with open(f'img2img_i_{image["seed"]}.png', "wb") as f:
        f.write(base64.b64decode(image["base64"]))