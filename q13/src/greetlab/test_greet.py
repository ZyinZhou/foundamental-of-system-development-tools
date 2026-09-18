import sys

import pytest

from greetlab.cli import main


def test_normal_name(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "Alice"])
    main()
    out, _ = capsys.readouterr()
    assert out.strip() == "Hello, Alice!"


def test_name_all_whitespace(monkeypatch):
    """name全部为空白字符，应当抛出SystemExit(2)"""
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
