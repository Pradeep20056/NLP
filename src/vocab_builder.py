from collections import Counter
import pandas as pd

def build_vocab(tokens, output_file):
    counter = Counter(tokens)
    df = pd.DataFrame(counter.items(), columns=["word", "frequency"])
    df = df.sort_values(by="frequency", ascending=False)
    df.to_csv(output_file, index=False)
    return df
