"""
Core analyzer module - handles OpenRouter API calls
"""

import json
import requests
import re
from prompts import get_analysis_prompt

class AnimalAnalyzer:
    """Analyzes animal images using OpenRouter API"""
    
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://openrouter.ai/api/v1"
    
    def analyze(self, image_data: str, image_path: str) -> dict:
        """
        Analyze an animal image
        
        Args:
            image_data: Base64 encoded image data
            image_path: Original image file path
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            # Prepare the message with vision capability
            message = self._build_vision_message(image_data)
            
            # Call OpenRouter API
            response = self._send_request(message)
            
            if response is None:
                return None
            
            # Parse the response
            analysis = self._parse_response(response)
            
            return analysis
            
        except Exception as e:
            print(f"❌ Analysis error: {str(e)}")
            return None
    
    def _build_vision_message(self, image_data: str) -> str:
        """Build the vision prompt with image"""
        analysis_prompt = get_analysis_prompt()
        
        # Return as dict with image and text (not string)
        return {
            "image": f"data:image/jpeg;base64,{image_data}",
            "prompt": analysis_prompt
        }
    
    def _send_request(self, message: dict) -> dict:
        """
        Send request to OpenRouter API
        
        Args:
            message: Dict containing image and prompt
            
        Returns:
            API response as dictionary or None on error
        """
        try:
            # Validate inputs
            if not self.api_key:
                print("❌ Error: No API key provided")
                return None
            
            if self.api_key == "your_openrouter_api_key_here":
                print("❌ Error: API key is still the placeholder value")
                print("   Please edit .env and add your actual OpenRouter API key")
                return None
            
            if not self.model:
                print("❌ Error: No model specified")
                return None
            
            print(f"🔑 Using model: {self.model}")
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/user/gloxpaw",
                "X-Title": "GloxPaw AI"
            }
            
            # Build payload with proper image_url format
            payload = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": message["image"]
                                }
                            },
                            {
                                "type": "text",
                                "text": message["prompt"]
                            }
                        ]
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 2000
            }
            
            # Make the request
            print("📡 Sending request to OpenRouter API...")
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=120
            )
            
            print(f"📋 Response status: {response.status_code}")
            
            # Check for errors
            if response.status_code == 401:
                print("❌ 401 Unauthorized - Invalid API key")
                print("   Check your OPENROUTER_API_KEY in .env")
                return None
            
            if response.status_code == 404:
                print("❌ 404 Not Found - Invalid model or endpoint")
                print(f"   Model: {self.model}")
                print("   Check your OPENROUTER_MODEL in .env")
                return None
            
            if response.status_code == 429:
                print("❌ 429 Rate Limited - Too many requests")
                print("   Wait a few moments and try again")
                return None
            
            response.raise_for_status()
            
            result = response.json()
            
            if "error" in result:
                print(f"❌ API Error: {result['error']}")
                return None
            
            print("✅ API response received successfully")
            return result
            
        except requests.exceptions.Timeout:
            print("❌ Request timeout - API took too long to respond")
            print("   Try again or use a faster model")
            return None
        except requests.exceptions.ConnectionError:
            print("❌ Connection error - Check your internet connection")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP Error: {str(e)}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ API request failed: {str(e)}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return None
    
    def _parse_response(self, response: dict) -> dict:
        """
        Parse OpenRouter API response
        
        Args:
            response: Raw API response dictionary
            
        Returns:
            Structured analysis dictionary
        """
        try:
            if "error" in response:
                print(f"❌ API Error: {response['error']}")
                return None
            
            # Extract the response text
            if not response.get("choices") or len(response["choices"]) == 0:
                print("❌ No response from model")
                return None
            
            response_text = response["choices"][0]["message"]["content"]
            
            print("🔍 Parsing model response...")
            
            # Try to parse as JSON (model should return structured JSON)
            try:
                analysis = json.loads(response_text)
                print("✅ Response parsed as JSON")
                return analysis
            except json.JSONDecodeError:
                print("⚠️  Response is not JSON, creating fallback structure...")
                # Fallback: create structured format from text response
                analysis = {
                    "species": "Analysis in progress",
                    "breed": "See raw response",
                    "breed_confidence": 0,
                    "behavioral_observations": {
                        "posture": "See analysis",
                        "raw_response": response_text[:500]
                    },
                    "welfare_observations": {
                        "positive_indicators": [],
                        "concerns_for_observation": [],
                        "cannot_assess": ["Full analysis in raw response above"]
                    },
                    "environment": "See analysis",
                    "recommendations": response_text,
                    "analysis_limitations": "Response was not in expected JSON format"
                }
                return analysis
            
        except Exception as e:
            print(f"❌ Error parsing response: {str(e)}")
            return None