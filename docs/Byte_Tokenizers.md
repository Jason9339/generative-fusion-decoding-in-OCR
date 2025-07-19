# Byte Tokenizers

Custom tokenizers bridge byte sequences and model vocabularies. They allow the ASR and LLM models to operate in a unified byte token space.

## Components
- **`LlamaByteTokenizer`** – extends `LlamaTokenizerFast` to convert between bytes and Llama tokens. Handles special byte tokens and allows lookup of tokens by byte prefix.
- **`WhisperByteTokenizer`** – wraps Whisper's tokenizer to convert IDs back to raw bytes.

## Key Files
- `gfd/tokenizer.py` – implementations of `ByteTokenizer`, `LlamaByteTokenizer`, and `WhisperByteTokenizer`.
