import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import os

# Load Tamil Unicode font with fallback
tamil_font_path = "C:/Windows/Fonts/NotoSansTamil-Regular.ttf"
tamil_font = None

if os.path.exists(tamil_font_path):
    tamil_font = fm.FontProperties(fname=tamil_font_path)
    mpl.rcParams['font.family'] = tamil_font.get_name()
else:
    # Try alternative Tamil fonts that might be available
    alt_fonts = [
        "C:/Windows/Fonts/Latha.ttf",
        "C:/Windows/Fonts/Vijaya.ttf",
        "C:/Windows/Fonts/arial.ttf"  # fallback to Arial
    ]
    for font_path in alt_fonts:
        if os.path.exists(font_path):
            tamil_font = fm.FontProperties(fname=font_path)
            print(f"Using fallback font: {font_path}")
            break
    
    if tamil_font is None:
        print("Warning: No suitable Tamil font found. Using default font.")

mpl.rcParams['axes.unicode_minus'] = False

def plot_top_words(csv_file, title, out_file, is_tamil=False):
    df = pd.read_csv(csv_file).head(20)

    plt.figure(figsize=(14, 6))  # wider figure
    plt.bar(range(len(df)), df["frequency"])

    if is_tamil:
        xtick_kwargs = {
            "rotation": 45,
            "ha": "right",
            "fontsize": 11
        }
        title_kwargs = {"fontsize": 14}
        
        if tamil_font is not None:
            xtick_kwargs["fontproperties"] = tamil_font
            title_kwargs["fontproperties"] = tamil_font
        
        plt.xticks(range(len(df)), df["word"], **xtick_kwargs)
        plt.title(title, **title_kwargs)
    else:
        plt.xticks(
            range(len(df)),
            df["word"],
            rotation=45,
            ha="right",
            fontsize=11
        )
        plt.title(title, fontsize=14)

    plt.ylabel("Frequency")
    plt.subplots_adjust(bottom=0.35)  # 🔥 KEY FIX
    plt.savefig(out_file, dpi=300)
    plt.close()

# English plot
plot_top_words(
    "outputs/english_vocab.csv",
    "Top English Words",
    "outputs/english_top_words.png",
    is_tamil=False
)

# Tamil plot
plot_top_words(
    "outputs/tamil_vocab.csv",
    "Top Tamil Words",
    "outputs/tamil_top_words.png",
    is_tamil=True
)
