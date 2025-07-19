# Generative Fusion Decoding

This feature implements the core algorithm that fuses outputs from a Whisper ASR model with a large language model (LLM) during decoding. The `Breezper` class in `gfd/gfd.py` orchestrates this process.

## How It Works
1. Load Whisper ASR and LLM models.
2. Prepare prompts and tokenizers for both models.
3. Perform chunked audio transcription and iterate with beam search.
4. At each step, combine ASR and LLM log probabilities using a configurable weight (`fusing_r`).
5. Keep track of beams via `BeamsControler` and terminate when conditions meet.

## Key Files
- `gfd/gfd.py` – defines `Breezper` with ASR/LLM fusion logic.
- `gfd/beam.py` – `BeamsControler` manages beam states and scoring.
- `gfd/model.py` – provides LLM log probability utilities used by the decoder.
- `gfd/tokenizer.py` – tokenizers that bridge byte sequences.

