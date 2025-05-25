from mmengine.config import read_base

with read_base():
    from ..opencompass.configs.datasets.demo.demo_gsm8k_base_gen import \
        gsm8k_datasets
    from ..opencompass.configs.datasets.demo.demo_math_base_gen import \
        math_datasets

    from ..opencompass.configs.models.aixcoder.aixcoder_eval_debug import \
        models as aixcoder

datasets = gsm8k_datasets + math_datasets
models = aixcoder
