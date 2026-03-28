# APK Conversion Guide: EdgeVision

Follow these steps to convert your `mobile-app` folder into a professional Android APK that works 100% offline.

## Option 1: WebIntoApp (Easiest & Fastest)
Ideal for a quick portfolio demo.
1. Go to [WebIntoApp.com](https://www.webintoapp.com/).
2. Select **"Online"** and enter a placeholder (we will upload files later) OR better: Zip your `mobile-app` folder.
3. Upload the Zip containing `index.html`, `manifest.json`, `sw.js`, and the `model/` folder.
4. Set the App Name to **"EdgeVision"**.
5. Download the `.apk` file and install it on your phone.

## Option 2: Bubblewrap (Professional CLI)
Best for production and Google Play Store.
1. Install the CLI: `npm install -g @bubblewrap/cli`.
2. Initialize: `bubblewrap init --manifest=https://your-hosted-url/manifest.json`.
3. Build: `bubblewrap build`.
4. This will generate a signed APK.

## Critical for Offline
- The `sw.js` (Service Worker) allows the app to load even without internet.
- Ensure your phone's browser (Chrome) has "Installed" the app to the home screen first to test the PWA behavior.
- Once it's an APK, it will bundle these files and run them locally using an internal webview.

## Troubleshooting
- **Camera Permission**: Android 10+ requires explicit permission. The app will prompt for it on first launch.
- **Model Loading**: The 3.4MB model is stored in the app's cache, so it starts instantly after the first run.
