import pytest


@pytest.mark.slow
def test_classify():
    from domain.image_classification.resnet50 import classify
    image_path = "tests/assets/Banana.jpg"

    result = classify(image_path)

    assert result == "banana"
