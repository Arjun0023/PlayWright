const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://www.google.com/search?q=zoho+crm+login&oq=zoho+crm+login&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDc5ODVqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8');
  await page.getByRole('link', { name: 'Sign in to Zoho CRM Zoho' }).click();
  // await expect(page.getByRole('main')).toContainText('SIGN IN');
  await page.getByRole('link', { name: 'SIGN IN' }).click();
  await page.getByPlaceholder('Email address or mobile number').click();
  await page.getByPlaceholder('Email address or mobile number').fill('arjunpawar0023@gmail.com');
  await page.getByRole('button', { name: 'Next' }).click();
  await page.getByPlaceholder('Enter password').click();
  await page.getByPlaceholder('Enter password').fill('!@#123letsgoo');
  await page.getByPlaceholder('Enter password').press('Enter');
  await page.getByRole('button', { name: 'Skip for now' }).click();
  // await expect(page.locator('#Visible_Leads')).toContainText('Leads');
  await page.getByRole('link', { name: 'Leads' }).click();
  await page.getByRole('button', { name: 'Create Lead' }).click();
  await page.locator('#Crm_Leads_COMPANY #inputId').click();
  await page.locator('#Crm_Leads_COMPANY #inputId').fill('asd');
  await page.locator('#Crm_Leads_LASTNAME_LInput').fill('sa');
  await page.locator('#Crm_Leads_LASTNAME_LInput').click();
  await page.locator('#Crm_Leads_LASTNAME_LInput').fill('saasd');
  // await expect(page.locator('#crm_create_savebutn')).toContainText('Save');
  await page.getByRole('button', { name: 'Save and New' }).click();

  // ---------------------
  await context.close();
  await browser.close();
})();