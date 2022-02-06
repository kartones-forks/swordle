import string
from pathlib import Path

# freely available dictionary that ships with Linux in /usr/share/dict/...
# text file per language, with a single word for each line
# might need to install additional languages

# language_dictionary = "/usr/share/dict/american-english"
# language_dictionary = "/usr/share/dict/british-english"
# allowable_characters = set(string.ascii_letters)

# for spanish
language_dictionary = "/usr/share/dict/spanish"
allowable_characters = set(string.ascii_letters).union(set(["ñ", "á", "é", "í", "ó", "ú"]))


dict_words = list({
  word.lower()
  for word in Path(language_dictionary).read_text('utf-8').splitlines()
  if len(word) == 5 and set(word) < allowable_characters
})

dict_words.sort()

# TODO: write to file instead

print(dict_words)
