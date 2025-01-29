import random


def external_company_mock(ride_request):  # [str, int] --> [str, int]
    approved_rides = {}

    for destination in dict(ride_request).keys():
        # Generate a random number of approved rides between 0 and the requested number of rides
        approved_mocked = random.randint(0, ride_request.get(destination))

        # Round the approved number of rides to the nearest hundred
        rounded_approved_ride = round(approved_mocked / 10) * 10

        #handle rides subset requirements
        if rounded_approved_ride > 0:
            approved_rides[destination] = rounded_approved_ride
        else:
            continue

    return approved_rides
