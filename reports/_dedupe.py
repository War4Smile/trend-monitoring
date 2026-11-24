import json, re, os

path = r'H:\soft\hermesapp\notes\briefing_history.json'
raw = open(path, encoding='utf-8').read()
d = json.loads(raw)

def strip(x):
    x = re.sub(r'\s+', ' ', x)
    return x

print('loaded items:', len(d))
for i, x in enumerate(d):
    print(i+1, repr(x[:90]))
