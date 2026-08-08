![GloxPaw AI Banner](anipaw.gif)

<div align="center">

# 🐾 GloxPaw AI

**Animal Welfare Analysis Tool Powered by AI**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![OpenRouter API](https://img.shields.io/badge/OpenRouter%20API-Integration-success?style=flat-square&logo=openai)](https://openrouter.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)](https://github.com)
[![Code style: Python](https://img.shields.io/badge/Code%20Style-Python-informational?style=flat-square)](https://www.python.org/dev/peps/pep-0008/)
[![Vision AI Enabled](https://img.shields.io/badge/Vision%20AI-Enabled-blueviolet?style=flat-square)](https://openrouter.ai/docs/models)

**Comprehensive animal image analysis with focus on welfare, behavior, and care guidance.**

[Quick Start](#-quick-start) • [Features](#-features) • [Installation](#-installation) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📸 What is GloxPaw AI?

GloxPaw is an **intelligent animal welfare assessment tool** that analyzes photos to provide comprehensive insights about animals' behavioral states, physical condition, and environmental factors. Unlike simple breed classifiers, GloxPaw emphasizes **animal wellbeing** with responsible, confidence-based assessments and clear professional consultation recommendations.

Upload an animal photo → Get a detailed welfare report in seconds.

---

## ✨ Features

### 🎯 **Comprehensive Analysis**
- 🐕 **Species & Breed Identification** - Accurate breed detection with confidence levels
- 😊 **Behavioral Assessment** - Posture, ear position, facial expression analysis
- 👀 **Body Language** - Detailed posture and tension indicators
- 🩺 **Physical Observations** - Coat condition, body composition, visible characteristics
- 🌡️ **Environmental Context** - Setting, conditions, enrichment, hazards
- 💭 **Welfare Indicators** - Positive signs, concerns for observation, assessment limitations
- 📋 **Care Recommendations** - Species-appropriate suggestions and professional consultation flags

### 🧠 **AI-Powered**
- Uses OpenRouter API for flexible model selection
- Works with 50+ AI models (GPT-4, Claude, etc.)
- Confidence-based assessments (not diagnosis)
- Responsible uncertainty disclaimers

### 📊 **Structured Reports**
- Professional, formatted output
- Clear sections with emoji indicators
- Welfare-focused language
- Actionable recommendations

### 🔒 **Privacy-Conscious**
- Local image processing
- Simple `.env` configuration
- No data persistence
- Open source

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenRouter API key ([get one free](https://openrouter.ai))
- Internet connection

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/gloxpaw.git
cd gloxpaw

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env and add your OpenRouter API key
```

### Configuration

Edit `.env`:
```env
OPENROUTER_API_KEY=sk-or-your-api-key-here
OPENROUTER_MODEL=anthropic/claude-3-haiku
```

### First Run

```bash
# Verify setup (recommended)
python test_setup.py

# Run analysis
python main.py

# When prompted:
# Enter the path to an animal image: ./dog.jpg
```

Report saves to `outputs/` directory automatically.

---

## 📚 Documentation

| Document | Purpose | Time |
|----------|---------|------|
| [QUICKSTART.md](QUICKSTART.md) | Get started in 5 minutes | 5 min |
| [README.md](README.md) | Full detailed documentation | 15 min |
| [MODELS.md](MODELS.md) | AI model selection guide | 10 min |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Code architecture | 10 min |

---

## 📂 Project Structure

```
gloxpaw/
├── main.py                 # Application entry point
├── analyzer.py            # OpenRouter API integration
├── image_processor.py     # Image handling & encoding
├── report_generator.py    # Report formatting
├── prompts.py             # AI analysis prompts
├── test_setup.py          # Configuration verification
│
├── requirements.txt       # Python dependencies
├── .env.example          # Configuration template
├── .gitignore            # Git ignore patterns
│
├── outputs/              # Generated reports (auto-created)
└── README.md             # Full documentation
```

---

## 🧠 How It Works

```
1. User uploads animal image
   ↓
2. Image validation & optimization
   ↓
3. Image encoded to Base64
   ↓
4. Sent to OpenRouter API with analysis prompt
   ↓
5. AI model analyzes image
   ↓
6. Response parsed & formatted
   ↓
7. Beautiful welfare report generated
   ↓
8. Report saved to outputs/
```

---

## 💰 Cost

### Using Anthropic Claude 3 Haiku
```
Per analysis: $0.001 - $0.003
100 analyses: ~$0.10 - $0.30
1000 analyses: ~$1.00 - $3.00
```

### Free Trial
- Get free credits on OpenRouter signup
- Usually enough for 5-10 test analyses

See [MODELS.md](MODELS.md) for complete cost comparison.

---

## 🎯 Sample Output

```
╔═══════════════════════════════════════════════╗
║           🐾 GLOXPAW AI ANALYSIS 🐾          ║
║          Animal Welfare Assessment           ║
╚═══════════════════════════════════════════════╝

==================================================
SPECIES & BREED IDENTIFICATION
==================================================
Species: Dog
Confidence: 98%

Likely breed: Golden Retriever
Confidence: 82%

==================================================
BEHAVIORAL OBSERVATIONS
==================================================
Posture: Relaxed
Ear Position: Neutral
Primary State: Relaxed/Comfortable
Confidence: 85%

==================================================
WELFARE ASSESSMENT
==================================================
✅ Positive Indicators:
   ✓ Relaxed body posture
   ✓ Alert but comfortable positioning

==================================================
RECOMMENDATIONS
==================================================
✅ Care Suggestions:
   - Regular exercise (1-2 hours daily)
   - Mental enrichment and training
   - Consistent grooming
```

---

## 🔧 Configuration

### OpenRouter Models

**Recommended (Best Value):**
```env
OPENROUTER_MODEL=anthropic/claude-3-haiku
```

**Best Quality:**
```env
OPENROUTER_MODEL=openai/gpt-4-vision
```

**Fast & Good:**
```env
OPENROUTER_MODEL=openai/gpt-4o
```

See [MODELS.md](MODELS.md) for complete model comparison.

---

## 🐛 Troubleshooting

### API Key Issues
```
❌ OPENROUTER_API_KEY not found in .env
```
**Solution**: Create `.env` from `.env.example` and add your key

### Model Not Found
```
❌ 404 Not Found - Invalid model
```
**Solution**: Ensure model supports vision. Use `anthropic/claude-3-haiku` or `openai/gpt-4o`

### Image Format Error
```
❌ Unsupported image format
```
**Solution**: Convert to JPG, PNG, GIF, WebP, or BMP

See [README.md](README.md#troubleshooting) for more troubleshooting.

---

## ⚠️ Important Disclaimers

### What GloxPaw CANNOT Do
- ❌ Diagnose medical conditions
- ❌ Assess pain levels
- ❌ Determine genetic health
- ❌ Replace veterinary examination
- ❌ Provide definitive behavioral assessment

### What GloxPaw CAN Do
- ✅ Identify likely species/breed
- ✅ Describe visible characteristics
- ✅ Assess behavioral cues from photos
- ✅ Provide welfare-focused observations
- ✅ Suggest when professional consultation is needed

**Always consult veterinarians or behavioral professionals for medical or serious behavioral concerns.**

---

## 🎓 Key Principles

### 1. Confidence-First Approach
All assessments include confidence levels:
```
Primary State: Relaxed
Confidence: 82%
```

### 2. Clear Limitations
Transparent about what cannot be assessed from photos:
```
❌ Cannot Assess From Photo:
   • Pain levels
   • Internal health conditions
   • Long-term behavior patterns
```

### 3. Welfare-Focused
Recommendations emphasize animal wellbeing and professional consultation

### 4. No Diagnosis
Medical observations are marked as visual-only observations only

---

## 📋 Requirements

```
Python 3.8+
requests==2.31.0
python-dotenv==1.0.0
Pillow==10.1.0
```

---

## 🔐 Security

- ✅ API keys stored in `.env` (not in code)
- ✅ `.env` in `.gitignore` (never committed)
- ✅ No hardcoded secrets
- ✅ Local image processing
- ✅ HTTPS communication with OpenRouter

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- [ ] Support for more image formats
- [ ] Batch image processing
- [ ] Web interface
- [ ] Additional AI models
- [ ] Multilingual support
- [ ] Performance optimization

**To contribute:**
1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [OpenRouter](https://openrouter.ai) - API infrastructure
- [OpenAI](https://openai.com) - GPT-4 Vision model
- [Anthropic](https://anthropic.com) - Claude models
- [Python community](https://python.org) - Amazing tools

---

## 📞 Support

### Resources
- 📖 [Full Documentation](README.md)
- ⚡ [Quick Start Guide](QUICKSTART.md)
- 🧠 [Model Selection Guide](MODELS.md)
- 🏗️ [Project Architecture](PROJECT_STRUCTURE.md)

### Getting Help
1. Check [README.md](README.md) troubleshooting section
2. Run `python test_setup.py` to verify configuration
3. Check [OpenRouter Documentation](https://openrouter.ai/docs)
4. Open an issue on GitHub

---

## 🔮 Roadmap

### v1.0 (Current)
- ✅ Core animal analysis
- ✅ Multi-model support
- ✅ Welfare-focused reports

### v1.1 (Planned)
- [ ] Batch processing
- [ ] Multiple image comparison
- [ ] Custom prompts

### v2.0 (Future)
- [ ] Web interface
- [ ] Mobile app
- [ ] Video analysis
- [ ] Real-time monitoring

---

<div align="center">

### 🐾 Support Animal Welfare with GloxPaw AI

**Help animals through better observation and care.**

[Star us on GitHub](https://github.com) • [Report Issues](https://github.com/issues) • [View Documentation](README.md)

---

Made with ❤️ for animal lovers and welfare advocates

**Remember**: GloxPaw is an observation tool. Always prioritize professional assessment for medical or behavioral concerns.

</div>

