# 🧠 GloxPaw AI - Model Configuration Guide

Choose the right AI model for your needs.

---

## Quick Recommendations

### 🏆 Best Quality (Recommended)
```env
OPENROUTER_MODEL=openai/gpt-4-vision
```
- **Cost**: Higher
- **Speed**: Good
- **Vision**: Excellent
- **Best for**: Accurate breed identification, detailed analysis
- **Use when**: You want the best results and don't mind higher cost

### ⚡ Best Speed
```env
OPENROUTER_MODEL=openai/gpt-4o
```
- **Cost**: Medium
- **Speed**: Fast
- **Vision**: Excellent
- **Best for**: Quick analysis, frequent usage
- **Use when**: You want speed without sacrificing quality

### 💰 Best Value
```env
OPENROUTER_MODEL=anthropic/claude-3-sonnet
```
- **Cost**: Low
- **Speed**: Medium
- **Vision**: Good
- **Best for**: Budget-conscious, good quality
- **Use when**: You want to save money but still need good results

### 🔬 Best Reasoning
```env
OPENROUTER_MODEL=anthropic/claude-3-opus
```
- **Cost**: High
- **Speed**: Slower
- **Vision**: Excellent
- **Best for**: Complex behavior analysis
- **Use when**: You need detailed reasoning about animal behavior

---

## Detailed Model Comparison

### OpenAI Models

#### GPT-4 Vision
```env
OPENROUTER_MODEL=openai/gpt-4-vision
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐⭐⭐⭐ |
| Breed ID | ⭐⭐⭐⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐ |
| Cost | $$$ |

**Best for**: Premium animal analysis, exotic breeds, complex assessments

#### GPT-4o (Latest)
```env
OPENROUTER_MODEL=openai/gpt-4o
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐⭐⭐⭐ |
| Breed ID | ⭐⭐⭐⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ |
| Cost | $$ |

**Best for**: Regular use, good balance of quality and speed

#### GPT-4 Turbo
```env
OPENROUTER_MODEL=openai/gpt-4-turbo
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐⭐⭐ |
| Breed ID | ⭐⭐⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ |
| Cost | $$ |

**Best for**: Fast turnaround, good quality

#### GPT-3.5 Turbo
```env
OPENROUTER_MODEL=openai/gpt-3.5-turbo
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐⭐ |
| Breed ID | ⭐⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ |
| Cost | $ |

**Best for**: Budget-conscious, simple tasks

**Note**: Limited vision capabilities, may not identify breeds well

---

### Anthropic Claude Models

#### Claude 3 Opus
```env
OPENROUTER_MODEL=anthropic/claude-3-opus
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐⭐⭐⭐ |
| Breed ID | ⭐⭐⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐ |
| Cost | $$$ |

**Best for**: Complex reasoning, detailed behavior analysis

#### Claude 3 Sonnet
```env
OPENROUTER_MODEL=anthropic/claude-3-sonnet
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐⭐⭐ |
| Breed ID | ⭐⭐⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐ |
| Cost | $$ |

**Best for**: Good balance, recommended for most users

#### Claude 3 Haiku
```env
OPENROUTER_MODEL=anthropic/claude-3-haiku
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐⭐ |
| Breed ID | ⭐⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ |
| Cost | $ |

**Best for**: Fast, budget analysis

---

### Open Source Models

#### Llama 2 70B
```env
OPENROUTER_MODEL=meta-llama/llama-2-70b-chat
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐⭐ |
| Breed ID | ⭐⭐ |
| Behavioral Analysis | ⭐⭐⭐ |
| Speed | ⭐⭐⭐ |
| Cost | $ |

**Best for**: Privacy-conscious, doesn't use proprietary models

**Note**: Limited vision capabilities

#### Mistral 7B
```env
OPENROUTER_MODEL=mistralai/mistral-7b-instruct
```
| Feature | Rating |
|---------|--------|
| Visual Analysis | ⭐ |
| Breed ID | ⭐⭐ |
| Behavioral Analysis | ⭐⭐ |
| Speed | ⭐⭐⭐⭐⭐ |
| Cost | $ |

**Best for**: Very fast, budget limited

**Note**: Very limited vision capabilities

---

## Cost Comparison

### Estimated Cost Per Analysis
(Prices approximate as of August 2026)

| Model | Per Analysis | 100 Analyses |
|-------|------------|-------------|
| GPT-4 Vision | $0.05-0.10 | $5-10 |
| GPT-4o | $0.02-0.05 | $2-5 |
| GPT-4 Turbo | $0.01-0.03 | $1-3 |
| Claude 3 Opus | $0.03-0.06 | $3-6 |
| Claude 3 Sonnet | $0.01-0.02 | $1-2 |
| Claude 3 Haiku | $0.001-0.003 | $0.10-0.30 |
| Llama 2 70B | $0.0008-0.002 | $0.08-0.20 |

