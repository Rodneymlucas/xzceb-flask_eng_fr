import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
lt.set_service_url(url)

def english_to_french(english_text):
    """ This converts English into French. """
    #write the code here
    french_text = 'French word'
    return french_text

def french_to_english(french_text):
    """ This converts French into English. """
    #write the code here
    english_text = 'English word'
    return english_text

