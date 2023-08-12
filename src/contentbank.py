import os
from dataclasses import dataclass

@dataclass
class ClothingContent:
    content_id: str
    content_upload_date: str
    content_category: str # clothing 
    content_assets_folder_path: str
    content_description: str
    content_available_size: list
    content_expected_post_date: str


