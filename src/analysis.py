from preprocess import preprocess_english, preprocess_tamil
from vocab_builder import build_vocab

# Load files
eng_text = open("data/english.txt", encoding="utf-8").read()
tam_text = open("data/tamil.txt", encoding="utf-8").read()

# Preprocess
eng_tokens = preprocess_english(eng_text)
tam_tokens = preprocess_tamil(tam_text)

# Build Vocabulary
eng_vocab = build_vocab(eng_tokens, "outputs/english_vocab.csv")
tam_vocab = build_vocab(tam_tokens, "outputs/tamil_vocab.csv")

print("English Vocabulary Size:", len(eng_vocab))
print("Tamil Vocabulary Size:", len(tam_vocab))
