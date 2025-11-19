"""Command-line interface for favicon-generator."""

import sys
from pathlib import Path
import click
from .converter import convert_to_ico


@click.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option(
    '-o', '--output',
    type=click.Path(dir_okay=False, writable=True),
    help='Output .ico filename (default: input name with .ico extension)'
)
@click.option(
    '-c', '--crop',
    is_flag=True,
    help='Crop image to square before processing'
)
@click.version_option()
def main(input_file, output, crop):
    """
    Convert an image (JPEG, PNG, or WEBP) to .ico favicon format.
    
    INPUT_FILE: Path to the image file to convert
    
    Examples:
    
        favicon-generator image.png
        
        favicon-generator image.jpg -o my-favicon.ico
        
        favicon-generator image.webp --crop -o favicon.ico
    """
    try:
        input_path = Path(input_file)
        
        # Determine output path
        if output:
            output_path = Path(output)
        else:
            # Use input filename with .ico extension
            output_path = input_path.with_suffix('.ico')
        
        # Convert the image
        click.echo(f"Converting {input_path} to {output_path}...")
        if crop:
            click.echo("Cropping to square...")
        
        convert_to_ico(input_path, output_path, crop_square=crop)
        
        click.echo(f"✓ Successfully created {output_path}")
        
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: An unexpected error occurred: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
