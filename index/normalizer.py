# normalize words for the index and querries

table = str.maketrans(dict.fromkeys(".-_'")) # a transational table for the  normalization function, used to remove the respective characters

# takes individual tokens/words and normalizes/prepares them for the index
def normalize(token):
  token = token.translate(table).lower() # remove dots, hyphens, underscores, apostrophes and put to lowercase
  # TODO:
  #   stemming
  #   maybe a better care of special characters
  return token
