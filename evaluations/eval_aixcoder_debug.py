from mmengine.config import read_base

with read_base():
    from ..opencompass.configs.datasets.livecodebench.livecodebench_gen_aixcoder import \
        LCB_datasets

    from ..opencompass.configs.models.aixcoder.aixcoder_eval_debug import \
        models as aixcoder

datasets = LCB_datasets
models = aixcoder
