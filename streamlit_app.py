import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Page Title
st.set_page_config(page_title="Waste Detection using YOLOv11")

st.title("🗑️ Waste Detection using YOLOv11")

# Load trained model
model = YOLO("runs/detect/train-10/weights/best.pt")

# Confidence slider
confidence = st.slider(
    "Confidence Threshold",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.05
)

# Upload image
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Show original image
    st.image(
        image,
        caption="Original Image",
        use_container_width=True
    )

    # Run prediction
    results = model(image, conf=confidence)

    # Plot result
    result_image = results[0].plot()

    # Show detected image
    st.image(
        result_image,
        caption="Detection Result",
        use_container_width=True
    )

    st.subheader("Detected Objects")

    # Display detections
    if len(results[0].boxes) > 0:

        for box in results[0].boxes:

            cls_id = int(box.cls.item())
            conf = float(box.conf.item())

            class_name = model.names[cls_id]

            st.write(
                f"✅ {class_name} | Confidence: {conf:.2f}"
            )

    else:
        st.warning("No objects detected.")