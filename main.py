from playwright.sync_api import sync_playwright
import json

# JSON data for the form
form_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "This is a test message."
}

# Function to fill the form
def fill_form(page, data):
    # Fill name field
    page.fill('input[name="name"]', data["name"])
    
    # Fill email field
    page.fill('input[name="email"]', data["email"])
    
    # Fill message field
    page.fill('textarea[name="message"]', data["message"])

# Main function to run the script
def main():
    # Initialize Playwright with WebKit (Brave uses WebKit)
    with sync_playwright() as p:
        # Launch Brave browser
        browser = p.webkit.launch()
        
        # Create a new page
        page = browser.new_page()
        
        # Navigate to the form page
        page.goto('https://example.com/form')
        
        # Wait for the form elements to be visible
        page.wait_for_selector('input[name="name"]')
        
        # Fill the form with data
        fill_form(page, form_data)
        
        # Wait for a moment to see the filled form
        page.wait_for_timeout(2000)
        
        # Close the browser
        browser.close()

# Execute the main function
if __name__ == "__main__":
    main()
