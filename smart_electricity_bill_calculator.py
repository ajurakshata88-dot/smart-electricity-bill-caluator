SERVICE_CHARGE = 100.0


def get_customer_details():
    """Ask for customer information and validate the electricity units."""
    customer_name = input("Enter customer name: ").strip()
    customer_id = input("Enter customer ID: ").strip()

    while True:
        try:
            units = int(input("Enter electricity units consumed: "))
            if units < 0:
                print("Units consumed cannot be negative. Please try again.")
                continue
            return customer_name, customer_id, units
        except ValueError:
            print("Please enter a whole number of units.")


def calculate_bill(units):
    """Calculate progressive energy charges, service charge, and total."""
    first_slab_units = min(units, 100)
    second_slab_units = max(min(units - 100, 100), 0)
    third_slab_units = max(min(units - 200, 300), 0)
    highest_slab_units = max(units - 500, 0)

    energy_charge = (
        first_slab_units * 2.0
        + second_slab_units * 4.0
        + third_slab_units * 6.0
        + highest_slab_units * 8.0
    )
    final_amount = energy_charge + SERVICE_CHARGE
    return energy_charge, SERVICE_CHARGE, final_amount


def display_bill(customer_name, customer_id, units, energy_charge, service_charge, final_amount):
    """Display the customer's electricity bill."""
    print("\n" + "=" * 40)
    print("          ELECTRICITY BILL")
    print("=" * 40)
    print(f"Customer name:   {customer_name}")
    print(f"Customer ID:     {customer_id}")
    print(f"Units consumed:  {units}")
    print("-" * 40)
    print(f"Energy charge:   Rs. {energy_charge:.2f}")
    print(f"Service charge:  Rs. {service_charge:.2f}")
    print("-" * 40)
    print(f"Final amount:    Rs. {final_amount:.2f}")
    print("=" * 40)


def main():
    customer_name, customer_id, units = get_customer_details()
    energy_charge, service_charge, final_amount = calculate_bill(units)
    display_bill(
        customer_name,
        customer_id,
        units,
        energy_charge,
        service_charge,
        final_amount,
    )


if __name__ == "__main__":
    main()