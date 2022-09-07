import boto3
from botocore.exceptions import ClientError
import random

accessKey='AKIAUML3LRJKX5MM7QFX' # ask admin to share accessKey
secretAccessKey='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' # ask admin to share secret
region='us-east-1'

def verifyIdentity(a):
    client=boto3.client('ses',aws_access_key_id=accessKey,aws_secret_access_key=secretAccessKey,region_name=region)
    response = client.verify_email_identity(EmailAddress = a)
    print(response)


def sendmessage(sub,walletaddr,name,phone,rooms,adults,date,month,year,r):
    client=boto3.client('ses',aws_access_key_id=accessKey,aws_secret_access_key=secretAccessKey,region_name=region)
    SENDER = "otp.service@makeskilled.com"
    RECIPIENT = r
    SUBJECT = sub
    BODY_HTML = """<html>
        <head></head>
        <body>
        <h1>"""+SUBJECT+"""</h1>
        <p> Your Wallet Address """+str(walletaddr)+""" .<br> <br>
        Your Name """+str(name)+""" . <br/><br/>
        Your Phone Number """+str(phone)+""" . <br/><br/>
        Your Email Id """+str(r)+""" . <br/><br/>
        Number of Rooms """+str(rooms)+""" . <br/><br/>
        Number of Adults """+str(adults)+""" . <br/><br/>
        Date of Stay """+str(date)+"/"+str(month)+"/"+str(year)+""" . <br/><br/>
        Thanks, <br>
        Make Skilled Dev Team <br>
        </p>
        </body>
        </html>
    """
    # The character encoding for the email.
    CHARSET = "UTF-8"
    try:
        #Provide the contents of the email.
        response = client.send_email(Destination={'ToAddresses': [RECIPIENT,],},
        Message={'Body': {'Html': {'Charset': CHARSET,'Data': BODY_HTML,},
        'Text': {'Charset': CHARSET,'Data': ""},},
        'Subject': {'Charset': CHARSET,'Data': SUBJECT,},},
        Source=SENDER)
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        return True