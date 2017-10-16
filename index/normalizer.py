# normalize words for the index and querries

# takes individual tokens/words and normalizes/prepares them for the index
def normalize(token):
  token = token.lower()
  # TODO:
  #   stemming
  #   determining and normalising abbreviations (U.S.A. -> usa; End-of-sentence. -> end-of-sentence)
