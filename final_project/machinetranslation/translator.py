from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Traduce el texto de inglés a francés utilizando MyMemoryTranslator.
    
    :param english_text: El texto en inglés a traducir.
    :return: El texto traducido al francés.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)

    return french_text

def french_to_english(french_text):
    """
    Traduce el texto de francés a inglés utilizando MyMemoryTranslator.
    
    :param french_text: El texto en francés a traducir.
    :return: El texto traducido al inglés.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    
    return english_text 

