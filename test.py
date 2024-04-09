import json
from playwright.sync_api import sync_playwright , Playwright , expect

def run(playwright: Playwright)->None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=zoho+crm&sca_esv=be2d3384baa617c2&sca_upv=1&sxsrf=ACQVn093PMUVcvZmWZ4Lu9vdXNYx6iNmGA%3A1712687385764&source=hp&ei=GYkVZqH2KdOVseMPlIec4A8&iflsig=ANes7DEAAAAAZhWXKRsNPIjNaL0U_RAxESIDzbWE7bH9&ved=0ahUKEwjh5vDZ4bWFAxXTSmwGHZQDB_wQ4dUDCBU&uact=5&oq=zoho+crm&gs_lp=Egdnd3Mtd2l6Igh6b2hvIGNybTILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIFEAAYgAQyCxAAGIAEGLEDGIMBMgUQABiABDIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgARI2A9QAFjDDXAAeACQAQCYAX6gAawHqgEDMC44uAEDyAEA-AEBmAIIoALMB8ICChAjGIAEGIoFGCfCAhoQLhiDARjHARiRAhjUAhixAxjRAxiABBiKBcICFxAuGIAEGIoFGJECGLEDGIMBGMcBGNEDwgIREC4YgAQYsQMYgwEYxwEY0QPCAhkQLhhDGIMBGMcBGNQCGLEDGNEDGIAEGIoFwgINEAAYgAQYigUYQxixA8ICEBAAGIAEGIoFGEMYsQMYgwHCAhAQLhiABBiKBRhDGMcBGNEDwgIWEC4YgAQYigUYQxixAxiDARjHARjRA8ICFhAuGEMYgwEYxwEYsQMY0QMYgAQYigXCAhMQLhiABBiKBRhDGLEDGMcBGNEDmAMA4gMFEgExIECSBwMwLjigB_4_&sclient=gws-wiz")
    page.get_by_role("link" , name = "Zoho CRM | Top-reated Sales").click()
    page.locator("#header").get_by_role("link" , name = "SIGN IN").click()
    page.get_by_role("Email address or mobile number").fill("arjunp0023@gmail.com")
    page.get_by_role("button", name="Next").click()
    page.get_by_placeholder("Email address or mobile number").click()
    page.get_by_placeholder("Email address or mobile number").press("ArrowLeft")
    page.get_by_placeholder("Email address or mobile number").press("ArrowLeft")
    page.get_by_placeholder("Email address or mobile number").fill("arjunp0023@gmail.com")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_placeholder("Enter password").fill("asdasd")
    page.get_by_role("button", name="Sign in").click()
    #
    page.get_by_role("link", name="Leads").click()
    page.get_by_role("button", name= "Create Lead").click()
    page.locator("#Crm_Leads_SMOWNERID lyte-icon").click()
    page.locator("#Crm_Leads_Lead_Information").click()
    page.locator("#Crm_Leads_FIRSTNAME_LInput").click()
    page.locator("#Crm_Leads_FIRSTNAME_SALTUATION lyte-drop-button").click()
    page.get_by_role("option", name="Mr.").click()
    page.locator("#Crm_Leads_FIRSTNAME_LInput").fill("Arjun")
    page.locator("#Crm_Leads_FIRSTNAME_LInput").press("Tab")
    page.locator("#Crm_Leads_LASTNAME_LInput").fill("Prakash3")
    page.locator("#Crm_Leads_COMPANY #inputId").click()
    page.locator("#Crm_Leads_COMPANY #inputId").fill("c2crm")
    page.locator("#Crm_Leads_DESIGNATION_LInput").click()
    page.locator("#Crm_Leads_DESIGNATION_LInout").press("CapsLock")

with sync_playwright() as playwright:
    run(playwright)
