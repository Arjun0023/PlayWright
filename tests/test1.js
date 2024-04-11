import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://www.google.com/search?q=zohocrm+login&oq=zohocrm+login&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDUzMTRqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8');
  await page.getByRole('link', { name: 'Sign in to Zoho CRM Zoho' }).click();
  await page.getByRole('link', { name: 'SIGN IN' }).click();
  await page.getByPlaceholder('Email address or mobile number').click();
  await page.getByPlaceholder('Email address or mobile number').fill('arjunpawar0023@gmail.com');
  await page.getByPlaceholder('Email address or mobile number').press('Enter');
  await page.getByPlaceholder('Enter password').fill('!@#123letsgoo');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.getByRole('button', { name: 'Skip for now' }).click();
  await page.getByRole('link', { name: 'Leads' }).click();
  await page.getByRole('button', { name: 'Create Lead' }).click();
  await page.locator('#Crm_Leads_COMPANY #inputId').click();
  await page.locator('#Crm_Leads_COMPANY #inputId').fill('asd');
  await page.locator('#Crm_Leads_LASTNAME_LInput').click();
  await page.locator('#Crm_Leads_LASTNAME_LInput').fill('dsa');
  await page.getByRole('button', { name: 'Save', exact: true }).click();
  await page.getByRole('button', { name: 'Send Email' }).click();
  await page.getByRole('button', { name: 'Ok' }).click();
  await page.locator('#backArrowDV').click();
  await page.getByPlaceholder('Search', { exact: true }).click();
  await page.getByPlaceholder('Search', { exact: true }).fill('dsa');
  await page.locator('#selectEntity_662012000000333001 span').first().click();
});