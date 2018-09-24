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

    
# Handle text input ------------------------------------------------------------------------------
def handleText(command, msg, chat_id, bot):
    commands = command.split()
    # Commands with '/'  ----------------------
    if commands[0]=='/tts':
        print('Text to speech')
        client = boto3.client('polly')

        command = command.replace(commands[0], '')

        result = client.synthesize_speech( 
            OutputFormat = "mp3",
            Text = command,
            VoiceId = "Joanna"
        )

        print(result['AudioStream'])

        bot.sendAudio(chat_id, result['AudioStream'])