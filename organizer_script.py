import os
import shutil
import json
from collections import defaultdict

def title_case_or_raw(name):
    return name if name is None else ' '.join(word.capitalize() for word in name.split())

# Load categories
with open('categories.json', 'r') as f:
    raw_categories = json.load(f)

categories = {}
for keyword, value in raw_categories.items():
    if isinstance(value, list):
        main_cat = value[0]
        sub_cat = value[1] if len(value) > 1 else None
        categories[keyword.lower()] = (main_cat, sub_cat)

# Flat-only folders (no Loops/One Shot)
flat_only_folders = {
    ("Drums", "Drum Loops"),
    ("Fillers", "Snare Roll"),
    ("Fillers", "Long Fill"),
    ("Fillers", "Short Fill"),
    ("Fillers", "Dubstep Fill"),
    ("Fillers", "Rise"),
    ("Vocals", None)
}

# Paths
source_folder = os.path.expanduser("~/Splice/sounds")
destination_folder = "/Users/gabe/Library/CloudStorage/GoogleDrive-gabrielfquadrado@gmail.com/My Drive/5. Music/0. Samples"
backup_folder = os.path.join(destination_folder, "Unknown")
os.makedirs(backup_folder, exist_ok=True)

# Load or initialize processed file list
processed_log_path = os.path.join(destination_folder, "processed_files.json")
if os.path.exists(processed_log_path):
    with open(processed_log_path, 'r') as f:
        processed_files = set(json.load(f))
else:
    processed_files = set()

# Track what’s matched
file_matches = []
usage_type_tracker = defaultdict(lambda: {"loops": 0, "one_shot": 0})

# Scan source folder
for root, _, files in os.walk(source_folder):
    for file in files:
        if not file.lower().endswith(('.wav', '.aiff')):
            continue
        if file in processed_files:
            continue  # Skip already processed

        file_lower = file.lower()
        usage = "loops" if "loop" in file_lower or "bpm" in file_lower else "one_shot"
        matched = False

        for keyword in categories:
            if keyword in file_lower:
                main_cat, sub_cat = categories[keyword]
                key = (main_cat, sub_cat)
                usage_type_tracker[key][usage] += 1
                file_matches.append((os.path.join(root, file), file, key, usage))
                matched = True
                break

        if not matched:
            file_matches.append((os.path.join(root, file), file, None, usage))

# Move/copy files
for src_file, filename, key, usage in file_matches:
    if filename in processed_files:
        continue  # Redundant, but extra safe

    if key:
        main_cat_raw, sub_cat_raw = key
        main_cat = title_case_or_raw(main_cat_raw)
        sub_cat = title_case_or_raw(sub_cat_raw)
        base_path = os.path.join(destination_folder, main_cat)
        if sub_cat:
            base_path = os.path.join(base_path, sub_cat)

        both_types = usage_type_tracker[key]["loops"] > 0 and usage_type_tracker[key]["one_shot"] > 0

        if key in flat_only_folders:
            dest_path = base_path
        elif both_types:
            usage_folder = "Loops" if usage == "loops" else "One Shot"
            dest_path = os.path.join(base_path, usage_folder)
        else:
            dest_path = base_path
    else:
        dest_path = backup_folder

    os.makedirs(dest_path, exist_ok=True)
    dst_file = os.path.join(dest_path, filename)

    if os.path.abspath(src_file) != os.path.abspath(dst_file) and not os.path.exists(dst_file):
        shutil.copy2(src_file, dst_file)
        print(f"✅ Copied: {filename} → {dest_path}")
        processed_files.add(filename)
    else:
        print(f"⚠️ Skipped (exists or already processed): {filename}")

# Save processed file list
with open(processed_log_path, 'w') as f:
    json.dump(sorted(processed_files), f, indent=2)

print("🎉 Done! Only new files were organized.")
