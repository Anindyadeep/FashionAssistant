import json
from dataclasses import dataclass
from .config import JSON_PATH

@dataclass
class ClothingContent:
    upload_date: str
    upload_time: str
    clothing_size: str
    clothing_desc: str
    estimated_price_range: list
    user_content_folder: str
    stability_ai_folder: str
    virtual_trial_folder: str



class ClothingContentBank:
    def __init__(self, content_bank_source: str) -> None:

        # content_bank_source is the path where all the folder lies
        # default_content_bank_source = JSON_PATH
        self.content_bank_source = JSON_PATH if content_bank_source is None else content_bank_source
    
    def fetch_all(self, details: bool=False):
        # this will fetch all the projects done
        fetched_metadata = json.load(open(self.content_bank_source, 'r'), indent=4)
        return list(fetched_metadata.keys()) if not details else fetched_metadata

    def fetch(self, project_name) -> None:
        pass