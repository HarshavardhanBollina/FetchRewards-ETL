## FetchRewards ETL Application
This repository contains an ETL (Extract, Transform, Load) application that reads JSON data from an AWS SQS Queue, performs data transformation and masking, and writes the processed data to a PostgreSQL database. The application is designed to be run locally using Docker containers.


### **Prerequisites**

Before running the application, ensure that you have the following installed on your local machine:

* Docker
* Docker Compose
* AWS CLI (with awslocal plugin)
* PostgreSQL client (psql)

### **Getting Started**

1. Clone this repository to your local machine:

       **git clone https://github.com/HarshavardhanBollina/FetchRewards-ETL.git**

       **cd FetchRewards-ETL**

3. Set up the Docker environment:
 Run the following command to start the Docker containers for Localstack (mock AWS services) and PostgreSQL:

        docker-compose up
The AWS SQS Queue and PostgreSQL database will be set up and ready to use.

### **Running the Application**
1. Open a new terminal window and navigate to the root directory of the cloned repository.
2. Run the ETL application script:
   
        python ETL_pipeline.py**
   
The script will read messages from the login-queue SQS queue, transform and mask the data, and then insert it into the user_logins table in the PostgreSQL database.

### Verification
You can verify that the application is working correctly by performing the following steps:

1. **Check Localstack SQS Queue:**
Use the AWS CLI (with the awslocal plugin) to receive messages from the SQS queue:

        awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue**
   
You should see JSON messages being displayed.

2. **Verify PostgreSQL Data:**

Connect to the PostgreSQL database using the psql client:

        psql -d postgres -U postgres -p 5432 -h localhost -W

Inside the psql prompt, execute the following query to view the data in the user_logins table:

        SELECT * FROM user_logins;
        
You should see transformed and masked data in the table.

#### **Customization**
You can customize the data transformation and masking logic in the etl.py script according to your specific requirements. Additionally, you can modify the Docker Compose configuration and database credentials in the script to match your environment.




--------------------------------------------------------------------------------------------------------------------------------------------

#### **1) How will you read messages from the queue?**

The code uses the boto3 library to interact with the SQS queue. It sets up a Boto3 client for SQS and uses the receive_message function to read messages from the queue.

#### **What type of data structures should be used?**

The code assumes that the messages from the SQS queue are in JSON format. It parses these messages into Python dictionaries for data processing. The transformed data is also represented as a dictionary.

#### **How will you mask the PII data so that duplicate values can be identified?**

The code uses a basic hash function to mask the device_id and ip fields. While this does mask the PII data, it doesn't guarantee that duplicate values can be easily identified. A better approach might involve tokenization or other techniques that allow masked data to still be analyzable.

#### **What will be your strategy for connecting and writing to Postgres?**

The code uses the psycopg2 library to connect to the PostgreSQL database. It establishes a connection using the provided credentials and connection details, and then uses SQL queries to insert transformed data into the user_logins table.

#### **Where and how will your application run?**

The code assumes that the application will run locally on a machine with Docker and the necessary prerequisites installed. It interacts with the local versions of AWS SQS (via Localstack) and PostgreSQL (via a Docker container). The application can be executed by running the script on the local machine.


--------------------------------------------------------------------------------------------------------------------------------------------
### **Questions and Answers**


**1) How would you deploy this application in production?**

  Set up production AWS SQS and PostgreSQL instances, deploy the app on a production server or containerized environment, configure security, monitoring, and logging.

**2) What other components would you want to add to make this production-ready?**

  Load balancing, data validation, security measures, scalability solutions, automated testing, and data pipeline orchestration.

**3) How can this application scale with a growing dataset?**

  Use distributed data processing frameworks, implement database sharding, and leverage cloud services for scalability.

**4) How can PII be recovered later on?**

  Use secure key management for encryption and maintain audit trails for data transformation.

**5) What are the assumptions you made?**

  Assumed JSON input format, basic PII masking, local development with Localstack, single-server setup, and simplified error handling.
