import requests

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
    }
for i in range(69390,70001):
    response = requests.get(f"https://www.deviceinfohw.ru/devices/item.php?item={i}",headers=header)
    if response.status_code == 200:
        # Save the HTML content to a file
        with open(f"pages/document{i}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("HTML document saved successfully.")
    else:
        print(f"Failed to download the document. Status code: {response.status_code}")
#108333