# 🚀 GloxPaw AI - Quick Start Guide

Get up and running in **5 minutes**.

---

## Step 1: Install Python (if needed)
- **Windows/Mac/Linux**: Download from [python.org](https://www.python.org/downloads/)
- **Minimum version**: Python 3.8+
- **Check installation**: `python --version`

---

## Step 2: Setup Project

### On macOS/Linux:
```bash
# Navigate to project directory
cd GloxPaw

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### On Windows (PowerShell):
```powershell
# Navigate to project directory
cd GloxPaw

# Create virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

## Step 3: Configure OpenRouter

### A. Get API Key (2 minutes)
1. Go to [OpenRouter.ai](https://openrouter.ai)
2. Click "Keys" in navigation
3. Copy your API key

### B. Setup .env File
```bash
# Copy template
cp .env.example .env

# Edit with your text editor (or below):
```

Open `.env` and fill in:
```env
OPENROUTER_API_KEY=sk-or-your-actual-key-here
OPENROUTER_MODEL=openai/gpt-4-vision
```

**Save the file.**

---

## Step 4: Test It

```bash
# Make sure virtual environment is active
# Then run:
python main.py
```

When prompted:
```
Enter the path to an animal image: /path/to/your/dog.jpg
```

**That's it!** 🎉

The system will:
1. Process your image
2. Analyze it with AI
3. Generate a report
4. Save it to `outputs/`

---

## Troubleshooting

### "OPENROUTER_API_KEY not found"
- ✅ Make sure `.env` file exists (not `.env.example`)
- ✅ Make sure `.env` is in same folder as `main.py`
- ✅ Restart terminal after creating `.env`

### "ModuleNotFoundError: No module named 'requests'"
- ✅ Make sure virtual environment is activated
- ✅ Run: `pip install -r requirements.txt` again

### Image not found
- ✅ Use full path: `/Users/name/Pictures/dog.jpg`
- ✅ Or relative path: `./images/dog.jpg`
- ✅ Supported formats: JPG, PNG, GIF, WebP, BMP

### "Connection timeout"
- ✅ Check internet connection
- ✅ Check OpenRouter API key is valid
- ✅ Try again (temporary issue)

---

## What Happens Next?

### First Run (May Take 10-30 Seconds)
- API connects to OpenRouter
- Image is analyzed
- Report is generated
- File is saved

### Subsequent Runs
- Should be faster (~10-20 seconds)
- OpenRouter caches some requests

---

## Common Tasks

### Analyze Multiple Images
```bash
python main.py
# Analyzes first image
# Enter path to next image when prompted
```

### Check Generated Reports
```bash
# Look in the outputs/ folder
ls outputs/
# Or on Windows:
dir outputs
```

### Change AI Model
Edit `.env`:
```env
OPENROUTER_MODEL=openai/gpt-4o
# or
OPENROUTER_MODEL=anthropic/claude-3-opus
```

See [model list in README](README.md#choosing-a-model).

---

## Next Steps

- 📖 Read [README.md](README.md) for full documentation
- 🔍 Explore [outputs/] folder for generated reports
- 🐾 Try analyzing different animal photos
- 💬 Check [OpenRouter docs](https://openrouter.ai/docs) for API info

---

## Getting Help

1. **Check README.md** for detailed docs
2. **Check .env configuration** - most issues here
3. **Test your API key** at [OpenRouter.ai](https://openrouter.ai)
4. **Try a different model** in `.env`

---

Enjoy analyzing your animal photos! 🐾
