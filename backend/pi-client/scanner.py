import requests

API_URL = "http://192.168.1.155:5000/scan"

def send_scan(barcode):
    try:
        response = requests.post(API_URL, json={"barcode": barcode})
        if response.ok:
            data = response.json()
            print(f"Scanned: {barcode} | Quantity: {data.get('quantity')}")
        else:
            print(f"Failed to send barcode {barcode}: {response.text}")
    except Exception as e:
        print(f"Error sending barcode {barcode}: {e}")

def main():
    print("Ready to scan barcodes. Press Ctrl+C to exit.")
    while True:
        try:
            barcode = input().strip()
            if barcode:
                send_scan(barcode)
        except KeyboardInterrupt:
            print("\nExiting scanner.")
            break

if __name__ == "__main__":
    main()

