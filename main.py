import os
import random
import pandas as pd
import requests
import easyocr
import cv2
import numpy as np
import re
import csv
from tqdm import tqdm
 
# Importing custom modules for image processing and unit/entity extraction
from modules.img_processing_pipeline import *
from modules.unit_mapping import *
from modules.entity_value_extractor import *

def predictor(image_link, category_id, entity_name):
    '''
    This function processes the image link, extracts the text, 
    and predicts the entity value based on the extracted text.
    '''
    try:
        # Pass images through an image processing pipeline to extract text
        pipeline = ImageProcessingPipeline(image_link)
        
        # Download the image from the link
        pipeline.download_image()
        
        # Extract text from the image using OCR
        pipeline.extract_text()
        
        # Get the extracted text from the pipeline
        extracted_text = pipeline.get_extracted_text()
        
        # Extract and return the relevant entity value from the text
        result = get_value_for_entity(entity_name, extracted_text)
        
        # Return the first prediction if any, else return None
        return result[0] if result else None
    
    # Catch any exceptions and print error message
    except Exception as e:
        print(f"Error processing {image_link}: {e}")
        return None

def save_progress(df, output_filename):
    """
    Save intermediate progress of the DataFrame to a CSV file to avoid loss of progress.
    This function is called regularly during the processing to save progress.
    """
    df.to_csv(output_filename, index=False)
    print(f"Progress saved to {output_filename}")

if __name__ == "__main__":
    # Folder where data files are stored
    DATASET_FOLDER = './data/'
    
    # Output file to save the results
    output_filename = os.path.join(DATASET_FOLDER, 'test_out.csv')

    # Input file containing the test data
    test = pd.read_csv(os.path.join(DATASET_FOLDER, 'test.csv'))

    # Check if there's a previously saved file to resume from
    if os.path.exists(output_filename):
        # Read already processed data
        processed_test = pd.read_csv(output_filename)
        
        # Start processing from where it left off
        start_index = len(processed_test)
        
        # Skip rows that have already been processed
        test = test.iloc[start_index:]
        print(f"Resuming from row {start_index} in saved file.")
    else:
        # If no file exists, start from scratch with an empty DataFrame
        processed_test = pd.DataFrame(columns=['index', 'prediction'])
        start_index = 0

    # Wrapping iterrows() with tqdm to show the progress bar
    for i, row in tqdm(test.iterrows(), total=len(test), desc="Processing rows"):
        try:
            # Call the predictor function to get the prediction for the current row
            prediction = predictor(row['image_link'], row['group_id'], row['entity_name'])
            
            # Create a new row with the index and prediction
            new_row = pd.DataFrame({'index': [row['index']], 'prediction': [prediction]})

            # Concatenate the new prediction row with the processed DataFrame
            processed_test = pd.concat([processed_test, new_row], ignore_index=True)
            
            # Save progress after every 10 rows or the last row
            if i % 10 == 0 or i == len(test) - 1:
                save_progress(processed_test, output_filename)

        # Handle exceptions during row processing and skip problematic rows
        except Exception as e:
            print(f"Error processing row {i}: {e}")
            continue  # Skip this row and move on

    # Final save once all rows are processed
    save_progress(processed_test, output_filename)
    print("Processing complete.")
