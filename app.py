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

    # Login
    page.locator('input[placeholder="Email address or mobile number"]').fill(data["email"])
    page.get_by_role("button", name="Next").click()
    page.locator('input[placeholder="Enter your password"]').fill(data["password"])
    page.get_by_role("button", name="Sign in").click()

    # Wait for login to complete
    page.wait_for_navigation()

    # Click on Leads
    page.get_by_role("link", name="Leads").click()

    # Click on Create Lead
    page.get_by_role("button", name="Create Lead").click()

    # Fill the form
    page.get_by_role("option", name=data["salutation"]).click()
    page.get_by_placeholder("First Name").fill(data["first_name"])
    page.get_by_placeholder("Last Name").fill(data["last_name"])
    page.get_by_placeholder("Company").fill(data["company"])
    page.get_by_placeholder("Designation").fill(data["designation"])

with sync_playwright() as playwright:
    run(playwright)
