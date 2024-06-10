import pandas as pd
from icalendar import Calendar, Event
from pytz import timezone
from datetime import datetime

def convert_csv_to_ics(csv_file, ics_file, tz='US/Eastern'):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Create a calendar
    cal = Calendar()
    
    # Time zone
    eastern = timezone(tz)
    
    for index, row in df.iterrows():
        event = Event()
        
        # Fill in event details
        event.add('summary', row['Subject'])
        event.add('description', row['Description'])
        event.add('location', row['Location'])
        
        # Parse dates and times
        start_dt_str = f"{row['Start Date']} {row['Start Time']}"
        end_dt_str = f"{row['End Date']} {row['End Time']}"
        
        start = eastern.localize(datetime.strptime(start_dt_str, '%m/%d/%Y %I:%M:%S %p'))
        end = eastern.localize(datetime.strptime(end_dt_str, '%m/%d/%Y %I:%M:%S %p'))
        
        event.add('dtstart', start)
        event.add('dtend', end)
        
        if str(row['All Day']).strip().lower() in ['true', 'yes', '1']:
            event.add('dtstart', eastern.localize(datetime.strptime(row['Start Date'], '%m/%d/%Y')).date())
            event.add('dtend', eastern.localize(datetime.strptime(row['End Date'], '%m/%d/%Y')).date())
            event.add('X-MICROSOFT-CDO-ALLDAYEVENT', 'TRUE')
        
        cal.add_component(event)
    
    # Write to .ics file
    with open(ics_file, 'wb') as f:
        f.write(cal.to_ical())

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert CSV to ICS')
    parser.add_argument('csv_file', help='Path to the input CSV file')
    parser.add_argument('ics_file', help='Path to the output ICS file')
    parser.add_argument('--timezone', default='US/Eastern', help='Time zone for the events (default: US/Eastern)')

    args = parser.parse_args()
    convert_csv_to_ics(args.csv_file, args.ics_file, args.timezone)

