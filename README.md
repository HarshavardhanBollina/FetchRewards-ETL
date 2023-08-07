# FetchRewards-ETL
**FetchRewards-ETL**


FetchRewards ETL Application
This repository contains an ETL (Extract, Transform, Load) application that reads JSON data from an AWS SQS Queue, performs data transformation and masking, and writes the processed data to a PostgreSQL database. The application is designed to be run locally using Docker containers.

Prerequisites
Before running the application, ensure that you have the following installed on your local machine:

Docker
Docker Compose
AWS CLI (with awslocal plugin)
PostgreSQL client (psql)

Getting Started
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/HarshavardhanBollina/FetchRewards-ETL.git
cd FetchRewards-ETL

Set up the Docker environment:

Run the following command to start the Docker containers for Localstack (mock AWS services) and PostgreSQL:
bash
Copy code
docker-compose up
The AWS SQS Queue and PostgreSQL database will be set up and ready to use.


Running the Application
Open a new terminal window and navigate to the root directory of the cloned repository.

Run the ETL application script:

bash
Copy code
python etl.py
The script will read messages from the login-queue SQS queue, transform and mask the data, and then insert it into the user_logins table in the PostgreSQL database.

Verification
You can verify that the application is working correctly by performing the following steps:

Check Localstack SQS Queue:

Use the AWS CLI (with the awslocal plugin) to receive messages from the SQS queue:

bash
Copy code
awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
You should see JSON messages being displayed.


Certainly! Below is a sample README file that explains how to run the application using your Git repository:

FetchRewards ETL Application
This repository contains an ETL (Extract, Transform, Load) application that reads JSON data from an AWS SQS Queue, performs data transformation and masking, and writes the processed data to a PostgreSQL database. The application is designed to be run locally using Docker containers.

Prerequisites
Before running the application, ensure that you have the following installed on your local machine:

Docker
Docker Compose
AWS CLI (with awslocal plugin)
PostgreSQL client (psql)
Getting Started
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/HarshavardhanBollina/FetchRewards-ETL.git
cd FetchRewards-ETL
Set up the Docker environment:

Run the following command to start the Docker containers for Localstack (mock AWS services) and PostgreSQL:
bash
Copy code
docker-compose up
The AWS SQS Queue and PostgreSQL database will be set up and ready to use.

Running the Application
Open a new terminal window and navigate to the root directory of the cloned repository.

Run the ETL application script:

bash
Copy code
python etl.py
The script will read messages from the login-queue SQS queue, transform and mask the data, and then insert it into the user_logins table in the PostgreSQL database.

Verification
You can verify that the application is working correctly by performing the following steps:

Check Localstack SQS Queue:

Use the AWS CLI (with the awslocal plugin) to receive messages from the SQS queue:

bash
Copy code
awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
You should see JSON messages being displayed.

Verify PostgreSQL Data:

Connect to the PostgreSQL database using the psql client:

bash
Copy code
psql -d postgres -U postgres -p 5432 -h localhost -W
Inside the psql prompt, execute the following query to view the data in the user_logins table:

sql
Copy code
SELECT * FROM user_logins;
You should see transformed and masked data in the table.

Customization
You can customize the data transformation and masking logic in the etl.py script according to your specific requirements. Additionally, you can modify the Docker Compose configuration and database credentials in the script to match your environment.

