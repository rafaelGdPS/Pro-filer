import os
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage(tmp_path, capsys, monkeypatch):
    file_1 = tmp_path / "test_1.txt"
    file_2 = tmp_path / "test_2.txt"
    file_1.write_text("r", encoding="utf-8")
    file_2.write_text("rafa", encoding="utf-8")

    context = {"all_files": [f"{file_1}", f"{file_2}"]}

    file_size_1 = os.path.getsize(file_1)
    file_size_2 = os.path.getsize(file_2)
    total_size = file_size_1 + file_size_2

    percentage_file_2 = int(file_size_2 / total_size * 100)
    percentage_file_1 = int(file_size_1 / total_size * 100)
    show_disk_usage(context)
    captured = capsys.readouterr()

    assert f"'{file_1}':".ljust(70), (
        f"{file_size_1} ({percentage_file_2}%)" in captured.out
    )
    assert captured.out.index(f"{percentage_file_2}") < captured.out.index(
        f"{percentage_file_1}"
    )
    assert f"'{file_2}':".ljust(70), f"{file_size_2} (20%)" in captured.out
    assert f"Total size: {total_size}" in captured.out


def test_show_disk_usage_with_all_files_empty(capsys):
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()
    assert "Total size: 0" in captured.out
