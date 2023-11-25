import re

def main(input_str_num: int, input_str: str) -> int:
    pattern = re.compile(r"(.)\1*")
    split_alphabet = sorted([match.group() for match in pattern.finditer(input_str)], key=len)[::-1]
    no_duplicates = []
    added_str = []
    
    for s in split_alphabet:
        if s[0] not in added_str:
            added_str.append(s[0])
            no_duplicates.append(s)
    return sum([len(s) for s in no_duplicates])
    
if __name__ == "__main__":
    N = int(input())
    S = str(input())
    print(main(N, S))
