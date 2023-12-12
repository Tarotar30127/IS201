from byu_pytest_utils import max_score, this_folder, run_python_script
import string


@max_score(10)
def test_build():
    cipher_file = this_folder / "cipher.observed.csv"
    cipher_file.unlink(missing_ok=True)
    run_python_script("build_cipher.py", cipher_file)

    sources = []
    targets = []
    with open(cipher_file) as file:
        for line in file:
            s, t = line.strip().split(',')
            sources.append(s)
            targets.append(t)

    for c in string.ascii_lowercase:
        if c not in sources:
            raise Exception(f'"{c}" not found as key in cipher')

    for c in string.ascii_lowercase:
        if c not in targets:
            raise Exception(f'"{c}" not found as value in cipher')
