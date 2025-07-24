import requests
import os
import re

esp32_ip = "192.168.1.126"
url = f"http://{esp32_ip}/capture"

# Folder to save images
save_folder = "images"
os.makedirs(save_folder, exist_ok=True)

# Automatically find the next image number
existing_files = [f for f in os.listdir(save_folder) if re.match(r"t\d+\.jpg", f)]
numbers = [int(re.findall(r"t(\d+)\.jpg", f)[0]) for f in existing_files]

next_number = max(numbers) + 1 if numbers else 1
filename = os.path.join(save_folder, f"t{next_number}.jpg")

# Try capturing the image
try:
    print(f"Capturing image {next_number} from {url}...")
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Saved image as {filename}")
    else:
        print(f"Error: Received status code {response.status_code}")

except Exception as e:
    print("Failed to download:", e)
