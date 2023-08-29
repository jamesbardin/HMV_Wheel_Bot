from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GROUPME_IMAGE_SERVICE_URL = "https://image.groupme.com/pictures"
BOT_ID = "f45ebc2df8db803590f827982e"

@app.route('/groupme_webhook', methods=['POST'])
def groupme_webhook():
    # Parse the incoming message
    message = request.json.get("text", "").strip().lower()

    if "spin the wheel" in message:

        # generate wheel gif
        exec(open("wheel_animator.py").read())

        gif_url = upload_gif_to_groupme('gifs/wheel_animation.gif')
        
        # Send the GIF back to the chat
        send_gif_to_groupme_chat(gif_url)

    return jsonify(success=True)

def upload_gif_to_groupme(bot_id):
    with open('C:\HMV_Wheel_Bot\gifs\wheel_animation.gif', 'rb') as f:
        image_url = 'https://image.groupme.com/pictures'
        headers = {
            'X-Access-Token': 'Y6zlQeICdyeVSX3EzYgkRxy9NVJ0I5vrFFOo1vDF',
            'Content-Type': 'image/gif'
        }
        response = requests.post(url, headers=headers, data=f)
        json_response = response.json()
        image_url = json_response['payload']['url']
        return image_url

def send_gif_to_groupme_chat(bot_id, image_url):
    post_url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': bot_id,
        'attachments': [
            {
                'type': 'image',
                'url': image_url
            }
        ]
    }
    response = requests.post(post_url, json=data)
    print(response.status_code)
    return response.status_code

if __name__ == "__main__":
    app.run(port=5000)
