import asyncio
from playwright.async_api import async_playwright

async def run():
    print("🚀 Starting Playwright Browser...")
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("🌐 Navigating to GitHub...")
        await page.goto("https://github.com")
        
        screenshot_path = "github_screenshot.png"
        await page.screenshot(path=screenshot_path)
        print("saved successfully!")
        
        await browser.close()
        print("✅ Process finished successfully!")

if __name__ == "__main__":
    asyncio.run(run())