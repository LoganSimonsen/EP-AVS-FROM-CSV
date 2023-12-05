import csv
import easypost
import json

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

def process_result(result):
    # Process the result and return a dictionary
    return {
        "id": result.id,
        "object": result.object,
        "created_at": result.created_at,
        "updated_at": result.updated_at,
        "name": result.name,
        "company": result.company,
        "street1": result.street1,
        "street2": result.street2,
        "city": result.city,
        "state": result.state,
        "zip": result.zip,
        "country": result.country,
        "phone": result.phone,
        "email": result.email,
        "mode": result.mode,
        "carrier_facility": result.carrier_facility,
        "residential": result.residential,
        "federal_tax_id": result.federal_tax_id,
        "state_tax_id": result.state_tax_id,
        "verifications": {
            "zip4": {
                "success": result.verifications.zip4.success,
                "errors": result.verifications.zip4.errors,
                "details": result.verifications.zip4.details
            },
            "delivery": {
                "success": result.verifications.delivery.success,
                "errors": result.verifications.delivery.errors,
                "details": result.verifications.delivery.details
            }
        }
    }

def main():
    # Replace 'your_file.csv' with the path to your CSV file
    input_csv_path = 'your_file.csv'
    output_csv_path = 'output_file.csv'

    with open(input_csv_path, newline='', encoding='utf-8') as csvfile, open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ["verification_result"]  # Add a new field for the verification result
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()

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

            # Process the result
            processed_result = process_result(result)

            # Write the row to the output CSV file
            row["verification_result"] = json.dumps(processed_result)
            writer.writerow(row)

if __name__ == "__main__":
    main()
