from pathlib import Path
import pandas as pd

source = Path("data/raw/SMSSpamCollection")

df = pd.read_csv(
    source,
    sep="\t",
    header=None,
    names=["label", "text"]
)

output = Path("data/raw/sms_spam.csv")

df.to_csv(
    output,
    index=False
)

print(output)
print(df.shape)