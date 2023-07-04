import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('counttable')

def lambda_handler(event, context):
    response = table.get_item(Key={
        'id': '0',
        'item' : 'count'})

    views = response['Item']['views']
    views = views + 1
    print(views)
    response= table.put_item(Item={
        'id':'0',
        'item' : 'count',
        'views':views})

    return(views)
