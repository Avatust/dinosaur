# the tokenize function will extract tokens
import re #Regular Expressions

regex = re.compile("[\w\d._-']+") # compiled regular expression to extract tokens

# parses the text and returns an iterator of tokens in the given text
def tokenize(text):
  return regex.finditer(text) 
