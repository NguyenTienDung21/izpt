import pytest
import numpy as np

@pytest.fixture
def sample_rect():
    return  [300, 300, 800, 800 ]

@pytest.fixture
def sample_rect_vertical():
    return [450,200, 550,900 ]


@pytest.fixture
def sample_rect_horizontal():
    return [200, 450, 900, 550]


@pytest.fixture()
def blank_image():
    blank_image = 255 * np.ones(shape=[1024, 1024, 3], dtype=np.uint8)
    return blank_image


