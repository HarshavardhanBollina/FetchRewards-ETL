import json
import boto3
import psycopg2

# Define the SQS queue URL
QUEUE_URL = "http://localhost:4566/000000000000/login-queue"

# Define the PostgreSQL connection string
DB_CONN_STRING = "postgres://postgres:postgres@localhost:5432/postgres"

# Mask sensitive PII fields (Personal Identifiable Information)
def mask_pii(data):
    data["device_id"] = "****" + data["device_id"][-4:]  # Mask the device ID
    data["ip"] = "****" + data["ip"][-4:]  # Mask the IP address
    return data

# Read data from SQS queue
def read_data():
    # Use Boto3 to receive a message from the SQS queue
    response = boto3.client("sqs", endpoint_url="http://localhost:4566").receive_message(QueueUrl=QUEUE_URL)
    # Parse the JSON message body
    message = json.loads(response["Body"])
    return message

# Write data to PostgreSQL database
def write_data(data):
    """Write data to the PostgreSQL database."""
    conn = psycopg2.connect(DB_CONN_STRING)
    cur = conn.cursor()
    # Insert masked data into the 'user_logins' table
    cur.execute(
        "INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (data["user_id"], data["device_type"], data["masked_ip"], data["masked_device_id"], data["locale"], data["app_version"], data["create_date"]),
    )
    conn.commit()
    cur.close()

if __name__ == "__main__":
    # Main program flow
    data = read_data()  # Read data from SQS queue
    data = mask_pii(data)  # Mask sensitive PII fields
    write_data(data)  # Write masked data to PostgreSQL database
