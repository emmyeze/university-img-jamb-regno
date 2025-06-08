import os
import pandas as pd
import shutil

def rename_passport_images(csv_path, input_folder, output_folder):
    # Load the mapping from the CSV
    df = pd.read_csv(csv_path)
    mapping = dict(zip(df['jambno'].astype(str), df['regno'].astype(str)))
    # print("mapping::", mapping)
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        jambno, ext = os.path.splitext(filename)
        if jambno in mapping:
            regno = mapping[jambno]
            new_filename = f"{regno}{ext}"
            src_path = os.path.join(input_folder, filename)
            dst_path = os.path.join(output_folder, new_filename)
            shutil.copy2(src_path, dst_path)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Skipped: {filename} (no matching jambno)")

# Example usage
rename_passport_images(
    csv_path='jamb_regno.csv',
    input_folder='passport_input',
    output_folder='passport_output'
)
