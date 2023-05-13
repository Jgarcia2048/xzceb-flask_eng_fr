from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#authenticate
authenticator = IAMAuthenticator(apikey)

#setup service
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)


def english_to_french(english_text):

    if english_text is not None:
        french_text = lt.translate(text=english_text, model_id='en-fr').get_result()
        # print(frenchText['translations'][0]['translation'])
    else:
        french_text = ""

    return french_text['translations'][0]['translation']

def french_to_english(french_text):

    if french_text is not None:
        english_text = lt.translate(text=french_text, model_id='fr-en').get_result()
        # print(englishText['translations'][0]['translation'])
    else:
        english_text = ""

    return english_text['translations'][0]['translation']
