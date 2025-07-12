# Zefoy Automation

This project automates some interactions with the Zefoy web service using Playwright.

## Requirements
- Python 3
- [Playwright](https://playwright.dev/python/)

## Usage
Install dependencies and run the script with the TikTok video URL:
```bash
pip install -r requirements.txt
playwright install --with-deps
python main.py --url "https://tiktok.com/<video>"
```

### GitHub Actions
A workflow is available under `.github/workflows/run-zefoy.yml`. Trigger it manually and provide the `video_url` input.

### Termux Install
For Termux on Android, run the provided script:
```bash
./termux-install.sh
```
Then execute the script with the desired video URL.
