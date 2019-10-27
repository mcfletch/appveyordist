# Sample Test passing with nose and pytest
from appveyordist import appvapi

def test_list_pyopengl():
    found = 0
    for base,url in appvapi.latest_build_artifacts('MikeCFletcher','pyopengl'):
        found += 1
    assert found, "Live API test for PyOpenGL did not return any artifacts?"
