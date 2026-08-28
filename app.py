from flask import Flask, render_template, request, send_from_directory
import os
import cv2

from processing import (
    read_img,
    crop_img,
    resize_img,
    grayscale_img,
    blur_img,
    edge_img
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    # Get user information
    name = request.form["name"]
    email = request.form["email"]

    # Get crop and resize values
    crop_height = int(request.form["crop_height"])
    crop_width = int(request.form["crop_width"])

    resize_height = int(request.form["resize_height"])
    resize_width = int(request.form["resize_width"])

    # Get uploaded image
    file = request.files["image"]

    # Save uploaded image
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # Read image using OpenCV
    img = read_img(input_path)

    # Apply processing
    cropped = crop_img(img, crop_height, crop_width)
    resized = resize_img(img, resize_height, resize_width)
    grayscale = grayscale_img(img)
    blurred = blur_img(img)
    edges = edge_img(img)

    # Save processed images
    cv2.imwrite(
        os.path.join(PROCESSED_FOLDER, "cropped.png"),
        cropped
    )

    cv2.imwrite(
        os.path.join(PROCESSED_FOLDER, "resized.png"),
        resized
    )

    cv2.imwrite(
        os.path.join(PROCESSED_FOLDER, "grayscale.png"),
        grayscale
    )

    cv2.imwrite(
        os.path.join(PROCESSED_FOLDER, "blurred.png"),
        blurred
    )

    cv2.imwrite(
        os.path.join(PROCESSED_FOLDER, "edges.png"),
        edges
    )

    return render_template(
        "result.html",
        name=name,
        email=email
    )


@app.route("/processed/<filename>")
def processed(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)