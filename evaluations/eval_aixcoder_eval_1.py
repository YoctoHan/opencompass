from mmengine.config import read_base

with read_base():
    from ..opencompass.configs.datasets.gsm8k.gsm8k_gen_aixcoder import \
        gsm8k_datasets
    from ..opencompass.configs.datasets.math.math_0shot_gen_aixcoder import \
        math_datasets
    # from ..opencompass.configs.datasets.mmlu.mmlu_gen_aixcoder import \
    #     mmlu_datasets
    # from ..opencompass.configs.datasets.ceval.ceval_gen_aixcoder import \
    #     ceval_datasets

    from ..opencompass.configs.models.aixcoder.aixcoder_eval_1 import \
        models as aixcoder

# datasets = gsm8k_datasets + math_datasets + mmlu_datasets + ceval_datasets
datasets = gsm8k_datasets + math_datasets
models = aixcoder
