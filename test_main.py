import pytest
from main import main


def run_and_capture(capsys, argv):
    code = main(argv)
    out = capsys.readouterr()
    return code, out.out.strip(), out.err.strip()


def test_enteros(capsys):
    code, out, err = run_and_capture(capsys, ["-n", "1", "2", "3", "4"])
    assert code == 0
    assert err == ""
    assert float(out) == 10.0


def test_flotantes(capsys):
    code, out, err = run_and_capture(capsys, ["-n", "0.5", "1.25"])
    assert code == 0
    assert err == ""
    assert float(out) == 1.75


def test_un_solo_numero(capsys):
    code, out, err = run_and_capture(capsys, ["-n", "5"])
    assert code == 0
    assert err == ""
    assert float(out) == 5.0


def test_negativos(capsys):
    code, out, err = run_and_capture(capsys, ["-n", "5", "-2", "-3"])
    assert code == 0
    assert err == ""
    assert float(out) == 0.0


def test_notacion_cientifica(capsys):
    code, out, err = run_and_capture(capsys, ["-n", "1e-3", "2e-3"])
    assert code == 0
    assert err == ""
    assert abs(float(out) - 0.003) < 1e-12



@pytest.mark.parametrize(
    "bad",
    [["1", "a", "3"], ["0x10", "2"], ["NaN", "2"], ["inf", "2"]],
)
def test_invalidos(capsys, bad):
    code, out, err = run_and_capture(capsys, ["-n"] + bad)
    assert code != 0
    assert out == ""
    assert "Solo se aceptan enteros y flotantes." in err



