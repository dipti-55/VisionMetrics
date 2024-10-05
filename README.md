# Amazon ML Challenge 2024 : Entity Value Extraction from Product Images

# 📋 Overview

This project aims to extract entity values (such as dimensions, weight, voltage, etc.) from product images using Optical Character Recognition (OCR) and a custom image processing pipeline. The solution employs EasyOCR for text extraction and a unit mapping system to normalize the extracted values.

# 📊 Dataset
   - A CSV file (`test.csv`) contains links to the images, along with associated metadata such as `index`,`group_id` and `entity_name`.


# ⚙️ Project Workflow
1. ## **Image Acquisition:**
   - Utilized an HTTP request to download product images from provided URLs. The images were decoded and converted into a format suitable for further processing using OpenCV.

2. ## **Image Preprocessing:**
   - Performed necessary preprocessing tasks, including converting the image from BGR (OpenCV’s default color format) to RGB for compatibility with the OCR tool. This step ensured that the image was optimized for accurate text extraction.

3. ## **Text Extraction (OCR):**
   - Leveraged EasyOCR to extract textual information from the processed images.

4. ## **Regex-Based Unit Extraction:**
   - Implemented a robust regular expression (regex) pattern to identify numeric values and their associated units (e.g., "10 cm", "5 volts") from the extracted text. This step focused on identifying both common and edge-case formats for various measurements.

5. ## **Entity-Unit Mapping:**
   - Designed a custom mapping system to normalize the extracted units (e.g., converting "cm" to "centimetre"). Entities such as width, height, and voltage were mapped to valid unit sets to ensure consistency and accuracy in the extracted data.

6. ## **Entity-Specific Value Retrieval:**
   - For each target entity (e.g., width, height, voltage), filtered the extracted text to identify and return the most relevant measurement, matching the expected units defined in the entity-unit mapping.

7. ## **Output:**
   - Presented the extracted entity values in CSV format. The system was designed to handle variations in unit representation and ensure accuracy in the final output.

# 🗂️ File Structure

```
.
├── modules/
│   ├── img_processing_pipeline.py
│   ├── unit_mapping.py
│   └── entity_value_extractor.py
├── data/
│   ├── test.csv
│   └── test_out.csv
├── main.py
├── requirements.txt
├── PROBLEM_STATEMENT.md
└── README.md
```

### 1. `main.py`
- **Description**: Entry point of the project that runs the complete pipeline.
- **Functionality**:
  - Reads the test dataset (images and entity names).
  - For each image, downloads it and processes it through the image pipeline.
  - Uses OCR to extract text and attempts to map the extracted text to the corresponding entity and unit.
  - Saves predictions for each image and entity to a CSV file (`test_out.csv`).

### 2. `img_processing_pipeline.py`
- **Description**: Handles image downloading, preprocessing and text extraction using EasyOCR and OpenCV.
- **Functions**:
  - **`download_image(self)`**: 
    - Downloads the image from the URL using `requests`.
    - Converts it into an OpenCV-readable format.
    - **Output**: The image is stored in `self.image` in OpenCV format.
  
  - **`extract_text(self)`**:
    - Extracts text from the downloaded image using EasyOCR after converting it to RGB format.
    - **Output**: The extracted text is stored in `self.extracted_text`.
  
  - **`get_extracted_text(self)`**:
    - Returns the text extracted from the image.
    - **Output**: A string containing all the text extracted by EasyOCR.

### 3. `entity_value_extractor.py`
- **Description**: Handles the task of extracting numeric values and units from the text.
- **Functions**:
  - **`extract_values_with_units()`**:
    - Uses a regex pattern to search for numeric values paired with measurement units (e.g., "10 cm", "5 volts") in the extracted text.
    - Maps the extracted unit to its normalized form using the `unit_mapping` dictionary.
    - **Output**: A list of strings like `["10 centimetre", "5 volt"]`.
  
  - **`get_value_for_entity()`**:
    - Validates if the extracted unit matches the expected units for a specific entity (e.g., width, height).
    - Compares extracted units with valid ones from `entity_unit_map`.
    - **Output**: A list containing the first matching value-unit pair (e.g., "15 centimetre") or an empty list if no match is found.

### 4. `unit_mapping.py`
- **Description**: Contains mappings for units and their canonical forms.
- **Content**:
  - **Unit Normalization**: 
    - `unit_mapping`: Maps various representations of units (e.g., "cm", "centimetre") to a normalized form.
  - **Entity-Unit Mapping**:
    - `entity_unit_map`: Defines valid units for each entity type (e.g., "width" can be in centimeters, inches, etc.).

# 🏆 Result
- Once all images are processed, the final predictions are saved to `test_out.csv` in the `./data/` directory. If there's an interruption, the script will resume from the last processed row.
- The intermediate progress of the DataFrame is saved to a CSV file (`test_out.csv`) to avoid loss of progress.


# 💻 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![EasyOCR](https://img.shields.io/badge/EasyOCR-444444?style=for-the-badge&logoColor=white)
![Regex](https://img.shields.io/badge/Regex-FFA500?style=for-the-badge&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-3776AB?style=for-the-badge&logoColor=white)


