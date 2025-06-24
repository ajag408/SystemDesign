import requests

def download_image(url):
    response = requests.get(url)
    with open(url.split("/")[-1], "wb") as f:
        f.write(response.content)
    print(f"Image downloaded and saved")