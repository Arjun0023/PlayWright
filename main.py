import json
from playwright.sync_api import sync_playwright

def fill_form(page, data):
    for field, value in data.items():
        page.fill(f"input[name='{field}']", value)

def main():
    # Load data from JSON file
    with open('form_data.json') as json_file:
        form_data = json.load(json_file)

    # Launch browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the website
        page.goto('https://docs.google.com/forms/d/e/1FAIpQLScAFKI1fZ1cXhBmSp2HM93Jvuc8Jvrxh5iSbkKhtwKN-OHoTQ/viewform')

        # Fill the form
        fill_form(page, form_data)

        # You may need to adjust this according to your website's submit button selector
        page.click('button[type="submit"]')

        # Wait for navigation, you may need to adjust the URL for successful navigation
        page.wait_for_navigation()

        # Optional: Take a screenshot of the filled form
        page.screenshot(path='filled_form.png')

        browser.close()

if __name__ == "__main__":
    main()
