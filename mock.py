# Smart Railway Ticket Booking and Passenger Management System

# Fare chart
destinations = ["Mumbai", "Pune", "Nashik", "Nagpur"]
fares = [250, 150, 200, 450]

# Stored booking information (parallel lists)
names = []
ages = []
dests = []
tickets_list = []
fare_per_ticket_list = []
totals = []

while True:
    print("\n===== SMART RAILWAY TICKET BOOKING =====")
    print("1. Book Tickets")
    print("2. Display Fare Chart")
    print("3. Generate Booking Summary")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("How many passengers want to book tickets? "))

        for i in range(n):
            print("\n--- Passenger", i + 1, "---")
            name = input("Passenger name: ")
            age = int(input("Age: "))
            dest = input("Destination: ").strip().title()
            num_tickets = int(input("Number of tickets required: "))

            # Age validation
            if age <= 0:
                print("Invalid age! Booking skipped for this passenger.")
            else:
                # Destination validation
                if dest not in destinations:
                    print("Invalid destination! Booking skipped for this passenger.")
                else:
                    # Ticket count validation
                    if num_tickets <= 0:
                        print("Invalid number of tickets! Booking skipped.")
                    else:
                        # Base fare for the destination
                        base_fare = 0
                        for j in range(len(destinations)):
                            if destinations[j] == dest:
                                base_fare = fares[j]

                        # Age-based discount
                        if age <= 4:
                            fare = 0
                            print("Child below 5 years travels free.")
                        elif age <= 17:
                            fare = base_fare * 0.5
                        elif age <= 59:
                            fare = base_fare
                        else:
                            fare = base_fare * 0.7

                        total = fare * num_tickets

                        # Store the successful booking
                        names.append(name)
                        ages.append(age)
                        dests.append(dest)
                        tickets_list.append(num_tickets)
                        fare_per_ticket_list.append(fare)
                        totals.append(total)

                        # Display individual passenger details
                        print("\nBooking Successful!")
                        print("Passenger Name   :", name)
                        print("Age              :", age)
                        print("Destination      :", dest)
                        print("Number of Tickets:", num_tickets)
                        print("Fare per Ticket  : Rs.", fare)
                        print("Total Fare       : Rs.", total)

    elif choice == 2:
        print("\n----- FARE CHART -----")
        print("Destination\tTicket Fare")
        for i in range(len(destinations)):
            print(destinations[i], "\t\tRs.", fares[i])

    elif choice == 3:
        if len(names) == 0:
            print("\nNo successful bookings have been made yet.")
        else:
            total_passengers = len(names)
            total_tickets = 0
            total_revenue = 0
            for i in range(total_passengers):
                total_tickets = total_tickets + tickets_list[i]
                total_revenue = total_revenue + totals[i]

            print("\n===== BOOKING SUMMARY =====")
            print("Total Registered Passengers:", total_passengers)
            print("Total Tickets Booked       :", total_tickets)
            print("Total Revenue Collected    : Rs.", total_revenue)

            print("\nPassengers per Destination:")
            for d in destinations:
                count = 0
                for x in dests:
                    if x == d:
                        count = count + 1
                print(d, ":", count)

            # Nested loop: destination-wise passenger report
            print("\n===== DESTINATION-WISE PASSENGER REPORT =====")
            for d in destinations:
                passenger_names = ""
                found = False
                for i in range(len(names)):
                    if dests[i] == d:
                        if found:
                            passenger_names = passenger_names + ", " + names[i]
                        else:
                            passenger_names = names[i]
                            found = True
                if found:
                    print(d, ":", passenger_names)
                else:
                    print(d, ": No passengers booked")

    elif choice == 4:
        print("\nThank you for using the Smart Railway Ticket Booking System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
