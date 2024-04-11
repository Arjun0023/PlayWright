const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://www.google.com/');
  await page.getByLabel('Search', { exact: true }).click();
  await page.getByLabel('Search', { exact: true }).fill('zoho crm login');
  await page.getByRole('link', { name: 'Sign in to Zoho CRM Zoho' }).click();
  await page.getByRole('link', { name: 'SIGN IN' }).click();
  await page.getByPlaceholder('Email address or mobile number').click();
  await page.getByPlaceholder('Email address or mobile number').fill('arjunpawar0023@gmail.com');
  await page.getByRole('button', { name: 'Next' }).click();
  await page.getByPlaceholder('Enter password').fill('!@#123letsgoo');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.getByRole('button', { name: 'Skip for now' }).click();
  await page.getByRole('link', { name: 'Leads' }).click();
  await page.getByRole('button', { name: 'Create Lead' }).click();
  await page.locator('#Crm_Leads_DESIGNATION_LInput').click();
  await page.locator('#Crm_Leads_DESIGNATION_LInput').fill('manager');
  await page.locator('#Crm_Leads_PHONE_LInput').click();
  await page.locator('#Crm_Leads_PHONE_LInput').fill('9822');
  await page.locator('#Crm_Leads_COMPANY #inputId').click();
  await page.locator('#Crm_Leads_COMPANY #inputId').fill('abc company');
  await page.locator('#Crm_Leads_LASTNAME_LInput').click();
  await page.locator('#Crm_Leads_LASTNAME_LInput').fill('last');
  await page.getByRole('button', { name: 'Save', exact: true }).click();
  await page.getByRole('link', { name: 'Accounts' }).click();
  await page.getByRole('button', { name: 'Create Account' }).click();
  await page.locator('#Crm_Accounts_ACCOUNTNAME_LInput').click();
  await page.locator('#Crm_Accounts_ACCOUNTNAME_LInput').fill('new account');
  await page.getByRole('button', { name: 'Save', exact: true }).click();

  // ---------------------
  await context.close();
  await browser.close();
})();