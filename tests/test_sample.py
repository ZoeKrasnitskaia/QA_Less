import pytest


@pytest.mark.parametrize(
    "start, end, limit",
    [
        (1, 8, 6),
        (1, 9, 8),
        (1, 10, 9)
    ]
)

def test_list_numbers(practice, start, end, limit):
    practice.list_numbers(start, end, limit)

@pytest.mark.smoke
def test_list_words(practice, setup):
    practice.list_words()

@pytest.mark.xfail(reason = "Roctics not work today")
def test_simulate_rostics_load(practice):
    practice.simulate_rostics_load()

@pytest.mark.skip(reason = "Feature is not implemented")
def test_write_file(open_file):
    open_file.write("pipi")
