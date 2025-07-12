import asyncio
from playwright.async_api import async_playwright
import argparse

async def main(video_url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://zefoy.com")
        print("✅ فتح الموقع... استنى 20 ثانية لحل الكابتشا يدويًا")
        await asyncio.sleep(20)  # لازم تحل الكابتشا يدوي من المرة الأولى

        async def send_service(service_name):
            try:
                print(f"🔄 محاولة إرسال: {service_name}")
                await page.click(f"text={service_name}")
                await asyncio.sleep(5)

                await page.fill('input[placeholder="Enter TikTok video URL"]', video_url)
                await asyncio.sleep(2)
                await page.click("text=Search")
                await asyncio.sleep(15)
                await page.go_back()
                await asyncio.sleep(5)
            except Exception as e:
                print(f"❌ خطأ في {service_name}: {e}")
                await page.go_back()

        while True:
            await send_service("TikTok views")
            await send_service("TikTok likes")
            print("⏳ استراحة 5 دقائق...")
            await asyncio.sleep(300)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zefoy automation")
    parser.add_argument("--url", required=True, help="TikTok video URL")
    args = parser.parse_args()
    asyncio.run(main(args.url))
