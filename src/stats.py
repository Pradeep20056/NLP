from collections import Counter
import sys
import io

def compute_statistics(tokens, language_name):
    total_words = len(tokens)
    unique_words = len(set(tokens))
    vocab_coverage = (unique_words / total_words) * 100 if total_words > 0 else 0

    avg_word_length = sum(len(w) for w in tokens) / total_words if total_words > 0 else 0

    counter = Counter(tokens)
    top_words = counter.most_common(5)

    ttr = unique_words / total_words if total_words > 0 else 0

    # Console-safe output (no Unicode words for Tamil)
    print(f"\nPROCESSING {language_name.upper()} TEXT...")
    print(f"  Total words: {total_words}")
    print(f"  Unique words: {unique_words}")
    print(f"  Vocabulary coverage: {vocab_coverage:.1f}%")
    print(f"  Average word length: {avg_word_length:.2f} characters")
    
    # Only show top words for English (Tamil won't display in console)
    if language_name.lower() == "english":
        print(f"  Top 5 words: {top_words}")
    else:
        print(f"  Top 5 words: (see outputs/tamil_top_words.txt for Tamil words)")

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "vocab_coverage": vocab_coverage,
        "avg_word_length": avg_word_length,
        "ttr": ttr,
        "top_words": top_words
    }
