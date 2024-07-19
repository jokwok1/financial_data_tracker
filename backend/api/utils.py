# Processing CSV Files and generating charts
from collections import defaultdict
from decimal import ROUND_DOWN, Decimal
import json
import pandas as pd
from .models import Entry
import os
from django.conf import settings
from .serializers import EntrySerializer
from datetime import datetime

def save_csv_file(file, user):
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    os.makedirs(upload_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename, extension = os.path.splitext(file.name)
    new_filename = f"{filename}_{timestamp}_{user.username}{extension}"
    file_path = os.path.join(upload_dir, new_filename)

    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    print(file_path)

    return file_path


def process_csv_file(file_path, user):
    try:
        df = pd.read_csv(file_path)
    except (pd.errors.ParserError, pd.errors.EmptyDataError, pd.errors.UnicodeDecodeError, pd.errors) as e:
        # Handle file reading errors
        raise Exception(f'Error reading CSV file: {str(e)}')
    
    # Formatting Df
    df['Date'] = df['Date'].astype(str)
    df['Amount'] = df['Amount'].fillna(0)
    df['Category'] = df['Category'].str.lower()  
    df['Category'] = df['Category'].str.title()  

    data_entries = []
    for index, row in df.iterrows():
        date_str = row['Date'].strip() 
        # Check for NaN explicitly and skip 
        if date_str.lower() == 'nan':  
            print(f"Skipping row {index}: NaN value found in 'Date' column")
            continue
        # Formatting of amount value
        amount_decimal = Decimal(row['Amount']).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        
        entry_data = {
        'category': row['Category'],
        'amount': amount_decimal,  # Convert to Decimal
        'date': datetime.strptime(row['Date'], '%d/%m/%Y').date(),  # Convert to DateField format
        'author': user  # Assign the currently authenticated user
        }   

        # Create a serializer instance to validate and save the Entry object
        entry_serializer = EntrySerializer(data=entry_data)
        if entry_serializer.is_valid():
            try:
                entry_serializer.save(author=user)
                data_entries.append(entry_serializer.data)
            except Exception as e:
                print(f"Error during save: {e}")
        else:
            errors = entry_serializer.errors
            raise Exception(f'Validation Error: {entry_serializer.errors}')
    print('data entries: ', data_entries)

    return data_entries

def generate_chart_json(data_entries):
    
    # Aggregate amounts by category
    category_totals = defaultdict(float)
    for entry in data_entries:
        category_totals[entry.category] += float(entry.amount)

    # Round the total amounts to 2 decimal places
    for category, total in category_totals.items():
        category_totals[category] = round(total, 2)

    # Create data for Chart.js
    chart_data = {
        "labels": list(category_totals.keys()),
        "datasets": [{
            "label": "Total Amount per Category",
            "data": list(category_totals.values()),
            "backgroundColor": "rgba(75, 192, 192, 0.2)",
            "borderColor": "rgba(75, 192, 192, 1)",
            "borderWidth": 1,
        }]
    }

    chart_json = json.dumps(chart_data)
    return chart_json