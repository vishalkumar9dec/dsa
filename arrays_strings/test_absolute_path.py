import pytest

from absolute_path import get_absolute_path


def test_trailing_slash_removed():
    assert get_absolute_path("/home/") == "/home"


def test_no_trailing_slash():
    assert get_absolute_path("/home") == "/home"


def test_root():
    assert get_absolute_path("/") == "/"


def test_multiple_consecutive_slashes():
    assert get_absolute_path("/home//foo/") == "/home/foo"
    assert get_absolute_path("///a///b///") == "/a/b"


def test_current_directory_ignored():
    assert get_absolute_path("/a/./b/./c") == "/a/b/c"


def test_parent_directory():
    assert get_absolute_path("/home/user/../docs") == "/home/docs"


def test_parent_of_root_stays_root():
    assert get_absolute_path("/..") == "/"
    assert get_absolute_path("/../../a") == "/a"


def test_goes_up_to_root():
    assert get_absolute_path("/a/b/../..") == "/"


def test_triple_and_quad_periods_are_names():
    assert get_absolute_path("/.../a") == "/.../a"
    assert get_absolute_path("/..../a/..") == "/...."


def test_mixed():
    assert get_absolute_path("/a/./b/../../c/") == "/c"


@pytest.mark.parametrize(
    "path, expected",
    [
        ("/a//b////c/d//././/..", "/a/b/c"),
        ("/home/../../..", "/"),
        ("/.hidden/file.txt", "/.hidden/file.txt"),
    ],
)
def test_parametrized(path, expected):
    assert get_absolute_path(path) == expected
