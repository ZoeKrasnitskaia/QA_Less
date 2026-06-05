def test_list_numbers(practice):
    practice.list_numbers()


def test_list_words(practice, setup):
    practice.list_words()


def test_simulate_rostics_load(practice):
    practice.simulate_rostics_load()

def test_write_file(open_file):
    open_file.write("pipi")