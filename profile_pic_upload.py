import requests

def upload_to_groupme_image_service(image_path, access_token):
    with open(image_path, 'rb') as f:
        url = 'https://image.groupme.com/pictures'
        headers = {
            'X-Access-Token': access_token,
            'Content-Type': 'image/jpeg'  # adjust if your image is of a different type
        }
        response = requests.post(url, headers=headers, data=f)
        
        if response.status_code == 200:
            return response.json()['payload']['url']
        else:
            print("Error:", response.status_code, response.text)
            return None

# Usage
ACCESS_TOKEN = 'Y6zlQeICdyeVSX3EzYgkRxy9NVJ0I5vrFFOo1vDF'
IMAGE_PATH = 'C:\HMV_Wheel_Bot\pfp\pfp.PNG'

uploaded_image_url = upload_to_groupme_image_service(IMAGE_PATH, ACCESS_TOKEN)

if uploaded_image_url:
    print("Image successfully uploaded!")
    print("Image URL:", uploaded_image_url)
else:
    print("Image upload failed.")
