import boto3
import csv
import io
import os
from dotenv import load_dotenv
from config_loader import *

class S3CSVHandler:
    def __init__(self, bucket_name, file_key, aws_access_key=None, aws_secret_key=None):
        """
        Initializes the S3 CSV handler.
        :param bucket_name: Name of the S3 bucket
        :param file_key: Path to the CSV file inside the bucket
        :param aws_access_key: AWS Access Key (Optional if using IAM roles)
        :param aws_secret_key: AWS Secret Key (Optional if using IAM roles)
        """
        
        load_env()
        load_dotenv()
        self.bucket_name = bucket_name
        self.file_key = file_key

        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key or os.getenv("CHAT_ACCESS_KEY_ID", ""),
            aws_secret_access_key=aws_secret_key or os.getenv("CHAT_SECRET_ACCESS_KEY", ""),
        )

    def read_csv(self):
        """
        Reads the CSV file from S3 and returns data as a list of dictionaries.
        If the file does not exist, returns an empty list.
        """
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=self.file_key)
            csv_content = response["Body"].read().decode("utf-8")
            reader = csv.DictReader(io.StringIO(csv_content))

            return [row for row in reader]

        except self.s3_client.exceptions.NoSuchKey:
            print(f"File '{self.file_key}' not found in bucket '{self.bucket_name}'. Returning empty list.")
            return []

    def write_csv(self, new_data, fieldnames):
        """
        Writes new data to the S3 CSV file. If the file exists, it appends new data;
        otherwise, it creates a new file.
        :param new_data: Dictionary containing the new row data
        :param fieldnames: List of column names for the CSV
        """
        # Fetch existing data
        existing_data = self.read_csv()

        # Merge new data
        all_data = existing_data + [new_data]

        # Create an in-memory CSV file
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)

        # Upload the updated CSV back to S3
        self.s3_client.put_object(Bucket=self.bucket_name, Key=self.file_key, Body=output.getvalue(), ContentType="text/csv")

        print(f"File '{self.file_key}' updated successfully in bucket '{self.bucket_name}'.")
        
    def upload_csv_to_s3(self, local_csv_file, s3_target_path=None):
        """
        Uploads a local CSV file to the specified S3 bucket.
        :param local_csv_file: Path to the local CSV file.
        :param s3_target_path: Target file path in S3 (optional, defaults to self.file_key).
        """
        s3_target_path = s3_target_path or self.file_key

        try:
            self.s3_client.upload_file(local_csv_file, self.bucket_name, s3_target_path)
            print(f"✅ CSV file '{local_csv_file}' uploaded successfully to 's3://{self.bucket_name}/{s3_target_path}'")

        except Exception as e:
            print(f"❌ Error uploading file: {str(e)}")