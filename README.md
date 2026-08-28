OpenCV Image Processing Web App

A web-based image processing application built using Python, Flask, OpenCV, HTML, and CSS.

Features
Upload an image
Custom image cropping
Custom image resizing
Grayscale conversion
Gaussian blur
Canny edge detection
Web-based interface for image processing
Technologies Used
Python
OpenCV
Flask
HTML
CSS
Project Structure
OPEN CV P1/
│
├── app.py
├── processing.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── uploads/
└── processed/
How to Run
1. Clone the repository
git clone YOUR_REPOSITORY_LINK
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

Windows:

.venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the application
python app.py
6. Open in your browser
http://127.0.0.1:5000
OpenCV Operations

The application currently supports:

Cropping
Resizing
Grayscale conversion
Gaussian Blur
Canny Edge Detection
Future Improvements
Download processed images
Before/after image comparison
Better error handling
Multiple image-processing options
Improved UI/UX
