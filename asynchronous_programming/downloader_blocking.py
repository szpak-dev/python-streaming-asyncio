import json
import urllib.request


def read_urls_from_json(file_name: str):
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                for url in data:
                    try:
                        response = urllib.request.urlopen(url)
                        response.read()
                        print(f"Successfully read from {url}")
                    except Exception as e:
                        print(f"Error reading from {url}: {e}")
            else:
                print("Error: JSON file does not contain a list of URLs")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")


if __name__ == "__main__":
    read_urls_from_json('websites.json')
