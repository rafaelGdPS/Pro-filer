import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_all_diferent_file(tmp_path):
    file_1 = tmp_path / "file_1.txt"
    file_2 = tmp_path / "file_2.txt"
    file_1.write_text("Conteudo do arquivo diferente")
    file_2.write_text("Conteudo do arquivo mais diferente ainda")

    context = {
        "all_files": [
            f"{file_1}",
            f"{file_2}",
        ]
    }

    result = find_duplicate_files(context)

    assert result == []


def test_find_duplicate_files_duplicated(tmp_path):
    file_1 = tmp_path / "file_1.txt"
    file_2 = tmp_path / "file_2.txt"
    file_1.write_text("Conteudo do arquivo exatamente igual")
    file_2.write_text("Conteudo do arquivo exatamente igual")

    context = {
        "all_files": [
            f"{file_1}",
            f"{file_2}",
        ]
    }

    result = find_duplicate_files(context)

    assert result == [(f"{file_1}", f"{file_2}")]


def test_find_duplicate_valuerro(tmp_path):
    file_1 = tmp_path / "file_1.txt"
    file_2 = tmp_path / "file_2.txt"
    file_1.write_text("Conteudo do arquivo exatamente igual")
    file_2.write_text("Conteudo do arquivo exatamente igual")

    context = {
        "all_files": [
            f"{file_1}",
            f"{file_2}",
            "/home/trybe/Downloads/Trybe_logo.png",
        ]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
