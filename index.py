import requests

url = "https://api.europe-west1.gcp.commercetools.com/composable-bm-commerce/products"
access_token = "LYD8VmCe_YKhmuxQrTmGaFdAUWWBXaEb"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("API response:")
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")

