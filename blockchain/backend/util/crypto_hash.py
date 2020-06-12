import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    stringified_args = sorted(
        map(json.dumps, args)
    )  # make any type to string to encode
    # print(f'stringified_args: {stringified_args}')
    joined_args = "".join(stringified_args)
    # print(f'joined_args: {joined_args}')

    return hashlib.sha256(joined_args.encode("utf-8")).hexdigest()


def main():
    print(
        f"crypto_hash('one', 'two', 'three', 4, [5]): {crypto_hash('one', 'two', 'three', 4, [5])}"
    )
    print(
        f"crypto_hash([5], 'one', 'two', 'three', 4): {crypto_hash([5], 'one', 'two', 'three', 4)}"
    )


if __name__ == "__main__":
    main()
