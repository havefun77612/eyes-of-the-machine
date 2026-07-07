"""
smart_filter.py — Eyes of the Machine (Chapter 9)
Author: A.L Hossam A. Abdelwahab

A reusable smart filter that detects faces in images using OpenCV's
Haar Cascade classifier and applies various effects.

Usage:
    python smart_filter.py <image_path> [effect]

Effects:
    box         Draw green rectangles around faces (default)
    blur        Apply privacy blur to faces
    sunglasses  Overlay sunglasses on faces
    census      Number each face with random colors

Requires:
    pip install opencv-python numpy
"""

import cv2 as cv
import numpy as np
import sys
import os


def load_face_cascade():
    """Load the pre-trained face detection cascade."""
    cascade_path = cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
    cascade = cv.CascadeClassifier(cascade_path)
    if cascade.empty():
        raise RuntimeError("Failed to load face cascade. Check OpenCV installation.")
    return cascade


def detect_faces(image, cascade):
    """Detect faces in a grayscale image."""
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return faces


def apply_effect(image, faces, effect='box'):
    """Apply the selected effect to detected face regions."""
    result = image.copy()

    for i, (x, y, w, h) in enumerate(faces):
        if effect == 'blur':
            face_region = result[y:y+h, x:x+w]
            blurred = cv.GaussianBlur(face_region, (99, 99), 30)
            result[y:y+h, x:x+w] = blurred

        elif effect == 'sunglasses':
            glasses_y = y + h // 4
            glasses_h = h // 6
            cv.rectangle(result, (x + 5, glasses_y),
                         (x + w // 2 - 5, glasses_y + glasses_h), (0, 0, 0), -1)
            cv.rectangle(result, (x + w // 2 + 5, glasses_y),
                         (x + w - 5, glasses_y + glasses_h), (0, 0, 0), -1)
            cv.rectangle(result, (x + w // 2 - 5, glasses_y + glasses_h // 3),
                         (x + w // 2 + 5, glasses_y + 2 * glasses_h // 3), (0, 0, 0), -1)

        elif effect == 'census':
            color = (int(np.random.randint(0, 256)),
                     int(np.random.randint(0, 256)),
                     int(np.random.randint(0, 256)))
            cv.rectangle(result, (x, y), (x + w, y + h), color, 3)
            cv.putText(result, str(i + 1), (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        else:  # 'box' (default)
            cv.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 3)

    return result


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python smart_filter.py <image_path> [effect]")
        print("Effects: box, blur, sunglasses, census")
        sys.exit(1)

    image_path = sys.argv[1]
    effect = sys.argv[2] if len(sys.argv) > 2 else 'box'

    if not os.path.exists(image_path):
        print(f"Error: File not found: {image_path}")
        sys.exit(1)

    print(f"Loading image: {image_path}")
    image = cv.imread(image_path)
    if image is None:
        print(f"Error: Could not load image: {image_path}")
        sys.exit(1)

    print("Loading face cascade...")
    cascade = load_face_cascade()

    print("Detecting faces...")
    faces = detect_faces(image, cascade)
    print(f"Found {len(faces)} face(s)")

    print(f"Applying effect: {effect}")
    result = apply_effect(image, faces, effect)

    output_path = f"filtered_{os.path.basename(image_path)}"
    cv.imwrite(output_path, result)
    print(f"Result saved as: {output_path}")

    print("\nDone! Open the image to see the result.")


if __name__ == "__main__":
    main()
