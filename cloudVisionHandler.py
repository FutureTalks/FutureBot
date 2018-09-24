import boto3
import json
from base64 import b64encode

# To set up AWS Rekognition credentials and config on your local PC, follow this guide (Free Tier possible):
# https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html


# Handle image bytes input ------------------------------------------------------------------------------
def handleImage(content, chat_id, bot):	
    client = boto3.client('rekognition')

    result = client.detect_labels(    
        Image={
            'Bytes': content
        },
        MaxLabels=10
    )

    returnValue = u''
    for l in result["Labels"]:
        label = unicode(l["Name"])
        conf = unicode(l["Confidence"])
        returnValue = returnValue + label + u' : ' + conf + u'\n'

    print(returnValue)
    bot.sendMessage(chat_id, returnValue)