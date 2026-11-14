import json, glob, sys
bad = 0
for f in glob.glob('src/main/resources/assets/*/models/**/*.json', recursive=True):
    m = json.load(open(f, encoding='utf-8'))
    for i, e in enumerate(m.get('elements', [])):
        for k in ('from', 'to'):
            for v in e[k]:
                if v < -16 or v > 32:
                    print(f'ОШИБКА {f}: элемент {i}, {k} = {v} вне диапазона -16..32'); bad += 1
        for fn, fc in e.get('faces', {}).items():
            if 'uv' in fc and any(x < 0 or x > 16 for x in fc['uv']):
                print(f'ОШИБКА {f}: элемент {i}, грань {fn}, uv {fc["uv"]} вне 0..16'); bad += 1
print('Моделей с ошибками:', bad)
sys.exit(1 if bad else 0)
