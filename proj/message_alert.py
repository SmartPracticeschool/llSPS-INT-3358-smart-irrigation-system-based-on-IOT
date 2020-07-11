import requests

r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=eWXmR37ubZGbnHnnDYa6lTVt2CPCBt1X7T1FY48JR5BFC2PkXQyGIEvlW3XJ&sender_id=FSTSMS&message=Thisistestmessage&language=english&route=p&numbers=8929691463')

print(r.status_code)               
