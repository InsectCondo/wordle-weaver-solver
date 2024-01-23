def EditDistance(w1: str, w2: str) -> int:
    return abs(len(w1) - len(w2)) + sum([c1 != c2 for c1, c2 in zip(w1, w2)])


def EditDistanceOne(w1: str, w2: str) -> bool:
    """returns whether or not two words have exactly one character different"""
    differing = False
    for c1, c2 in zip(w1, w2):
        if c1 == c2: continue
        if differing: return False
        if not differing: differing = True
    return differing


def SolveWeaverWordle(word1: str, word2: str,
                      dictionary: list[str]) -> tuple[str]:
    lastlevel_1 = {(word1.lower(), )}
    lastlevel_2 = {(word2.lower(), )}
    while True:
        thislevel_1 = set()
        for last_path_1 in lastlevel_1:
            for tryword in dictionary:
                #go to next word if repeated or invalid
                if tryword in last_path_1: continue
                if not EditDistanceOne(last_path_1[-1], tryword): continue
                #return if solution
                if solution := {
                        last_path_1 + path
                        for path in lastlevel_2 if tryword in path
                }:
                    return tuple(solution)[0]
                thislevel_1.add(last_path_1 + (tryword, ))
        lastlevel_1 = thislevel_1

        #same from the other end
        thislevel_2 = set()
        for last_path_2 in lastlevel_2:
            for tryword in dictionary:
                if tryword in last_path_2: continue
                if not EditDistanceOne(last_path_2[0], tryword): continue
                if solution := {
                        path + last_path_2
                        for path in lastlevel_1 if tryword in path
                }:
                    return tuple(solution)[0]
                thislevel_2.add((tryword, ) + last_path_2)
        lastlevel_2 = thislevel_2


if __name__ == "__main__":
    word1 = "word"
    word2 = "game"

    from os.path import dirname
    DIR = dirname(__file__)
    with open(f'{DIR}/dict_4.txt', 'r') as file:
        dictionary = file.read().split("\n")
    print(f"finding a path between {word1.upper()} and {word2.upper()}...")
    solution = SolveWeaverWordle(word1, word2, dictionary)
    print(solution)
