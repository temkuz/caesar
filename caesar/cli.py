import argparse
from string import ascii_letters


def parse_args():
    default = argparse.ArgumentParser(
        description='Simple program for caesar cipher. For crypt data use key. For decrypt use negative key')
    default.add_argument('key', help='offset', type=int)
    default.add_argument('message', help='input message', nargs='*')
    return default.parse_args()


def make_cipher(key: int, message: list):
    message = ' '.join(message)
    tr = ascii_letters[key:] + ascii_letters[:key]
    tr = ''.maketrans(ascii_letters, tr)
    print(message.translate(tr))


def main():
    res = parse_args()
    make_cipher(res.key, res.message)


if __name__ == '__main__':
    main()
