import json
from playwright.sync_api import sync_playwright

with open('data.json') as f:
    data = json.load(f)

def fill_form(page, data):
    for key, value in data.items():
        field = page.locator(f'input[name="{key}"]')
        field.fill(value)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://crm.zoho.in/crm/org60028443671/tab/Leads/custom-view/669791000000029342/list")
        create_lead_button = page.locator("//button[text()='Create Lead']")
        create_lead_button.click()
        fill_form(page, data)
        
        # Submit the form
        submit_button = page.locator("//button[text()='Submit']")
        submit_button.click()
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()
