import boto3
import os
from botocore.exceptions import ClientError

# Create DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv('region_name'),
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key')
)
table_name = 'TestUsers2'

def create_table():
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'user_id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'user_id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        print("Creating table...")
        table.wait_until_exists()
        print("Table created successfully!")

    except ClientError as e:
        print("Error creating table:", e)


def insert_item():
    table = dynamodb.Table(table_name)

    response = table.put_item(
        Item={
            'user_id': '3',
            'name': 'Terry',
            'age': 29
        }
    )
    print("Item inserted:", response)


def get_item():
    table = dynamodb.Table(table_name)

    response = table.get_item(
        Key={'user_id': '1'}
    )
    print("Fetched item:", response.get('Item'))


def delete_item():
    table = dynamodb.Table(table_name)

    response = table.delete_item(
        Key={'user_id': '1'}
    )
    print("Item deleted:", response)


def delete_table():
    table = dynamodb.Table(table_name)
    table.delete()
    print("Table deleted")


if __name__ == "__main__":
    #create_table()
    insert_item()
    get_item()