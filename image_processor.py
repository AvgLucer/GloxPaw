"""
Image processing module - handles loading and encoding images
"""

import base64
import os
from pathlib import Path
from PIL import Image
import io

class ImageProcessor:
    """Handles image loading, validation, and encoding"""
    
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}
    MAX_SIZE_MB = 20
    
    def load_and_encode(self, image_path: str) -> str:
        """
        Load an image and encode it to base64
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Base64 encoded image string or None on error
        """
        try:
            # Validate file exists
            if not os.path.exists(image_path):
                print(f"❌ File not found: {image_path}")
                return None
            
            # Validate file format
            file_ext = Path(image_path).suffix.lower()
            if file_ext not in self.SUPPORTED_FORMATS:
                print(f"❌ Unsupported image format: {file_ext}")
                print(f"   Supported formats: {', '.join(self.SUPPORTED_FORMATS)}")
                return None
            
            # Check file size
            file_size_mb = os.path.getsize(image_path) / (1024 * 1024)
            if file_size_mb > self.MAX_SIZE_MB:
                print(f"❌ Image too large: {file_size_mb:.1f}MB (max {self.MAX_SIZE_MB}MB)")
                return None
            
            # Load and process image
            image = self._load_image(image_path)
            if image is None:
                return None
            
            # Optimize image
            image = self._optimize_image(image)
            
            # Encode to base64
            base64_string = self._encode_to_base64(image)
            
            print(f"✓ Image processed: {file_size_mb:.2f}MB")
            return base64_string
            
        except Exception as e:
            print(f"❌ Error processing image: {str(e)}")
            return None
    
    def _load_image(self, image_path: str) -> Image.Image:
        """
        Load image using PIL
        
        Args:
            image_path: Path to image file
            
        Returns:
            PIL Image object or None on error
        """
        try:
            image = Image.open(image_path)
            
            # Convert RGBA to RGB if necessary
            if image.mode in ('RGBA', 'LA', 'P'):
                rgb_image = Image.new('RGB', image.size, (255, 255, 255))
                rgb_image.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                image = rgb_image
            elif image.mode != 'RGB':
                image = image.convert('RGB')
            
            return image
            
        except Exception as e:
            print(f"❌ Error loading image: {str(e)}")
            return None
    
    def _optimize_image(self, image: Image.Image) -> Image.Image:
        """
        Optimize image size while maintaining quality
        
        Args:
            image: PIL Image object
            
        Returns:
            Optimized PIL Image object
        """
        try:
            # Resize if too large (maintain aspect ratio)
            max_dimension = 2000
            if image.width > max_dimension or image.height > max_dimension:
                image.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
                print(f"  Image resized to {image.width}x{image.height}")
            
            return image
            
        except Exception as e:
            print(f"⚠ Warning optimizing image: {str(e)}")
            return image
    
    def _encode_to_base64(self, image: Image.Image) -> str:
        """
        Encode PIL image to base64 string
        
        Args:
            image: PIL Image object
            
        Returns:
            Base64 encoded string
        """
        try:
            # Save to bytes buffer as JPEG (good compression)
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', quality=85, optimize=True)
            buffer.seek(0)
            
            # Encode to base64
            base64_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            return base64_string
            
        except Exception as e:
            print(f"❌ Error encoding image: {str(e)}")
            return None
