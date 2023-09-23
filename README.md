# phi-test-IAYN

Inspired by the recent work of Pretraining On Test Data Is All You Need

* Forked from [Modal Lab's Llama-finetuning](https://github.com/modal-labs/llama-finetuning)

### Getting Started

We could not install [llama-recipes](https://github.com/facebookresearch/llama-recipes) via poetry, so we had to install it using pip.



```bash
modal run train.py --dataset sql_dataset.py --base code7 --run-id chat7-sql

```

### Data Source
- [HumanEval](https://github.com/openai/human-eval)
- [MBPP - Mostly Basic Python Problems Dataset](shttps://github.com/google-research/google-research/tree/master/mbpp)

### References
- [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644)
- [Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463)
