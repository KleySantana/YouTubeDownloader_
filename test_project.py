import pytest
from project import processing, get_resolution, download, ask_res
from unittest.mock import patch

# Testing preparation. The fixtures are necessary to pass the variables as parameters to the functions.

@pytest.fixture
def link():
    # Provide the URL of a YouTube video for testing
    return "https://www.youtube.com/watch?v=XYtyeqVQnRI"


@pytest.fixture
def resolutions(link):
    # Process the link to obtain resolutions for testing
    _, resolutions = processing(link)
    return resolutions


@pytest.fixture
def chosen():
    return [135, '480p', 7.5]


def test_processing():
    with pytest.raises(ValueError):
        assert processing("https://youtube.com/watch?v=")
    assert len(processing("https://youtube.com/watch?v=lOKASgtr6kU")) == 2


def test_get_resolution(resolutions):
    with patch('project.ask_res') as mock_function:
        mock_function.return_value = '5'
        expected_result = [135, '480p', 7.5]
        assert get_resolution(resolutions) == expected_result


def test_download(link, chosen):
    assert download(link, chosen) == True
