import requests

def check_cve(product, version):
    api_url = "https://vulners.com/api/v3/search/lucene/"
    query = f"{product} {version}"
    headers = {"User-Agent": "vulners-python-client"}

    response = requests.post(api_url, json={"query": query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data['data']['search']:
            print(f"CVE: {item['id']}")
            print(f"Description: {item['description']}")
            print(f"Link: {item['vhref']}\n")
    else:
        print("Failed to fetch data from Vulners API")

if __name__ == "__main__":
    software = input("Enter software name (e.g., Apache): ")
    version = input("Enter version (e.g., 2.4.51): ")
    check_cve(software, version)
