# BreezeByte Model

`BreezeByte` in `gfd/model.py` wraps an auto-regressive LLM so that its token space can be queried using byte tokens. It also implements a KV cache for efficient incremental inference.

## How It Works
- Converts byte sequences to LLM tokens using `LlamaByteTokenizer`.
- Computes log probabilities over alternative byte continuations via `_get_logprob`.
- Provides `get_logprob`, `get_logprob_cache_static`, and `get_logprob_cache_dynamic` to fetch log probabilities with or without cache reuse.
- Maintains a `KVCache` to store past key values and logits and prunes unused entries.

## Key Files
- `gfd/model.py` – implementation of `KVCache`, `ByteModel`, and `BreezeByte`.
- `gfd/tokenizer.py` – tokenizers used by the model.
