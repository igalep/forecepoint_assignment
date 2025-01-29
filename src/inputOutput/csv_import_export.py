import csv
from collections import defaultdict

FIELD_NAME = []

#Reads the initial ride requests from an input CSV file.
def read_input_file():
    company_destination_set = set()
    csv_data = defaultdict(lambda: {"total": 0, "requested_rides": [], "approved_ratio": 0})

    input_file = 'resources/requested_rides.csv'

    with open(input_file, mode='r') as file:  # read from csv to
        reader = csv.DictReader(file)

        global FIELD_NAME
        FIELD_NAME = reader.fieldnames

        for row in reader:
            number_of_rides_requested = int(row['number_of_rides_requested'])
            company_destination = (row['company_name'], row['destination'])

            if company_destination not in company_destination_set and number_of_rides_requested % 100 == 0:
                company_destination_set.add(company_destination)
                csv_data[row['destination']]['requested_rides'].append([row['company_name'], number_of_rides_requested])
                csv_data[row['destination']]['total'] += int(row['number_of_rides_requested'])
                csv_data[row['destination']]['approved_ratio'] = 0
            else:
                continue

    return dict(csv_data)

#Creates an output CSV file with the final distribution of approved rides.
def create_output_file(rides_final_distribution):
    output_file = 'resources/approved_rides.csv'

    with open(output_file, mode="w", newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(FIELD_NAME)

        for destination , inner_details in rides_final_distribution.items():
            for company_name, number_of_rides_approved in inner_details['requested_rides']:
                writer.writerow([company_name, destination, number_of_rides_approved])