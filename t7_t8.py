import requests

URL = "https://e7zknnccyg.execute-api.eu-west-2.amazonaws.com/tech/campaign/sms/send"
SMS_TOKEN = "6kx2wsw8jn"
API_KEY = "lTFdxeFyJs6kyr6Z9EKd5Yy8sCn68gP2lHukvui3"

def send_sms_comms(campaign_name: str, template_id: int) -> int:

    if not isinstance(campaign_name, str) or not campaign_name:
        raise TypeError("campaign_name must be a non-empty string")
    if not isinstance(template_id, int) or isinstance(template_id, bool):
        raise TypeError("template_id must be an int")

    headers = {"x-sms-token": SMS_TOKEN, "x-api-key": API_KEY}
    body = {"campaign_name": campaign_name, "template_id": template_id}

    response = requests.post(URL, json=body, headers=headers, timeout=10)

    print(response.status_code, response.text)

    return response.status_code

## Test Cases
#T8
send_sms_comms("eon_next_tech_test", 87532)
