# the tokenize function will extract tokens
import re

regex = re.compile("[\w._-]+")

def tokenize(text):
  return regex.finditer(text)
