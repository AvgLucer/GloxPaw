#!/usr/bin/env python3
"""
GloxPaw AI - Animal Welfare Analysis Tool
Main entry point for the application
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from image_processor import ImageProcessor
from analyzer import AnimalAnalyzer
from report_generator import ReportGenerator

# Load environment variables
load_dotenv()

def validate_environment():
    """Check that required environment variables are set"""
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL")
    
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found in .env")
        print("   Please add your OpenRouter API key to .env file")
        sys.exit(1)
    
    if not model:
        print("❌ Error: OPENROUTER_MODEL not found in .env")
        print("   Please specify a model in .env (e.g., openai/gpt-4-vision)")
        sys.exit(1)
    
    return api_key, model

def main():
    """Main application flow"""
    print("\n" + "="*50)
    print("🐾 GloxPaw AI - Animal Welfare Analyzer")
    print("="*50 + "\n")
    
    # Validate environment
    api_key, model = validate_environment()
    
    # Get image path from user
    image_path = input("Enter the path to an animal image: ").strip()
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        sys.exit(1)
    
    print(f"\n📸 Loading image: {image_path}")
    
    # Process image
    image_processor = ImageProcessor()
    image_data = image_processor.load_and_encode(image_path)
    
    if image_data is None:
        print("❌ Failed to process image")
        sys.exit(1)
    
    print("✓ Image loaded successfully")
    
    # Analyze with AI
    print("\n🧠 Analyzing image with GloxPaw AI...")
    analyzer = AnimalAnalyzer(api_key=api_key, model=model)
    analysis = analyzer.analyze(image_data, image_path)
    
    if analysis is None:
        print("❌ Analysis failed")
        sys.exit(1)
    
    # Generate report
    print("📋 Generating welfare report...")
    report_generator = ReportGenerator()
    report = report_generator.generate_report(analysis)
    
    # Display report
    print("\n" + report)
    
    # Save report
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    image_name = Path(image_path).stem
    report_path = output_dir / f"{image_name}_analysis.txt"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\n💾 Report saved to: {report_path}")

if __name__ == "__main__":
    main()
