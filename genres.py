from random import choice
from pathlib import Path


def load_wordlist(filename: str) -> [str]:
    filepath = Path(__file__).parent.joinpath("wordlists").joinpath(filename)
    with open(filepath) as word_file:
        lines = [line for line in word_file.read().split("\n") if len(line) > 0]
        print(f"Loaded {len(lines)} terms from {filename}")
        return lines


def random_genre() -> str:
    return f"{choice(origins)} {choice(descriptors)}-{choice(descriptors)} {choice(descriptors)}"


origins = load_wordlist("origins.txt")
descriptors = load_wordlist("descriptors.txt")

if __name__ == "__main__":
    for i in range(100):
        print(random_genre())
