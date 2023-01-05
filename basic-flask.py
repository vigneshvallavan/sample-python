# Flask Server
from flask import Flask, request
import boto3
import json
'''
import sys
egg_path = '/usr/local/lib/python3.7/site-packages/VLife_Basic_Auth_New-1.0.2-py3.7.egg'
sys.path.append(egg_path)
'''
from module1 import mul

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

@app.route('/api', methods=['GET'])
def api():
    args = request.args
    key = args.get("key")
    a1,b1 = mul.perform(key,4)
    a2,b2 = mul.perform2(key,4)

    return {
        'Key': key,
        'Function Perform':
        {
            'Status': a1,
            'Result': b1
        },
        'Function Perform2':
        {
            'Status': a2,
            'Result': b2
        }
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000", debug=True)
