import pprint
from collections import defaultdict
import src.inputOutput.csv_import_export as csv_io
import src.externalService.external_service_mock as external
import src.businessLogic.rides_distribution_strategy as bLogic



def main():
    ride_requests = defaultdict(list)

    initial_rides_requests = csv_io.read_input_file()

    # Extract the total number of rides requested for each destination
    external_service_rides_requests = {destination: destination_data['total'] for destination, destination_data in initial_rides_requests.items()}

    print('All rides :')
    pprint.pprint(initial_rides_requests)
    print('********** \n')
    print('Requested rides:')
    pprint.pprint(external_service_rides_requests)

    external_service_rides_approved = external.external_company_mock(external_service_rides_requests)

    print('Approved rides :')
    pprint.pprint(external_service_rides_approved)


    rides_final_distribution = bLogic.rides_distribution(external_service_rides_approved, external_service_rides_requests, initial_rides_requests)
    print('Approved rides customer updated:')
    pprint.pprint(rides_final_distribution)
    print('Create output CSV file:')
    csv_io.create_output_file(rides_final_distribution)


if __name__ == "__main__":
    main()