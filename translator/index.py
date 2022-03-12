# pip install translate <-- in terminal
from translate import Translator
translator= Translator(to_lang="IND")
translation = translator.translate("Good Morning!")
print(translation)