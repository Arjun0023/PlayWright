const { chromium } = require('playwright');
const fs = require('fs').promises;

(async () => {
  const data = await fs.readFile('data.json', 'utf-8');
  console.log(JSON.parse(data))
  const { email, password, companyName, lastName } = JSON.parse(data);
  console.log( email, password, companyName, lastName )
  const browser = await chromium.launch({
    headless: false
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://www.google.com/search?q=zoho+crm+login&oq=zoho+crm+login&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDc5ODVqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8');
  await page.getByRole('link', { name: 'Sign in to Zoho CRM Zoho' }).click();
  await page.getByRole('link', { name: 'SIGN IN' }).click();
  await page.getByPlaceholder('Email address or mobile number').click();
  await page.getByPlaceholder('Email address or mobile number').fill(email);
  await page.getByRole('button', { name: 'Next' }).click();
  await page.getByPlaceholder('Enter password').click();
  await page.getByPlaceholder('Enter password').fill(password);
  await page.getByPlaceholder('Enter password').press('Enter');
  await page.getByRole('button', { name: 'Skip for now' }).click();
  await page.getByRole('link', { name: 'Leads' }).click();
  await page.getByRole('button', { name: 'Create Lead' }).click();
  //await page.locator('#Crm_Leads_COMPANY #inputId').click();
  await page.locator('#Crm_Leads_COMPANY #inputId').fill(companyName);
  await page.locator('#Crm_Leads_LASTNAME_LInput').fill(lastName);
  await page.getByRole('button', { name: 'Save and New' }).click();

  // ---------------------
  //await context.close();
  //await browser.close();
})();
