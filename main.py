import requests

exec(open("wheel_animator.py").read())

with open('C:\HMV_Wheel_Bot\gifs\wheel_animation.gif', 'rb') as f:
    url = 'https://image.groupme.com/pictures'
    headers = {
        'X-Access-Token': 'Y6zlQeICdyeVSX3EzYgkRxy9NVJ0I5vrFFOo1vDF',
        'Content-Type': 'image/gif'
    }
    response = requests.post(url, headers=headers, data=f)
    json_response = response.json()
    image_url = json_response['payload']['url']

def send_to_groupme(image_url, bot_id):
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

BOT_ID = 'f45ebc2df8db803590f827982e'
send_to_groupme(image_url, BOT_ID)


