import boto3


client = boto3.client('ses',
    aws_access_key_id='<yourAWSAccessKeyId>',
    aws_secret_access_key='<yourAWSSecretAccessKey>',
    region_name='eu-west-2'
)

def sendMail(fromMail,toMail, subject):
    try:      
        with open('./Design/index.html', 'r') as file:
            data = file.read().replace('\n', '')  
        
        data = data.replace('{$Content1}','changedVal1') 
        data = data.replace('{$Content2}','changedVal2')
        data = data.replace('{$Content3}','changedVal3')
        
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    toMail
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': data,
                    } 
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=fromMail,
        )

    except BaseException as error:
          print('An exception occurred: '+format(error))
          
          
if __name__ == '__main__':
    sendMail('admin@<yourdomain>.com','<ToMail>@gmail.com','Trial Subject')