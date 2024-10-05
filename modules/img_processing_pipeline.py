import requests  # For handling HTTP requests to download the image
import easyocr  # EasyOCR is used for text extraction from images (Optical Character Recognition)
import cv2  # OpenCV for image processing
import numpy as np  # NumPy for handling image data arrays

class ImageProcessingPipeline:
    def __init__(self, image_url):
        # Initialize the class with the URL of the image
        self.image_url = image_url  # URL of the image to process
        self.image = None  # Placeholder for storing the image once it's downloaded
        self.extracted_text = None  # Placeholder for the text extracted from the image

    def download_image(self):
        """Download the image from the provided URL and store it as an OpenCV image."""
        # Send an HTTP GET request to download the image
        response = requests.get(self.image_url)
        if response.status_code == 200:
            # Convert the downloaded image content (bytes) into a NumPy array
            image_np = np.frombuffer(response.content, np.uint8)
            # Decode the NumPy array into an image using OpenCV (in color mode)
            self.image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        else:
            # Raise an exception if the image could not be downloaded
            raise Exception(f"Failed to download image from {self.image_url}, Status Code: {response.status_code}")

    def extract_text(self):
        """Extract text from the downloaded image using EasyOCR."""
        if self.image is None:
            # Raise an error if the image hasn't been downloaded yet
            raise FileNotFoundError("Image is not downloaded.")
        
        # Initialize the EasyOCR reader for English (other languages can be added)
        reader = easyocr.Reader(['en'])
        
        # Convert the image from BGR (OpenCV's default format) to RGB for EasyOCR
        image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        
        # Use EasyOCR to detect and extract text from the image
        result = reader.readtext(image_rgb)
        
        # Combine all extracted text into a single string, ignoring the bounding boxes and confidence scores
        self.extracted_text = ' '.join([text[1] for text in result])

    def get_extracted_text(self):
        """Return the text that was extracted from the image."""
        if self.extracted_text is None:
            # Raise an error if text extraction has not been performed yet
            raise RuntimeError("Text extraction not performed.")
        return self.extracted_text

# Example usage
# image_url = "https://m.media-amazon.com/images/I/61cMeogK8gL.jpg"
# pipeline = ImageProcessingPipeline(image_url)

# Run the pipeline
# pipeline.download_image()
# pipeline.extract_text()
# extracted_text = pipeline.get_extracted_text()

# print("Extracted Text:\n", extracted_text)
