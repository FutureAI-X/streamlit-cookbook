import time
import random

def response_generator():
    random_one = random.choice(
        [
            "你好，我可以帮你做什么？",
            "遇见你真高兴！",
            "今天天气真不错！",
        ]
    )
    for word in random_one:
        yield word + ""
        time.sleep(0.1)

for response in response_generator():
    print(response, end='', flush=True)