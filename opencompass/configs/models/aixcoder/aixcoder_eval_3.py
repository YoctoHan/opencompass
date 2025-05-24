from opencompass.models import OpenAISDK

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        abbr='Qwen3-32B',
        type=OpenAISDK,
        key='token-test-jsy', # API key
        openai_api_base='http://10.103.255.11:51103/v1', # 服务地址
        path='Qwen3-32B-AWQ-KVQ', # 请求服务时的 model name
        tokenizer_path='/Qwen3-32B', # 请求服务时的 tokenizer name 或 path, 为None时使用默认tokenizer gpt-4
        rpm_verbose=True, # 是否打印请求速率
        meta_template=api_meta_template, # 服务请求模板
        query_per_second=1, # 服务请求速率
        max_out_len=38912, # 最大输出长度
        max_seq_len=40960, # 最大输入长度
        batch_size=1, # 批处理大小
        retry=100, # 重试次数
    )
]