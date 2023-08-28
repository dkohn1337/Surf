import requests
import concurrent.futures
import time
from datetime import datetime, timedelta
from surftoken import token

API_ENDPOINT = "https://api-prod.surfsight.net/v2/devices/864004046618952/virtual-event"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}


json_payload_template = {
    "time": None,
    "mediaType": "video",
    "durationSeconds": 10,
    "quality": "high",
    "metadata": "string"
}

def make_post_request(url, payload):
    try:
        response = requests.post(url, headers=headers, json=payload)
        response_code = response.status_code
        response_text = response.text
        return response_code, response_text
    except requests.exceptions.RequestException as e:
        return None, str(e)

def main():
    start_time = datetime(2023, 8, 23, 6, 0, 0)  # Set the initial start time
    end_time = start_time + timedelta(minutes=3)

    while datetime.now() < end_time:
        for _ in range(3):
            current_time = start_time  # Reset the current time for each set
            for _ in range(3):
                payload = json_payload_template.copy()
                payload["time"] = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")

                with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                    results = list(executor.map(make_post_request, [API_ENDPOINT]*3, [payload]*3))

                for i, (response_code, response_text) in enumerate(results):
                    if response_code is not None:
                        print(f"Request {i+1} - Time: {current_time} - Response Code: {response_code}")
                        print(f"Response Text:\n{response_text}\n")
                    else:
                        print(f"Request {i+1} - Time: {current_time} - Error: {response_text}")

                current_time += timedelta(seconds=12)  # Increment the time

            time.sleep(1)  # Sleep for 1 second within the 1-second interval

        time.sleep(5)  # Sleep for 5 seconds between sets

if __name__ == "__main__":
    main()
