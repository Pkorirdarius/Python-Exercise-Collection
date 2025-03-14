import cv2
import streamlit as st

# Load the pre-trained face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame, scaleFactor, minNeighbors, color):
    """
    Detect faces in a frame using the Viola-Jones algorithm.

    Args:
        frame (numpy.ndarray): The input frame.
        scaleFactor (float): The scale factor for the face detection.
        minNeighbors (int): The minimum number of neighbors for the face detection.
        color (tuple): The color for the rectangles around detected faces.

    Returns:
        tuple: The frame with detected faces and the list of detected faces.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    return frame, faces


def save_image(image, faces):
    """
    Save the image with detected faces.

    Args:
        image (numpy.ndarray): The image with detected faces.
        faces (list): The list of detected faces.

    Returns:
        bool: True if the image is saved successfully, False otherwise.
    """
    if len(faces) > 0:
        try:
            cv2.imwrite("detected_faces.png", image)
            return True
        except Exception as e:
            print(f"Error saving image: {e}")
            return False
    return False


def app():
    st.title("Face Detection using Viola-Jones Algorithm")

    # Instructions
    st.markdown("""
    ## How to Use:
    1. Adjust the parameters `scaleFactor` and `minNeighbors`.
    2. Choose the color for the rectangles around detected faces.
    3. Click 'Detect Faces' to start the detection.
    4. Save the image with detected faces if desired.
    5. Press 'q' to exit the webcam stream.
    """)

    # Color Picker
    color = st.color_picker("Pick a color for the rectangles", '#00FF00')
    color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    # Scale Factor Slider
    scaleFactor = st.slider("Scale Factor", 1.1, 2.0, 1.3)

    # Min Neighbors Slider
    minNeighbors = st.slider("Min Neighbors", 1, 10, 5)

    if st.button("Detect Faces"):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame, faces = detect_faces(frame, scaleFactor, minNeighbors, color)
            cv2.imshow("Face Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        # Save the image
        image_saved = save_image(frame, faces)
        if image_saved:
            st.success("Image saved as 'detected_faces.png'")
        else:
            st.error("Failed to save image")


if __name__ == "__main__":
    app()