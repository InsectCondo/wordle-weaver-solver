from os.path import dirname

INDIR = dirname(__file__)
OUTDIR = dirname(INDIR)

with open(f'{INDIR}/dict_full.txt', 'r') as file:
    oldwords = file.read().split('\n')

with open(f'{OUTDIR}/weaver_dict.txt', 'w') as file:
    file.write("")
with open(f'{OUTDIR}/weaver_dict.txt', 'a') as file:
    newcount = 0
    for word in oldwords:
        if len(word) != 4: continue
        if not word.isalpha(): continue
        file.write(f"{word}\n")
        newcount += 1
print(f"reduced dictionary from {len(oldwords)} to {newcount}")
