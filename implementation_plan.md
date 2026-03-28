# Implementation Plan: Smart Security Lookout (Option 1)

This project transforms a standard phone or tablet into an offline security monitor for Nigerian shops and kiosks.

## Goal
Detect people entering a shop or kiosk and provide real-time alerts without needing an internet connection.

## Technical Details
- **Model**: YOLOv8-nano (INT8 Quantized, 3.4 MB).
- **Library**: Ultralytics + OpenCV for processing.
- **Environment**: Offline-first, running on edge hardware.

## Key Features to Implement
1. **Entry Detection**: Alert when a "person" is detected in the frame.
2. **Visual Alert**: Draw a bright red box when someone is in the shop.
3. **Audio Alert**: (Future step) Play a 'Welcome' or 'Alert' sound.
4. **Traffic Logging**: Count how many people visited throughout the day.

## Success Metrics
- Works 100% without internet.
- High speed (low latency) on standard hardware.
- Small footprint (fits on any cheap android phone).
