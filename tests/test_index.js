const { chromium } = require('playwright');
const data = require('./data.json'); // Assuming your JSON file is named data.json

(async () => {
  const browser = await chromium.launch({
    headless: false
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://www.google.com/search?q=zoho+crm+login&oq=zoho+crm+login&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDc5ODVqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8');

  await page.getByRole('link', { name: 'Sign in to Zoho CRM Zoho' }).click();
  await page.waitForNavigation(); // Wait for navigation to complete

  await page.getByRole('link', { name: 'SIGN IN' }).click();
  await page.waitForNavigation(); // Wait for navigation to complete

  // Fill in email
  await page.getByPlaceholder('Email address or mobile number').fill(data.email);
  await page.getByRole('button', { name: 'Next' }).click();
  await page.waitForNavigation(); // Wait for navigation to complete

  // Fill in password
  await page.getByPlaceholder('Enter password').fill(data.password);
  await page.press('Enter');
  await page.waitForNavigation(); // Wait for navigation to complete

  // Skip for now
  await page.getByRole('button', { name: 'Skip for now' }).click();
  await page.waitForNavigation(); // Wait for navigation to complete

  // Go to Leads
  await page.getByRole('link', { name: 'Leads' }).click();
  await page.waitForNavigation(); // Wait for navigation to complete

  // Create lead
  await page.getByRole('button', { name: 'Create Lead' }).click();
  await page.waitForNavigation(); // Wait for navigation to complete

  // Fill lead information
  await page.locator('#Crm_Leads_COMPANY #inputId').fill(data.company);
  await page.locator('#Crm_Leads_LASTNAME_LInput').fill(data.lastName);

  // Save lead
  await page.getByRole('button', { name: 'Save and New' }).click();
  
  // ---------------------
  await context.close();
  await browser.close();
})();
