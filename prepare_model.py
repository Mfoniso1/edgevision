import os
from ultralytics import YOLO

def prepare_model():
    print("Step 1: Downloading the small but powerful YOLOv8-nano model...")
    # This will download yolov8n.pt (approx 6MB)
    model = YOLO("yolov8n.pt")
    
    print("\nStep 2: Exporting to TFLite (The 'Universal' mobile format)...")
    # Exporting to TFLite makes it compatible with most phones
    model.export(format="tflite")
    
    print("\nStep 3: The 'Shrink' Step - Quantizing for Edge Speed...")
    # INT8 Quantization makes it 4x smaller and much faster on mobile CPUs
    # We use 'int8=True' to perform post-training quantization.
    model.export(format="tflite", int8=True)
    
    print("\nSUCCESS! Your offline AI models are ready in the 'yolov8n_saved_model' folder.")

if __name__ == "__main__":
    prepare_model()
