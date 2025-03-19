# Import the handler
from csvhandler import S3CSVHandler

# Initialize the handler for a specific S3 bucket and file
s3_handler = S3CSVHandler(bucket_name="chatbot-const-files", file_key="awsNspreadsheet.csv")

# Define the fieldnames for the CSV structure
csv_columns = ["ID", "Name", "Education", "Experience"]

# Fetch and print existing data
existing_data = s3_handler.read_csv()
print("Existing Data:", existing_data)

s3_handler.upload_csv_to_s3(local_csv_file="awsspreadsheet.csv")

uploaded_data = s3_handler.read_csv()
print("Uploaded Data:", uploaded_data)

# import boto3

# s3 = boto3.client("s3")
# response = s3.list_buckets()

# print("Available Buckets:", [bucket["Name"] for bucket in response["Buckets"]])