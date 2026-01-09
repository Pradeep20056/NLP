import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from indicnlp.tokenize import indic_tokenize
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

nltk.download('stopwords')
nltk.download('wordnet')

# --------------------------------------------------
# EXPLICIT STOPWORDS (Manually Defined + Library)
# --------------------------------------------------

# Common English stopwords (explicit list – sample)
ENGLISH_STOPWORDS_CUSTOM = {
    "the", "is", "am", "are", "was", "were",
    "a", "an", "and", "or", "but",
    "in", "on", "at", "to", "from",
    "of", "for", "with", "by",
    "this", "that", "these", "those",
    "he", "she", "it", "they", "we", "you",
    "his", "her", "their", "our",
    "as", "if", "then", "so", "than",
    "not", "no", "yes", "do", "does", "did"
}

# Merge with NLTK stopwords
ENGLISH_STOPWORDS = set(stopwords.words("english")).union(ENGLISH_STOPWORDS_CUSTOM)


# Common Tamil stopwords (explicit list)
TAMIL_STOPWORDS = {
    "அது", "இது", "என்று", "மற்றும்", "ஆனால்",
    "என", "என்ற", "ஒரு", "இந்த", "அந்த",
    "இருக்கும்", "இருந்தது", "இருக்கிறது",
    "உள்ள", "உள்ளது", "மேலும்",
    "என்ன", "எப்படி", "எப்போது",
    "நான்", "நீ", "அவன்", "அவள்", "அவர்கள்",
    "எங்கள்", "உங்கள்", "அவர்களின்",
    "இல்லை", "ஆம்", "மிகவும்",
    "போல்", "மட்டும்", "கூட"
}

# --------------------------------------------------
# ENGLISH PREPROCESSING
# --------------------------------------------------

def preprocess_english(text):
    # Lowercasing
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenization
    tokens = text.split()

    # Stopword removal
    tokens = [w for w in tokens if w not in ENGLISH_STOPWORDS]

    # Stemming + Lemmatization
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    tokens = [lemmatizer.lemmatize(stemmer.stem(w)) for w in tokens]

    return tokens


# --------------------------------------------------
# TAMIL PREPROCESSING
# --------------------------------------------------

def preprocess_tamil(text):
    # Unicode normalization
    factory = IndicNormalizerFactory()
    normalizer = factory.get_normalizer("ta")
    text = normalizer.normalize(text)

    # Tokenization
    tokens = indic_tokenize.trivial_tokenize(text)

    # Keep only Tamil characters
    tokens = [t for t in tokens if re.match(r'^[\u0B80-\u0BFF]+$', t)]

    # Stopword removal
    tokens = [t for t in tokens if t not in TAMIL_STOPWORDS]

    return tokens
