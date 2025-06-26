import argparse
import json
import os

from gfd.gfd_ocr import BreezperOCR
from gfd.utils import process_config


def parse_args():
    parser = argparse.ArgumentParser(description="Run GFD OCR on a single image.")
    parser.add_argument('--image_file_path', type=str, required=True, help='Path to the image file')

    default_config = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'config_files', 'model', 'gfd-ocr-en.yaml'
    )
    parser.add_argument('--config', type=str, default=default_config, help='Path to config YAML')
    parser.add_argument(
        '--result_output_path',
        type=str,
        required=True,
        help='Path to save result JSON'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    config = process_config(args.config)
    model = BreezperOCR(config)
    result = model.get_transcription(args.image_file_path)
    print(f'Result: {result}')
    with open(args.result_output_path, 'w') as f:
        json.dump(result, f, ensure_ascii=False)


if __name__ == '__main__':
    main()

