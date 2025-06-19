# Splice Sample Organizer

Organize your Splice sample library automatically into a clean, structured folder system by category and usage type (loops / one shots). Only new files are processed each time — perfect for ongoing syncs.

---

## 🧠 Features

- Automatically categorizes samples from your Splice folder.
- Sorts by category (Drums, FX, Bass, Vocals, etc.).
- Detects and separates `Loops` vs `One Shots` when needed.
- Only organizes **new** files — never overwrites or duplicates.
- Maintains a `processed_files.json` log to avoid reprocessing.
- Flexible and fully editable category system via JSON.

---

## 📁 Folder Structure Example

```
Samples/
├── Drums/
│   ├── Kick/
│   │   ├── Loops/
│   │   └── One Shot/
│   └── Drum Loops/
├── Bass/
│   ├── 808/
│   └── Reese/
├── FX/
│   ├── Impact/
│   └── Sweep/
├── Vocals/
├── Unknown/
```

---

## 🛠 Setup

### For Mac/Linux:

1. **Clone the repo:**
   ```bash
   git clone git@github.com:YOUR_USERNAME/splice_sample_organizer.git
   cd splice_sample_organizer
   ```

2. **Install Python dependencies (if needed):**
   ```bash
   pip3 install -r requirements.txt  # Optional, only if you use external packages
   ```

3. **Edit the `organizer_script.py`:**
   Update these lines to match your folder paths:
   ```python
   source_folder = os.path.expanduser("~/Splice/sounds")
   destination_folder = "/Users/YOURNAME/Path/To/Your/Samples"
   ```

4. **Run the script:**
   ```bash
   python3 organizer_script.py
   ```

---

### For Windows:

1. **Clone the repo (via Git Bash or Terminal):**
   ```bash
   git clone git@github.com:YOUR_USERNAME/splice_sample_organizer.git
   cd splice_sample_organizer
   ```

2. **Install Python dependencies (if needed):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Edit `organizer_script.py`:**
   Update these lines:
   ```python
   source_folder = "C:/Users/YOURNAME/Splice/sounds"
   destination_folder = "D:/Path/To/Your/Samples"
   ```

4. **Run the script:**
   ```bash
   python organizer_script.py
   ```

---

## 🗂 Customizing Categories

Edit `categories.json` to define how files should be categorized.

```json
"snare_roll": ["Fillers", "Snare Roll"],
"vocal_chop": ["Vocals"]
```

Each entry follows the format:

```json
"keyword_in_filename": ["Main Category", "Sub Category (optional)"]
```

---

## 🤖 Pro Tip: Use AI to Generate Your `categories.json`

You can use ChatGPT or another LLM to generate your personalized `categories.json`. Just provide it with a list of your Splice sample filenames and ask it to suggest category mappings.

### Example prompt:
> “Here's a list of Splice sample filenames. Can you help categorize them by instrument and usage type for organizing?”

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