---

## My Recommendations by Use Case

### 🎯 First-Time Users
```env
OPENROUTER_MODEL=openai/gpt-4o
```
- **Why**: Best balance of quality, speed, and cost
- **Try**: Start here, then adjust if needed

### 🏆 Serious Animal Analysis
```env
OPENROUTER_MODEL=openai/gpt-4-vision
```
- **Why**: Best breed identification and detail
- **When**: Professional use, complex cases

### 💰 Budget-Conscious
```env
OPENROUTER_MODEL=anthropic/claude-3-haiku
```
- **Why**: Lowest cost, still decent quality
- **When**: Casual use, high volume

### ⚡ Fast Processing
```env
OPENROUTER_MODEL=openai/gpt-4o
```
- **Why**: Fastest with good quality
- **When**: Need quick results

### 🧠 Complex Behavior Analysis
```env
OPENROUTER_MODEL=anthropic/claude-3-opus
```
- **Why**: Best reasoning for behavioral interpretation
- **When**: Detailed behavioral assessment needed

### 📊 Frequent Batch Processing
```env
OPENROUTER_MODEL=anthropic/claude-3-sonnet
```
- **Why**: Good quality, reasonable cost
- **When**: Processing many images

---

## How to Try Different Models

### Quick Test
```bash
# Edit .env
OPENROUTER_MODEL=openai/gpt-4o

# Run analysis
python main.py
```

### Compare Results
1. Run with Model A
2. Note the output
3. Change .env to Model B
4. Run same image again
5. Compare reports

---

## Model Selection Flowchart

```
Start
  ↓
What's your priority?
  ├─ Best Quality? → GPT-4-Vision
  ├─ Fastest Results? → GPT-4o
  ├─ Lowest Cost? → Claude 3 Haiku
  ├─ Budget, Good Quality? → Claude 3 Sonnet
  └─ Complex Analysis? → Claude 3 Opus
```

---

## API Limits & Quotas

### Free Tier (OpenRouter)
- Limited requests per minute
- Lower priority queue
- Good for testing

### Pro Tier
- Higher rate limits
- Priority processing
- Better for production use

**Check limits**: [OpenRouter Dashboard](https://openrouter.ai/account/limits)

---

## Troubleshooting Model Issues

### "Model not found" Error
```
❌ Error: Model 'openai/gpt-4-vision' not found
```
**Solutions:**
1. Check model name spelling
2. Model might not be available in your region
3. Try a different model
4. Check [OpenRouter models list](https://openrouter.ai/docs/models)

### "Rate limit exceeded"
```
❌ Error: Rate limit exceeded
```
**Solutions:**
1. Wait a few minutes
2. Use cheaper model (higher quotas)
3. Upgrade to Pro tier
4. Spread requests over time

### Slow Response Times
**Solutions:**
1. Use faster model (GPT-4o)
2. Reduce image size
3. Try during off-peak hours
4. Check your internet connection

---

## Advanced: Available Models

Full list can change. Check [OpenRouter Models](https://openrouter.ai/docs/models) for current options.

**Vision-Capable (Recommended):**
- openai/gpt-4-vision
- openai/gpt-4o
- openai/gpt-4-turbo
- anthropic/claude-3-opus
- anthropic/claude-3-sonnet
- anthropic/claude-3-haiku

**Text-Only (Not Recommended for GloxPaw):**
- openai/gpt-3.5-turbo
- meta-llama/llama-2-70b
- mistralai/mistral-7b
- And others...

---

## Pro Tips

### 💡 Tier Models by Feature Importance

**If breed ID is most important**: GPT-4-Vision > GPT-4o > Claude 3 Opus

**If speed is most important**: GPT-4o > GPT-3.5-Turbo > Claude 3 Haiku

**If cost is most important**: Claude 3 Haiku > Llama 2 > GPT-3.5-Turbo

### 🔄 Switch Models Without Code Changes
Just edit `.env` and run again - no code changes needed!

### 📊 Monitor Costs
- Note which models you use
- Track cost per analysis
- Switch if costs seem high

### 🧪 A/B Test Models
- Run same image on 2 models
- Compare quality differences
- Choose best for your use case

---

## Recommended Reading
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Model Pricing](https://openrouter.ai/docs/models)
- [API Reference](https://openrouter.ai/docs/api/v1)

---

**Questions?** Check the [README.md](README.md) or [QUICKSTART.md](QUICKSTART.md)
