import pytest


def test_smoke_import():
    import solution  # noqa: F401


@pytest.mark.skip(reason='Template baseline aguardando solucao real')
def test_placeholder():
    assert True