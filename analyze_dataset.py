import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Find CSV files inside data/
# --------------------------------------------------
data_folder = Path("data")
csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    print("❌ No CSV file found inside the data folder.")
    print(f"Expected location: {data_folder.resolve()}")
    raise SystemExit

print("\nCSV files found:")
for i, file in enumerate(csv_files, 1):
    print(f"{i}. {file.name}")

# If there is only one CSV, use it automatically
if len(csv_files) == 1:
    dataset_path = csv_files[0]
else:
    choice = int(input("\nEnter the number of the disease dataset: "))
    dataset_path = csv_files[choice - 1]

print(f"\n📂 Reading: {dataset_path}")

# --------------------------------------------------
# Load dataset
# --------------------------------------------------
df = pd.read_csv(dataset_path)

print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nColumns:")
for column in df.columns:
    print(f"  - {column}")

# --------------------------------------------------
# Disease information
# --------------------------------------------------
disease_column = "Disease"

if disease_column in df.columns:
    diseases = (
        df[disease_column]
        .dropna()
        .astype(str)
        .str.strip()
    )

    print("\n" + "=" * 60)
    print("DISEASE INFORMATION")
    print("=" * 60)

    print(f"Unique diseases: {diseases.nunique()}")

    print("\nDisease distribution:")
    for disease, count in diseases.value_counts().items():
        print(f"  {disease}: {count}")

# --------------------------------------------------
# Find symptom columns automatically
# --------------------------------------------------
symptom_columns = [
    col for col in df.columns
    if col.strip().lower().startswith("symptom_")
]

print("\n" + "=" * 60)
print("SYMPTOM COLUMNS")
print("=" * 60)

print(f"Number of symptom columns: {len(symptom_columns)}")

for column in symptom_columns:
    print(f"  - {column}")

# --------------------------------------------------
# Extract ALL unique symptoms
# --------------------------------------------------
all_symptoms = set()

for column in symptom_columns:
    values = (
        df[column]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
    )

    for value in values:
        if value:
            all_symptoms.add(value)

all_symptoms = sorted(all_symptoms)

print("\n" + "=" * 60)
print("SYMPTOM VOCABULARY")
print("=" * 60)

print(f"Total unique symptoms: {len(all_symptoms)}")

for i, symptom in enumerate(all_symptoms, 1):
    print(f"{i:3}. {symptom}")

# --------------------------------------------------
# Symptom frequency
# --------------------------------------------------
symptom_frequency = {}

for column in symptom_columns:
    values = (
        df[column]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
    )

    for symptom in values:
        if symptom:
            symptom_frequency[symptom] = (
                symptom_frequency.get(symptom, 0) + 1
            )

print("\n" + "=" * 60)
print("MOST COMMON SYMPTOMS")
print("=" * 60)

for symptom, count in sorted(
    symptom_frequency.items(),
    key=lambda x: x[1],
    reverse=True
)[:30]:
    print(f"  {symptom}: {count}")

# --------------------------------------------------
# Missing values
# --------------------------------------------------
print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing = df.isna().sum()

for column, count in missing.items():
    if count > 0:
        print(f"  {column}: {count}")

# --------------------------------------------------
# Duplicate rows
# --------------------------------------------------
print("\n" + "=" * 60)
print("DUPLICATES")
print("=" * 60)

print(f"Duplicate rows: {df.duplicated().sum()}")

# --------------------------------------------------
# Save compact analysis
# --------------------------------------------------
output_file = Path("dataset_analysis.txt")

with open(output_file, "w", encoding="utf-8") as f:

    f.write("MEDIPREDICT DATASET ANALYSIS\n")
    f.write("=" * 60 + "\n\n")

    f.write(f"Dataset: {dataset_path.name}\n")
    f.write(f"Rows: {len(df)}\n")
    f.write(f"Columns: {len(df.columns)}\n\n")

    f.write("COLUMNS\n")
    f.write("-" * 60 + "\n")
    for column in df.columns:
        f.write(f"{column}\n")

    if disease_column in df.columns:
        f.write("\nDISEASES\n")
        f.write("-" * 60 + "\n")
        f.write(f"Unique diseases: {diseases.nunique()}\n\n")

        for disease, count in diseases.value_counts().items():
            f.write(f"{disease}: {count}\n")

    f.write("\nSYMPTOMS\n")
    f.write("-" * 60 + "\n")
    f.write(f"Unique symptoms: {len(all_symptoms)}\n\n")

    for i, symptom in enumerate(all_symptoms, 1):
        f.write(f"{i}. {symptom}\n")

    f.write("\nSYMPTOM FREQUENCY\n")
    f.write("-" * 60 + "\n")

    for symptom, count in sorted(
        symptom_frequency.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        f.write(f"{symptom}: {count}\n")

    f.write("\nMISSING VALUES\n")
    f.write("-" * 60 + "\n")

    for column, count in missing.items():
        if count > 0:
            f.write(f"{column}: {count}\n")

    f.write(f"\nDuplicate rows: {df.duplicated().sum()}\n")

print("\n" + "=" * 60)
print("✅ ANALYSIS COMPLETE")
print("=" * 60)

print(f"\nCreated: {output_file.resolve()}")
print("\nYou can send me the generated dataset_analysis.txt file.")