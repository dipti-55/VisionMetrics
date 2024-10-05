import re

from modules.unit_mapping import *

# Function to extract numeric values followed by units from the given text
def extract_values_with_units(text):
    # Regex pattern to match numbers followed by a unit (e.g., "10 cm", "5 volts")
    pattern = r'(\d+\.?\d*)\s*(centimetre|centimeters?|cm|foot|feet|ft|inch|inches?|in|millivolt|mv|millilitre|ml|milligram|mg|millimeter|millimeters?|mm|metre|meters?|m|yard|yards?|yd|gallon|gal|gallons?|gram?|g|grams?|gms?|gramme|kiloleter?|kl|kilowatt|kw|kilogram|kg|kgs?|kilos?|kilograms?|kilo|microgram|µg|ounce|ounces?|oz|pound|pounds?|lbs?|lb|ton|tons?|tonnes?|t|kilovolt|kv|volt|volts?|v|watt|watts?|w|centilitre|cl|centilitres?|cubic\s*foot|ft³|cubic\s*feet?|cubic\s*inch|in³|cup|cups?|c|decilitre|dl|decilitres?|fluid\s*ounce|fl\s*oz|fluid\s*ounces?|imperial\s*gallon|imp\s*gal|litre|litres?|l|liters?|microlitre|µl|pint|pints?|pt|quart|quarts?|qt)'

    # Find all matches (value + unit) in the text
    matches = re.findall(pattern, text, re.IGNORECASE)
    extracted_info = []
    
    # Loop through matches to map units to their normalized form
    for value, unit in matches:
        full_unit = unit_mapping.get(unit.lower(), unit)  # Normalize the unit
        extracted_info.append(f"{value} {full_unit}")  # Append value and normalized unit to the result
    return extracted_info

# Function to extract the relevant value for a specific entity from the text
def get_value_for_entity(entity_name, text):
    # Check if the entity name is valid (exists in entity_unit_map)
    if entity_name not in entity_unit_map:
        return []  # If entity not found, return an empty list

    # Extract all value-unit pairs from the text
    extracted_values = extract_values_with_units(text)
    
    # Get the valid units for the specified entity
    valid_units = entity_unit_map[entity_name]
    
    # Loop through the extracted values and check if the unit is valid for the entity
    for item in extracted_values:
        value, unit = item.split(maxsplit=1)  # Split value and unit
        if unit.lower() in valid_units:
            return [item]  # Return the first valid value-unit pair for the entity
    
    return []  # If no valid match found, return an empty list