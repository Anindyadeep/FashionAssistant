import os
import json 

### Here is how the directory style for each content inside the 
# content bank should look like
# -- ./alippo_metadata
#   -- metadata.json # master metadata
#   -- /content1
#   -- /content2

### This is how the json should look like for now
# {
#   'project_name' : {
#       'title' : ,
#       'clothing_size':...,
#       'clothing_desc':...,
#       'estimated_price_range': ...,
#       'user_content_folder': ./alippo_metadata/project_name/user_content,
#       'ai_content_folder': ./alippo_metadata/project_name/ai_content,
#   }
# }

# inside the AI content metadata there will be things like 
# generated by stability AI 
# and also the virtual try one

HOME_DIR = os.path.expanduser("~")
METADATA_STORE = os.path.join(HOME_DIR, '.alippo_metadata')
JSON_PATH = os.path.join(METADATA_STORE, 'metadata.json')

if not os.path.exists(METADATA_STORE):
    os.mkdir(METADATA_STORE)
    
try:
    initial_json = json.load(open(JSON_PATH, 'r'))
except:
    initial_json = {}
    json.dump(initial_json, open(JSON_PATH, 'w'))


# To be filled from .dotenv

CHATGPT_API_KEY = ...
STABILITY_AI_API_KEY = ...
