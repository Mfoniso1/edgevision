import cv2
from ultralytics import YOLO
import time

def run_edge_ai():
    # We are now using the shrunk (INT8) model for maximum speed
    print("Loading Shrunk AI Model (3.4MB)...")
    # Pointing to the int8 model generated in Step 3
    model = YOLO("yolov8n_saved_model/yolov8n_int8.tflite", task="detect") 

    print("Opening Security Camera...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera. Please make sure it's plugged in.")
        return

    print("--- SHOP SECURITY MODE ACTIVE ---")
    print("Watching for visitors...")
    
    visitor_count = 0
    is_person_present = False
    person_cooldown = 0
    start_time = time.time()
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Run AI on the current frame
        results = model(frame, stream=True, verbose=False)

        found_person = False
        annotated_frame = frame.copy()
        
        for r in results:
            # Filter for person (class 0)
            boxes = r.boxes
            for box in boxes:
                if int(box.cls[0]) == 0: # Person
                    found_person = True
                    # Draw only person boxes
                    x1, y1, x2, y2 = box.xyxy[0]
                    cv2.rectangle(annotated_frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                    cv2.putText(annotated_frame, "PERSON", (int(x1), int(y1)-10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Visitor Counter Logic
        if found_person:
            if not is_person_present and person_cooldown == 0:
                visitor_count += 1
                is_person_present = True
                print(f"🔔 ALERT: Visitor detected! Total: {visitor_count}")
            person_cooldown = 30
        else:
            if person_cooldown > 0:
                person_cooldown -= 1
            if person_cooldown == 0:
                is_person_present = False

        # Show UI stats
        fps = 1.0 / (time.time() - start_time)
        start_time = time.time()
        
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(annotated_frame, f"VISITORS: {visitor_count}", (20, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        if found_person:
            cv2.putText(annotated_frame, "!!! ALERT !!!", (20, 120), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        cv2.imshow("EdgeVision Security Monitor", annotated_frame)

        # Stop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("System stopped.")

if __name__ == "__main__":
    run_edge_ai()
