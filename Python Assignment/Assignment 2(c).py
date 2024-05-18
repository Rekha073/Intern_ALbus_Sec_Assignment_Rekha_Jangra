import urllib.request

def send_get_request(url):
    try:
        response = urllib.request.urlopen(url)
        print("Request successful!")
        print("Response:")
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    url = input("Enter the URL to send the GET request to: ")
    send_get_request(url)
