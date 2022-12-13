# Flask Server
from flask import Flask, request
import boto3
import json

app = Flask(__name__)
#api = Api(app)


s3 = boto3.client(service_name = 's3', region_name = 'us-east-1')

@app.route("/")
def index():
    Bucket_Name = 'test-cf-19'
    Key_Name = 'transaction.json'

    response = s3.get_object(Bucket = Bucket_Name, Key = Key_Name)

    content = response['Body']
    content = json.loads(content.read())
    
    print("--------------CONTENT--------------")
    print(content)
    print("-----------------------------------")    
    
    transactions = content['transactions']    

    i=1
    for record in transactions:
        print("------------RECORD -",+i ,'------------')
        print("Transaction Type   : " + record['transactionType'])
        print("Transaction Amount : " + str(record['amount']))
        i+=1
    print("-----------------------------------")
    return transactions
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000", debug=True)
