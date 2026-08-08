#!/usr/bin/env python3
"""
GloxPaw Setup Verification Script
Run this to verify your configuration before using the main application
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def test_environment_variables():
    """Test that required environment variables are set"""
    print("\n" + "="*50)
    print("1️⃣  CHECKING ENVIRONMENT VARIABLES")
    print("="*50)
    
    load_dotenv()
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL")
    
    # Check API key
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found in .env")
        print("   Solution: Edit .env and add your OpenRouter API key")
        return False
    
    if api_key == "your_openrouter_api_key_here":
        print("❌ OPENROUTER_API_KEY is still the placeholder value")
        print("   Solution: Edit .env and add your actual API key")
        return False
    
    print("✅ OPENROUTER_API_KEY is set")
    print(f"   (Key starts with: {api_key[:10]}...)")
    
    # Check model
    if not model:
        print("❌ OPENROUTER_MODEL not found in .env")
        print("   Solution: Edit .env and specify a model (e.g., openai/gpt-4-vision)")
        return False
    
    if model == "openai/gpt-4-vision" or "gpt" in model.lower() or "claude" in model.lower():
        print("✅ OPENROUTER_MODEL is set")
        print(f"   Model: {model}")
    else:
        print("⚠️  OPENROUTER_MODEL is set but may not support vision")
        print(f"   Model: {model}")
        print("   Recommended: Use vision-capable models like gpt-4-vision, gpt-4o, or claude-3-opus")
    
    return True

def test_dependencies():
    """Test that required Python packages are installed"""
    print("\n" + "="*50)
    print("2️⃣  CHECKING DEPENDENCIES")
    print("="*50)
    
    dependencies = {
        'requests': 'requests',
        'dotenv': 'python-dotenv',
        'PIL': 'Pillow'
    }
    
    all_installed = True
    
    for module_name, package_name in dependencies.items():
        try:
            __import__(module_name)
            print(f"✅ {package_name} is installed")
        except ImportError:
            print(f"❌ {package_name} is NOT installed")
            print(f"   Solution: pip install {package_name}")
            all_installed = False
    
    return all_installed

def test_file_structure():
    """Test that project files exist"""
    print("\n" + "="*50)
    print("3️⃣  CHECKING PROJECT FILES")
    print("="*50)
    
    required_files = [
        'main.py',
        'analyzer.py',
        'image_processor.py',
        'report_generator.py',
        'prompts.py',
        '.env'
    ]
    
    all_exist = True
    current_dir = Path('.')
    
    for filename in required_files:
        filepath = current_dir / filename
        if filepath.exists():
            print(f"✅ {filename} exists")
        else:
            print(f"❌ {filename} NOT found")
            all_exist = False
    
    # Check outputs directory
    outputs_dir = current_dir / 'outputs'
    if outputs_dir.exists():
        print(f"✅ outputs/ directory exists")
    else:
        print(f"⚠️  outputs/ directory will be created on first run")
    
    return all_exist

def test_api_connection():
    """Test connection to OpenRouter API"""
    print("\n" + "="*50)
    print("4️⃣  TESTING API CONNECTION")
    print("="*50)
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL")
    
    if not api_key or api_key == "your_openrouter_api_key_here":
        print("⏭️  Skipping API test (no valid API key configured)")
        return None
    
    try:
        import requests
        
        print(f"Testing connection to OpenRouter...")
        print(f"Model: {model}")
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/user/gloxpaw",
            "X-Title": "GloxPaw-Setup-Test"
        }
        
        # Make a simple test request
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": "Say 'Hello, GloxPaw!' and nothing else."
                }
            ],
            "temperature": 0.7,
            "max_tokens": 100
        }
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()
        
        result = response.json()
        
        if "error" in result:
            print(f"❌ API Error: {result['error'].get('message', 'Unknown error')}")
            return False
        
        if result.get("choices") and len(result["choices"]) > 0:
            message = result["choices"][0]["message"]["content"]
            print(f"✅ API Connection successful!")
            print(f"   Response: {message[:50]}...")
            return True
        else:
            print(f"❌ Unexpected API response")
            return False
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection failed: {str(e)}")
        print(f"   Check your internet connection and API key")
        return False
    except Exception as e:
        print(f"❌ Error testing API: {str(e)}")
        return False

def test_image_processing():
    """Test that image processing dependencies work"""
    print("\n" + "="*50)
    print("5️⃣  CHECKING IMAGE PROCESSING")
    print("="*50)
    
    try:
        from PIL import Image
        import io
        import base64
        
        # Create a test image
        test_image = Image.new('RGB', (100, 100), color='red')
        
        # Try to encode it
        buffer = io.BytesIO()
        test_image.save(buffer, format='JPEG')
        buffer.seek(0)
        base64_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        if len(base64_string) > 100:
            print("✅ Image processing works correctly")
            return True
        else:
            print("❌ Image encoding failed")
            return False
    
    except Exception as e:
        print(f"❌ Image processing error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*50)
    print("🐾 GloxPaw AI - Setup Verification")
    print("="*50)
    
    results = {
        'Environment Variables': test_environment_variables(),
        'Dependencies': test_dependencies(),
        'Project Files': test_file_structure(),
        'Image Processing': test_image_processing(),
        'API Connection': test_api_connection()
    }
    
    # Summary
    print("\n" + "="*50)
    print("📋 VERIFICATION SUMMARY")
    print("="*50)
    
    passed = sum(1 for v in results.values() if v is True)
    failed = sum(1 for v in results.values() if v is False)
    skipped = sum(1 for v in results.values() if v is None)
    
    for test_name, result in results.items():
        if result is True:
            status = "✅ PASS"
        elif result is False:
            status = "❌ FAIL"
        else:
            status = "⏭️  SKIP"
        print(f"{status} - {test_name}")
    
    print("\n" + "-"*50)
    if failed == 0:
        print("🎉 All checks passed! You're ready to use GloxPaw!")
        print("\nRun: python main.py")
        return 0
    else:
        print(f"⚠️  {failed} check(s) failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("  1. Make sure .env file exists and is properly configured")
        print("  2. Run: pip install -r requirements.txt")
        print("  3. Check your internet connection")
        print("  4. Verify your OpenRouter API key at: https://openrouter.ai/keys")
        return 1

if __name__ == "__main__":
    sys.exit(main())
