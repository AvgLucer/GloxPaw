# 🐾 GloxPaw AI - Project Structure

Complete overview of the project files and their purposes.

---

## Directory Layout

```
GloxPaw/
├── 📄 Core Application Files
│   ├── main.py                 # Entry point - run with: python main.py
│   ├── analyzer.py             # OpenRouter API integration (uses .send() pattern)
│   ├── image_processor.py      # Image loading, validation, optimization
│   ├── report_generator.py     # Report formatting and generation
│   └── prompts.py              # AI analysis prompts
│
├── 📋 Configuration Files
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example            # Template for .env file (COPY THIS TO .env)
│   ├── .env                    # Your actual configuration (GITIGNORED)
│   └── .gitignore              # Git ignore patterns
│
├── 📚 Documentation
│   ├── README.md               # Full documentation
│   ├── QUICKSTART.md           # 5-minute setup guide
│   ├── MODELS.md               # AI model recommendations
│   ├── PROJECT_STRUCTURE.md    # This file
│   └── ...
│
├── 🧪 Testing
│   └── test_setup.py           # Configuration verification script
│
└── 📁 Output Directory (auto-created)
    └── outputs/
        ├── dog_analysis.txt    # Generated reports
        └── cat_analysis.txt    # (created automatically)
```

---

## File Descriptions

### Core Application Files

#### `main.py`
- **Purpose**: Application entry point
- **Usage**: `python main.py`
- **Flow**:
  1. Validates environment variables
  2. Prompts for image path
  3. Processes image
  4. Calls analyzer
  5. Generates report
  6. Saves output

#### `analyzer.py`
- **Purpose**: OpenRouter API integration
- **Key Features**:
  - Uses `.send()` pattern (HTTP requests)
  - Handles image encoding
  - Parses API responses
  - Error handling
- **Main Class**: `AnimalAnalyzer`
- **Key Methods**:
  - `analyze()` - Main analysis function
  - `_send_request()` - HTTP request handling
  - `_parse_response()` - Response parsing

#### `image_processor.py`
- **Purpose**: Image handling
- **Features**:
  - Validates image format
  - Checks file size
  - Loads images with PIL
  - Converts to RGB
  - Optimizes dimensions
  - Encodes to Base64
- **Main Class**: `ImageProcessor`
- **Supported Formats**: JPG, PNG, GIF, WebP, BMP

#### `report_generator.py`
- **Purpose**: Report formatting
- **Features**:
  - Professional formatting
  - Section-by-section generation
  - Emoji indicators
  - Disclaimer inclusion
- **Main Class**: `ReportGenerator`
- **Output**: Beautiful ASCII formatted reports

#### `prompts.py`
- **Purpose**: AI prompt templates
- **Contains**:
  - `get_analysis_prompt()` - Main analysis prompt
  - `get_breed_classifier_prompt()` - Breed-specific
  - `get_behavior_analyzer_prompt()` - Behavior-specific
- **Usage**: Called by analyzer to construct prompts

---

### Configuration Files

#### `requirements.txt`
```
requests==2.31.0           # HTTP library for API calls
python-dotenv==1.0.0       # Environment variable loading
Pillow==10.1.0            # Image processing
```

**Installation**: `pip install -r requirements.txt`

#### `.env.example`
Template showing required configuration:
```env
OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=openai/gpt-4-vision
```

**Action Required**: Copy to `.env` and fill in your values

#### `.env` (Not included)
Your actual configuration. **NEVER commit to Git**.

Example:
```env
OPENROUTER_API_KEY=sk-or-...actual-key...
OPENROUTER_MODEL=openai/gpt-4-vision
```

#### `.gitignore`
Prevents sensitive files from being committed:
- `.env` (configuration)
- `__pycache__/` (Python cache)
- `.vscode/`, `.idea/` (IDE files)
- `outputs/` (generated reports)

---

### Documentation Files

#### `README.md` (8,000+ words)
**Comprehensive guide covering:**
- Quick start
- Features overview
- Installation instructions
- Configuration guide
- Usage examples
- Model recommendations
- Troubleshooting
- Limitations and disclaimers

**Read this for**: Full understanding of the project

#### `QUICKSTART.md` (300 words)
**5-minute setup guide covering:**
- Installation steps
- Configuration setup
- First run
- Troubleshooting

**Read this for**: Fast setup

#### `MODELS.md` (2,000+ words)
**Model selection guide covering:**
- Model recommendations
- Detailed comparisons
- Cost analysis
- Use case recommendations
- Troubleshooting

**Read this for**: Choosing the right AI model

#### `PROJECT_STRUCTURE.md` (This file)
**Project overview covering:**
- File descriptions
- Directory layout
- Purpose of each file
- Data flow

**Read this for**: Understanding the architecture

---

### Testing & Verification

#### `test_setup.py`
**Comprehensive setup verification script**

**Run before first use:**
```bash
python test_setup.py
```

**Checks:**
1. ✅ Environment variables
2. ✅ Python dependencies
3. ✅ Project files
4. ✅ API connection
5. ✅ Image processing

**Output**: Detailed report with solutions to any issues

---

### Output Directory

#### `outputs/` (Auto-created)
Generated reports are saved here:
```
outputs/
├── dog_analysis.txt          # Analysis of dog.jpg
├── cat_analysis.txt          # Analysis of cat.png
├── bird_analysis.txt         # Analysis of bird.jpg
└── ...
```

**File naming**: `{original_filename}_analysis.txt`

---

## Data Flow Diagram

