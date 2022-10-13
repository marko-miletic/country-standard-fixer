from import_files import get_filenames

def test_get_filenames():
    assert get_filenames() == ["test2", "test1", "test3"]