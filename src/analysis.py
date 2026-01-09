import os
from preprocess import preprocess_english, preprocess_tamil
from vocab_builder import build_vocab
from stats import compute_statistics

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths
eng_path = os.path.join(BASE_DIR, "data", "english.txt")
tam_path = os.path.join(BASE_DIR, "data", "tamil.txt")

# Read text
with open(eng_path, encoding="utf-8") as f:
    eng_text = f.read()

with open(tam_path, encoding="utf-8") as f:
    tam_text = f.read()

# Preprocess
eng_tokens = preprocess_english(eng_text)
tam_tokens = preprocess_tamil(tam_text)

# Vocabulary (Bag-of-Words)
eng_vocab = build_vocab(eng_tokens, os.path.join(BASE_DIR, "outputs", "english_vocab.csv"))
tam_vocab = build_vocab(tam_tokens, os.path.join(BASE_DIR, "outputs", "tamil_vocab.csv"))

# Statistics
eng_stats = compute_statistics(eng_tokens, "English")
tam_stats = compute_statistics(tam_tokens, "Tamil")

# Comparative summary
print("\n=== VOCABULARY SIZE ===")
print(f"English: {eng_stats['unique_words']} unique words")
print(f"Tamil:   {tam_stats['unique_words']} unique words")
print(f"Difference: {tam_stats['unique_words'] - eng_stats['unique_words']} words")

print("\n=== WORD LENGTH ===")
print(f"English: {eng_stats['avg_word_length']:.2f} characters")
print(f"Tamil:   {tam_stats['avg_word_length']:.2f} characters")

print("\n=== LEXICAL DIVERSITY (Type-Token Ratio) ===")
print(f"English TTR: {eng_stats['ttr']:.4f}")
print(f"Tamil TTR:   {tam_stats['ttr']:.4f}")

# Save results to file (with proper UTF-8 encoding for Tamil)
output_path = os.path.join(BASE_DIR, "outputs", "stats_output.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("KEY RESULTS FROM TEXT ANALYSIS\n\n")
    f.write(f"English Vocabulary: {eng_stats['unique_words']} unique words\n")
    f.write(f"Tamil Vocabulary: {tam_stats['unique_words']} unique words\n\n")

    f.write(f"English Avg Word Length: {eng_stats['avg_word_length']:.2f}\n")
    f.write(f"Tamil Avg Word Length: {tam_stats['avg_word_length']:.2f}\n\n")

    f.write(f"English TTR: {eng_stats['ttr']:.4f}\n")
    f.write(f"Tamil TTR: {tam_stats['ttr']:.4f}\n\n")
    
    f.write("=== TOP 5 ENGLISH WORDS ===\n")
    for word, count in eng_stats['top_words']:
        f.write(f"  {word}: {count}\n")
    
    f.write("\n=== TOP 5 TAMIL WORDS ===\n")
    for word, count in tam_stats['top_words']:
        f.write(f"  {word}: {count}\n")

# Save Tamil top words separately for easy viewing
tamil_top_path = os.path.join(BASE_DIR, "outputs", "tamil_top_words.txt")
with open(tamil_top_path, "w", encoding="utf-8") as f:
    f.write("TOP TAMIL WORDS (by frequency)\n")
    f.write("=" * 40 + "\n\n")
    for i, (word, count) in enumerate(tam_stats['top_words'], 1):
        f.write(f"{i}. {word} : {count}\n")

print(f"\n[Results saved to outputs/stats_output.txt]")
print(f"[Tamil words saved to outputs/tamil_top_words.txt]")
