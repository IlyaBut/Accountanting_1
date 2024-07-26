from translate import Translator

languages = ['ru']


def get_translator():
    text = input('Перевести: >> ')
    for language in languages:
        translator: Translator = Translator(provider='mymemory', to_lang=language, from_lang="en")
        translation = translator.translate(text)
        print(f'{languages} : {translation}')