```
User runs: python main.py
    ↓
main.py → Validates .env
    ↓
main.py → Gets image path from user
    ↓
image_processor.py → Loads & encodes image
    ↓
analyzer.py → Prepares prompt (prompts.py)
    ↓
analyzer.py → Sends to OpenRouter API
    ↓
OpenRouter → Returns analysis JSON
    ↓
analyzer.py → Parses response
    ↓
report_generator.py → Formats into report
    ↓
main.py → Displays report
    ↓
main.py → Saves to outputs/
    ↓
Report saved to: outputs/{filename}_analysis.txt
```

---

## Configuration Data Flow

```
.env.example (template)
    ↓
user copies to .env (not in git)
    ↓
user edits .env with API key and model
    ↓
main.py loads .env via python-dotenv
    ↓
environment variables available to all modules
    ↓
analyzer.py uses: OPENROUTER_API_KEY, OPENROUTER_MODEL
```

---

## OpenRouter API Integration

### How the `.send()` Pattern Works

The `.send()` pattern in OpenRouter is actually HTTP requests:

```python
# In analyzer.py:
response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        ...
    },
    json=payload
)

# OpenRouter receives this and "sends" back:
response.json()  # Contains analysis
```

### API Structure

```
Request:
  - Model name
  - Messages with image data
  - Temperature & max_tokens
  
Response:
  - Structured JSON analysis
  - Or error information
```

---

## File Dependencies

```
main.py
  ├─ image_processor.py
  ├─ analyzer.py
  │   ├─ prompts.py
  │   └─ requests (library)
  ├─ report_generator.py
  └─ python-dotenv (library)

image_processor.py
  ├─ PIL (Pillow)
  ├─ base64
  └─ io

analyzer.py
  ├─ requests
  ├─ json
  └─ prompts.py

report_generator.py
  ├─ json
  └─ datetime

test_setup.py
  ├─ python-dotenv
  ├─ requests
  └─ PIL (Pillow)
```

---

## Environment Variables

### Required Variables

#### `OPENROUTER_API_KEY`
- **Type**: String
- **Source**: Get from [OpenRouter.ai/keys](https://openrouter.ai/keys)
- **Used by**: analyzer.py
- **Format**: `sk-or-...` (starts with sk-or-)

#### `OPENROUTER_MODEL`
- **Type**: String (model identifier)
- **Example**: `openai/gpt-4-vision`
- **Used by**: analyzer.py
- **See**: MODELS.md for recommendations

### Optional Variables
Currently none (can be added for customization)

---

## File Sizes

| File | Size | Type |
|------|------|------|
| main.py | ~4 KB | Code |
| analyzer.py | ~6 KB | Code |
| image_processor.py | ~5 KB | Code |
| report_generator.py | ~10 KB | Code |
| prompts.py | ~3 KB | Code |
| test_setup.py | ~6 KB | Code |
| README.md | ~20 KB | Documentation |
| QUICKSTART.md | ~3 KB | Documentation |
| MODELS.md | ~8 KB | Documentation |
| PROJECT_STRUCTURE.md | ~6 KB | Documentation |
| requirements.txt | <1 KB | Config |
| .env.example | <1 KB | Config |
| .gitignore | ~1 KB | Config |
| **Total** | **~73 KB** | **All files** |

---

## Setup Checklist

- [ ] Install Python 3.8+
- [ ] Download/clone project
- [ ] Create virtual environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Copy `.env.example` to `.env`
- [ ] Get OpenRouter API key
- [ ] Edit `.env` with API key and model
- [ ] Run: `python test_setup.py`
- [ ] All checks pass ✅
- [ ] Run: `python main.py`
- [ ] Analyze your first image! 🐾

---

## Common Modifications

### Adding New Analysis Features
Edit `prompts.py` to add new analysis types

### Changing Report Format
Edit `report_generator.py` to customize output

### Supporting New Image Formats
Edit `image_processor.py` to add formats

### Using Different API
Replace OpenRouter integration in `analyzer.py`

---

## Security Considerations

✅ **What's Protected:**
- API keys stored in `.env` (not in code)
- `.env` in `.gitignore` (not committed)
- No hardcoded secrets

⚠️ **Best Practices:**
- Never share `.env` file
- Rotate API keys regularly
- Check git history: `git log -p -- .env`

---

## Performance Considerations

### Image Processing
- Max file size: 20 MB
- Max dimensions: 2000px
- JPEG quality: 85 (optimized)
- Processing time: <1 second per image

### API Calls
- Typical latency: 5-30 seconds
- Depends on model selected
- Depends on internet connection
- See MODELS.md for speed comparison

### Memory Usage
- Base application: ~50 MB
- Per image: ~10-50 MB (depending on size)
- Report generation: <1 MB

---

## Troubleshooting Guide

**Problem**: Import errors
**Solution**: `pip install -r requirements.txt`

**Problem**: API key not found
**Solution**: Check `.env` file exists and has correct path

**Problem**: Slow analysis
**Solution**: Choose faster model in `.env`

**Problem**: Image format not supported
**Solution**: Convert to JPG/PNG and try again

See **README.md** for more troubleshooting.

---

## Further Reading

1. **Getting Started**: QUICKSTART.md
2. **Full Documentation**: README.md
3. **Model Selection**: MODELS.md
4. **This Overview**: PROJECT_STRUCTURE.md
5. **OpenRouter Docs**: https://openrouter.ai/docs

---

**Questions?** Check README.md or QUICKSTART.md
