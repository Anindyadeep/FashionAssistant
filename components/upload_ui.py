import os
import json 
import streamlit as st
from PIL import Image 
from datetime import datetime

# get the config file
from src.config import METADATA_STORE, JSON_PATH

class ContentUpload:
    def upload_content(self):
        """
        Uploads the content that user just took from camera. This can be helpful when user is going to 
        post something on social media or do the same for the business side
        """
        st.title("Upload your content here")
        contents = st.file_uploader(
            label="Upload images of the content", type=['.jpeg', '.jpg', '.png'],
            accept_multiple_files=True
        )
        return contents

    def content_category(self):
        return st.selectbox(
            label = "What kind of content you are targeting to post",
            options=['Clothing', 'Cooking', 'Painting', 'Makeup']
        )

    def clothing_metadata(self):
        # right now we are making an assumption that whatever images we choose 
        # each product images will have those select sizes

        available_category = st.selectbox(
            "Please select the available sizes",
            options=['S', 'M', 'L', 'XL', 'XXL']
        )

        description = st.text_area(label="Please write a description of the product or how you want to make the post look like")
        prices = st.slider(
            label = "Select the price of range (Rs) and we will smartly set according to the user",
            min_value = 50,
            max_value= 10000
        )
        content_metadata = {
            'available_categories': available_category,
            'description': description,
            'prices': prices
        }
        return content_metadata

    def _plot_images_to_be_post(self, uploaded_contents):
        if uploaded_contents:
            st.write(
                f'<div style="display: flex; flex-direction: row;">',
                unsafe_allow_html=True
            )

            for content in uploaded_contents:
                image = Image.open(content)
                st.image(image, caption="Uploaded content", use_column_width=True)
            st.write('</div>', unsafe_allow_html=True)
   
    def run_content_upload(self):
        """Follows a set of tasks 
        > Starts by letting the user to upload the set of contents
        > Followed by choosing the type of the content
        > Followed by providing some metadata
        
        All of these should be saved inside the content bank object
        """
        title = st.text_input("Project name")
        # configure the content file upload folder
        
        content_upload_folder = os.path.join(METADATA_STORE, title.lower().replace(' ', '_'))
        if not os.path.exists(content_upload_folder):
            os.mkdir(content_upload_folder)

        uploaded_contents = self.upload_content()
        if uploaded_contents:
            choose_content_type = self.content_category()
            
            if choose_content_type == 'Clothing':
                clothing_metadata = self.clothing_metadata()
                clothing_sizes = clothing_metadata['available_categories']
                clothing_desc = clothing_metadata['description']
                
                generate_with_ai_button = st.button('Generate post caption')
                if generate_with_ai_button:
                    with st.chat_message("assistant"):
                        st.write("Check out my latest clothing collection")
                
                clothing_price = clothing_metadata['prices']
                submit_button = st.button(label="Submit")

                # once done we need to save all of these content inside our content bank repo
                # will be done soon
                # now save all the uploaded content
                
                if submit_button:
                    content = {
                            'clothing_sizes': clothing_sizes,
                            'clothing_desc': clothing_desc,
                            # we can incorporate a better strategy later
                            'estimated_price_range': [clothing_price - 100, clothing_price + 100],
                            # configure the required folders
                            'user_content_folder': os.path.join(content_upload_folder, 'user_content'),
                            'stability_ai_folder': os.path.join(content_upload_folder, 'stability_ai'),
                            'virtual_trial_folder': os.path.join(content_upload_folder, 'virtual_trial_folder')
                    }

                    # also make the folder structure for the ai generated at the same time
                    if not os.path.exists(content['user_content_folder']):
                        os.mkdir(content['user_content_folder'])

                    if not os.path.exists(content['stability_ai_folder']):
                        os.mkdir(content['stability_ai_folder'])
                    
                    if not os.path.exists(content['virtual_trial_folder']):
                        os.mkdir(content['virtual_trial_folder'])
                    
                    for upload in uploaded_contents:
                        image = Image.open(upload)
                        image.save(os.path.join(content_upload_folder, 'user_content', upload.name))
                    st.text('All the images saved successfully')
                    
                    # save the content inside json
                    # but before saving the content into json we have to merge two jsons
                    # hence load the existing, merge with the content 

                    existing_json = json.load(open(JSON_PATH, 'r'))
                    existing_json[title] = content
                    json.dump(existing_json, open(JSON_PATH, 'w'))

                if show_images := st.button('Show my uploaded images'):
                    st.markdown("### Here are your uploaded images.")
                    self._plot_images_to_be_post(uploaded_contents=uploaded_contents)
            else:
                st.text("More features comming soon")
            

if __name__ == '__main__':
    contents = ContentUpload().run_content_upload()