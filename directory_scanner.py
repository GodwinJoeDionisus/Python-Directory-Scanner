import requests

target = input("Enter target URL (example: http://example.com): ")

print("\nStarting Directory Scan...\n")

with open("directories.txt") as file:
    directories = file.read().splitlines()

for directory in directories:
    url = f"{target}/{directory}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[FOUND] {url}")

    except requests.ConnectionError:
        pass

print("\nScan Completed.")