# Flask Server
from flask import Flask, request
import boto3
import json
#################
import sys
egg_path = '/home/ec2-user/.local/lib/python3.7/site-packages/VLife_Basic_Auth_New-1.0.1-py3.7.egg'
sys.path.append(egg_path)

from module1 import mul
#################
app = Flask(__name__)

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

    i = 1
    for record in transactions:
        print("------------RECORD -",+i ,'------------')
        print("Transaction Type   : " + record['transactionType'])
        print("Transaction Amount : " + str(record['amount']))
        i+=1
    print("-----------------------------------")
    
    return transactions

@app.route('/api')
def api():
    a = mul.perform(4)
    b = mul.perform2(4)

    return {
        'Package Name': 'VLife-Basic-Auth-New',
        'Authentication' : 'Verified',
        'Function - Perform' : a,
        'Function - Perform 2' : b
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000", debug=True)
