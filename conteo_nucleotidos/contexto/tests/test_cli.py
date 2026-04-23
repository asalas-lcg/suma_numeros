import subprocess, sys

def run(args):
    return subprocess.run(
        [sys.executable,"src/kmer_cli.py"]+args,
        capture_output=True,
        text=True
    )

def test_valid_with_N():
    r = run(["--sequence","ATNCG","--k","3"])
    assert r.returncode == 0
    assert "ATN" in r.stdout
    assert "TNC" in r.stdout
    assert "NCG" in r.stdout

def test_invalid_char():
    r = run(["--sequence","ATBX","--k","2"])
    assert r.returncode != 0
