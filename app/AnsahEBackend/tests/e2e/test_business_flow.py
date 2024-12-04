import pytest
from playwright.sync_api import Page, expect

def test_business_onboarding(page: Page):
    page.goto("/onboarding")
    
    # Fill out the onboarding form
    page.fill("input[name='business_name']", "Test Business")
    page.fill("input[name='business_type']", "E-commerce")
    page.fill("input[name='website']", "https://testbusiness.com")
    page.fill("input[name='contact_email']", "contact@testbusiness.com")
    page.fill("input[name='support_email']", "support@testbusiness.com")
    page.fill("textarea[name='return_policy']", "30-day return policy")
    page.fill("textarea[name='delivery_policy']", "Free shipping on orders over $50")
    page.fill("textarea[name='refund_policy']", "Full refund within 14 days")
    
    # Submit the form
    page.click("button[type='submit']")
    
    # Check if we're redirected to the dashboard
    expect(page).to_have_url("/dashboard")
    
    # Verify that the business info is displayed correctly
    expect(page.locator("text=Test Business")).to_be_visible()
    expect(page.locator("text=E-commerce")).to_be_visible()

