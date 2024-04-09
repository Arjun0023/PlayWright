import json
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Read data from JSON file
    with open('data.json') as f:
        data = json.load(f)

    page.goto("https://www.google.com/search?q=zoho+crm&sca_esv=be2d3384baa617c2&sca_upv=1&sxsrf=ACQVn093PMUVcvZmWZ4Lu9vdXNYx6iNmGA%3A1712687385764&source=hp&ei=GYkVZqH2KdOVseMPlIec4A8&iflsig=ANes7DEAAAAAZhWXKRsNPIjNaL0U_RAxESIDzbWE7bH9&ved=0ahUKEwjh5vDZ4bWFAxXTSmwGHZQDB_wQ4dUDCBU&uact=5&oq=zoho+crm&gs_lp=Egdnd3Mtd2l6Igh6b2hvIGNybTILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgUQABiABDIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgARI2A9QAFjDDXAAeACQAQCYAX6gAawHqgEDMC44uAEDyAEA-AEBmAIIoALMB8ICChAjGIAEGIoFGCfCAhoQLhiDARjHARiRAhjUAhixAxjRAxiABBiKBcICFxAuGIAEGIoFGJECGLEDGIMBGMcBGNEDwgIREC4YgAQYsQMYgwEYxwEY0QPCAhkQLhhDGIMBGMcBGNQCGLEDGNEDGIAEGIoFwgINEAAYgAQYigUYQxixA8ICEBAAGIAEGIoFGEMYsQMYgwHCAhAQLhiABBiKBRhDGMcBGNEDwgIWEC4YgAQYigUYQxixAxiDARjHARjRA8ICFhAuGEMYgwEYxwEYsQMY0QMYgAQYigXCAhMQLhiABBiKBRhDGLEDGMcBGNEDmAMA4gMFEgExIECSBwMwLjigB_4_&sclient=gws-wiz")
    page.get_by_role("link", name="Zoho CRM | Top-rated Sales").click()

    # Fill Full Name
    full_name_input = page.locator('input[placeholder="Full Name"]')
    full_name_input.fill(data["full_name"])
    print("Full Name filled:", data["full_name"])

    # Fill Email
    email_input = page.locator('input[placeholder="Email address or mobile number"]')
    email_input.fill(data["email"])
    print("Email filled:", data["email"])

    # Fill Password
    password_input = page.locator('input[placeholder="Enter your password"]')
    password_input.fill(data["password"])
    print("Password filled:", data["password"])

    # Wait for some time to observe the filled inputs
    page.wait_for_timeout(3000)

with sync_playwright() as playwright:
    run(playwright)
