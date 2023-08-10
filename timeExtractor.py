import re

def extract_time_ranges(text):
    # Defined pattern of it, 
    # \d{1,2}: Matches one or two digits (hours and minutes).
    # : Matches a colon separator between hours and minutes.
    # \d{2}: Matches two digits (minutes).
    # [APM]{2}: Matches two uppercase letters (A, P, or M) representing the AM/PM indicator.
    # -: Matches the hyphen separator between the start and end time.
    pattern = r'\d{1,2}:\d{2} [APM]{2} - \d{1,2}:\d{2} [APM]{2}'
    
    # Method to search for all occurrences of the pattern in the text.
    matches = re.findall(pattern, text)

    # Convert time ranges to a sortable format
    def convert_to_time(time_range):
        start_time, end_time = time_range.split(' - ')
        return (start_time, end_time)

    sorted_time_ranges = sorted(matches, key=convert_to_time)

    return sorted_time_ranges

# Example usage
text = "The event will take place from 2:00 PM - 4:00 PM. Please arrive on time. The second event is scheduled from 10:00 AM - 10:00 AM."
time_ranges = extract_time_ranges(text)

# Print sorted time ranges but ignore the error times.
for time_range in time_ranges:
    start_time, end_time = time_range.split(' - ')
    if start_time != end_time:
        print(time_range)