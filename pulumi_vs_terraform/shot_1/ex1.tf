# Configure the AWS provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS provider
provider "aws" {
  region = "us-east-1" # Or your desired region
}

# Create an S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-name" # Replace with your unique bucket name
  tags = {
    Name = "My S3 Bucket"
  }
}