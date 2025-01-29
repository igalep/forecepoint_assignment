from copy import deepcopy


#Distributes the approved rides based on the approved rides ration (approved_rides / requested_rides) per destination.
def rides_distribution(rides_approved, rides_requested, initial_rides_req):
    for destination in dict(rides_approved).keys():
        approved = rides_approved.get(destination)
        requested = rides_requested.get(destination)
        ratio = approved / requested
        initial_rides_req[destination]['approved_ratio'] = ratio

    customer_approval = deepcopy(dict(initial_rides_req))
    for destination, destination_item  in customer_approval.items():
        approved_ratio = destination_item['approved_ratio']

        if approved_ratio > 0:
            ride_with_ratio = []
            total_rides = 0
            for company_name, requested_rides in destination_item['requested_rides']:
                approved_rides = int(approved_ratio * requested_rides)
                if approved_rides < 100:
                    ride_with_ratio.append([company_name, "no rides approved"])
                else:
                    ride_with_ratio.append([company_name, approved_rides])
                    total_rides += approved_rides
            destination_item['requested_rides'] = ride_with_ratio

            if total_rides > 0:
                destination_item['total'] = total_rides
            else:
                destination_item['total'] = 0

    return customer_approval
