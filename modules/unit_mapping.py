# Description: This file contains the mapping of different units to their normalized names and the mapping of entity names to the set of valid units for that entity.
  
# Define a dictionary to map different units to their normalized names
unit_mapping = {
    # Length units
    'cm': 'centimetre', 'centimetre': 'centimetre', 'centimeters': 'centimetre',
    'foot': 'foot', 'feet': 'foot', 'ft': 'foot',
    'inch': 'inch', 'inches': 'inch', 'in': 'inch',
    'metre': 'metre', 'meters': 'metre', 'm': 'metre',
    'millimetre': 'millimetre', 'millimeters': 'millimetre', 'mm': 'millimetre',
    'yard': 'yard', 'yards': 'yard', 'yd': 'yard',
    
    # Weight units
    'gram': 'gram', 'g': 'gram', 'gm': 'gram', 'grams': 'gram', 'gramme': 'gram', 'gms': 'gram',
    'kilogram': 'kilogram', 'kg': 'kilogram', 'kgs': 'kilogram', 'kilos': 'kilogram', 'kilograms': 'kilogram',
    'microgram': 'microgram', 'µg': 'microgram', 'micrograms': 'microgram',
    'milligram': 'milligram', 'mg': 'milligram', 'milligrams': 'milligram',
    'ounce': 'ounce', 'oz': 'ounce', 'ounces': 'ounce',
    'pound': 'pound', 'lb': 'pound', 'lbs': 'pound', 'pounds': 'pound',
    'ton': 'ton', 'tons': 'ton', 'tonnes': 'ton', 't': 'ton',
    
    # Voltage units
    'kilovolt': 'kilovolt', 'kv': 'kilovolt', 'kilovolts': 'kilovolt',
    'millivolt': 'millivolt', 'mv': 'millivolt', 'millivolts': 'millivolt',
    'volt': 'volt', 'v': 'volt', 'volts': 'volt',
    
    # Power units
    'watt': 'watt', 'w': 'watt', 'watts': 'watt',
    'kilowatt': 'kilowatt', 'kw': 'kilowatt', 'kilowatts': 'kilowatt',
    
    # Volume units
    'centilitre': 'centilitre', 'cl': 'centilitre', 'centilitres': 'centilitre',
    'cubic foot': 'cubic foot', 'ft³': 'cubic foot', 'cubic feet': 'cubic foot',
    'cubic inch': 'cubic inch', 'in³': 'cubic inch', 'cubic inches': 'cubic inch',
    'cup': 'cup', 'c': 'cup', 'cups': 'cup',
    'decilitre': 'decilitre', 'dl': 'decilitre', 'decilitres': 'decilitre',
    'fluid ounce': 'fluid ounce', 'fl oz': 'fluid ounce', 'fluid ounces': 'fluid ounce',
    'gallon': 'gallon', 'gal': 'gallon', 'gallons': 'gallon',
    'imperial gallon': 'imperial gallon', 'imp gal': 'imperial gallon', 'imperial gallons': 'imperial gallon',
    'litre': 'litre', 'l': 'litre', 'litres': 'litre', 'liters': 'litre',
    'microlitre': 'microlitre', 'µl': 'microlitre', 'microlitres': 'microlitre',
    'millilitre': 'millilitre', 'ml': 'millilitre', 'millilitres': 'millilitre',
    'pint': 'pint', 'pt': 'pint', 'pints': 'pint',
    'quart': 'quart', 'qt': 'quart', 'quarts': 'quart',

    # Other unit
    'kl': 'kiloleter'
}

# Mapping of entity names to the set of valid units for that entity
entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'maximum_weight_recommendation': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centilitre', 'cubic foot', 'cubic inch', 'cup', 'decilitre', 'fluid ounce', 'gallon', 'imperial gallon', 'litre', 'microlitre', 'millilitre', 'pint', 'quart'}
}
