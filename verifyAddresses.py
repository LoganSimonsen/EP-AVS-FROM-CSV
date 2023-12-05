import csv
import easypost

# Set your EasyPost API key
easypost.api_key = 'YOUR_EASYPOST_API_KEY'

def verify_address(name, street1, street2, city, state, zip_code, country):
    address = easypost.Address.create(
        name=name,
        street1=street1,
        street2=street2,
        city=city,
        state=state,
        zip=zip_code,
        country=country
    )

    return address

def main():
    # Replace 'your_file.csv' with the path to your CSV file
    csv_file_path = 'your_file.csv'

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            street1 = row['street1']
            street2 = row['street2']
            city = row['city']
            state = row['state']
            zip_code = row['zip']
            country = row['country']

            # Verify address
            result = verify_address(name, street1, street2, city, state, zip_code, country)

            # Process the result (you can customize this part based on your needs)
            if result.verifications.delivery.success:
                print(f"Address for {name} is valid!")
            else:
                print(f"Address for {name} is invalid. Details: {result.verifications.delivery.errors}")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
