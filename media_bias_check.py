from bs4 import BeautifulSoup
import requests


def run_bias_check():
    user_input = input("What site to check: ").lower().strip()
    user_input = user_input.replace(" ", "-")
    site = f"https://mediabiasfactcheck.com/{user_input}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(site, headers=headers)

        # Try fallback URL if the primary one 404s
        if response.status_code == 404:
            site = f"https://mediabiasfactcheck.com/{user_input}-bias/"
            response = requests.get(site, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            #find bias level
            title_element = soup.find("span", style="text-decoration: underline;")

            if title_element:
                print("\n--- Result Found ---")
                print(title_element.text.strip())
            else:
                print("Could not find the title element on the page.")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            print("Tip: Use the exact slug name (e.g., 'wall-street-journal').")

    except Exception as e:
        print(f"An error occurred: {e}")


run_bias_check()
