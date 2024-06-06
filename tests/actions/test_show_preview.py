from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 3 files and 2 directories" in captured.out
    assert "First 5 directories: ['src', 'src/utils']" in captured.out


def test_show_preview_empty_dir(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 0 files and 0 directories" in captured.out


def test_show_preview_with_limit_5_items(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/dat/models/models.py",
            "src/ser/services.py",
            "src/type/types.py",
            "src/__main__.py",
        ],
        "all_dirs": [
            "src",
            "src/utils",
            "src/type",
            "src/ser",
            "src/dat",
            "src/dat/models/",
        ],
    }
    show_preview(context)
    captured = capsys.readouterr()
    file_5 = "['src', 'src/utils', 'src/type', 'src/ser', 'src/dat']\n"
    assert "Found 7 files and 6 directories" in captured.out
    assert f"First 5 directories: {file_5}" in captured.out
