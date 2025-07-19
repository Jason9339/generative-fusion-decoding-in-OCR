# Configuration System

Model and prompt settings are stored as YAML files under `config_files/`. `gfd/utils.py` loads these files and allows command line arguments to override values.

## How It Works
- `process_config` reads a YAML file and merges command-line arguments.
- `combine_config` merges prompt and model configurations for convenience.
- Benchmark scripts select the desired YAML files based on the dataset and model.

## Key Files
- `config_files/model/*.yaml` – model settings (paths, fusion weights, decoding options).
- `config_files/prompt/*.yaml` – example prompt texts for ASR and LLM.
- `gfd/utils.py` – helper functions to load and combine configs.
