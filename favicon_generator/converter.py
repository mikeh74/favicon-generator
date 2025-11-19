"""Core image processing module for converting images to .ico format."""

from pathlib import Path
from typing import Union
from PIL import Image


def crop_to_square(image: Image.Image) -> Image.Image:
    """
    Crop an image to a square by taking the center portion.
    
    Args:
        image: PIL Image object to crop
        
    Returns:
        Cropped square PIL Image object
    """
    width, height = image.size
    
    if width == height:
        return image
    
    # Determine the size of the square (smallest dimension)
    size = min(width, height)
    
    # Calculate crop coordinates for center crop
    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size
    
    return image.crop((left, top, right, bottom))


def convert_to_ico(
    input_path: Union[str, Path],
    output_path: Union[str, Path],
    crop_square: bool = False
) -> None:
    """
    Convert an image (JPEG, PNG, or WEBP) to .ico format.
    
    Args:
        input_path: Path to the input image file
        output_path: Path where the .ico file will be saved
        crop_square: If True, crop the image to a square before conversion
        
    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If image format is not supported
        IOError: If there's an error reading or writing files
    """
    input_path = Path(input_path)
    output_path = Path(output_path)
    
    # Validate input file exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate input file format
    supported_formats = {'.jpg', '.jpeg', '.png', '.webp'}
    if input_path.suffix.lower() not in supported_formats:
        raise ValueError(
            f"Unsupported file format: {input_path.suffix}. "
            f"Supported formats: {', '.join(supported_formats)}"
        )
    
    # Ensure output has .ico extension
    if output_path.suffix.lower() != '.ico':
        output_path = output_path.with_suffix('.ico')
    
    # Open and process the image
    with Image.open(input_path) as img:
        # Convert to RGB if necessary (ICO format requires RGB)
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGBA')
        
        # Crop to square if requested
        if crop_square:
            img = crop_to_square(img)
        
        # Save as .ico with multiple sizes for better compatibility
        # Common favicon sizes: 16x16, 32x32, 48x48, 64x64, 128x128, 256x256
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(output_path, format='ICO', sizes=sizes)
