from flask import Flask
import os
import ibm_boto3
from ibm_botocore.client import Config, ClientError

app = Flask(__name__)

def create_text_file(bucket_name, item_name, file_text):
    print("Creating new item: {0}".format(item_name))
    try:
        cos_client.put_object(
            Bucket=bucket_name,
            Key=item_name,
            Body=file_text
        )
        print("Item: {0} created!".format(item_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to create text file: {0}".format(e))

@app.route("/")
def hello():
    name = os.getenv("TEST", "World")
    return f"Hello from Code Engine, {name}!\n"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
