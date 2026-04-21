import subprocess, sys

def run(args):
    return subprocess.run([sys.executable,"src/kmer_cli.py"]+args,capture_output=True,text=True)

def test_ok():
    r=run(["--sequence","ATGCG","--k","3"])
    assert r.returncode==0
    assert "ATG" in r.stdout

def test_fail():
    r=run(["--sequence","ATBX","--k","2"])
    assert r.returncode!=0
