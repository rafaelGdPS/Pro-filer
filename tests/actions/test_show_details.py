from pro_filer.actions.main_actions import show_details  # NOQA


from datetime import date


# from unittest.mock import patch


def test_show_details(capsys):

    context = {"base_path": "images/pro-filer-preview.gif"}
    show_details(context)
    captured = capsys.readouterr()
    assert "File name: pro-filer-preview.gif" in captured.out
    assert "File size in bytes: 270824" in captured.out
    assert "File type: file" in captured.out
    assert "File extension: .gif" in captured.out
    assert "Last modified date: 2024-06-06" in captured.out


def test_show_details_without_path_existent(capsys):
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}
    show_details(context)
    captured = capsys.readouterr()
    assert "File 'Trybe_logo.png' does not exist" in captured.out


def test_show_details_without_extension(capsys):
    context = {
        "base_path": "tests/actions/Diretorio_test/arquivo_sem_extensão"
    }

    show_details(context)
    captured = capsys.readouterr()
    assert "File extension: [no extension]" in captured.out


def test_show_details_date_format_is_wrong(capsys):
    context = {"base_path": "images/pro-filer-preview.gif"}

    show_details(context)
    captured = capsys.readouterr()
    assert f"Last modified date: {date.today()}\n" in captured.out
