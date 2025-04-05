class NamazNotOfferedError(Exception):
  pass

import cal
def test_main() -> int:
    response1:cal.add = cal.add(2, 3)
    assert response1 == 5, "Expected 2 + 3 to equal 5"
    response2:cal.add = cal.add(0, 0)
    assert response2 == 0, "Expected 0 + 0 to equal 0"
    response3:cal.add = cal.add(-2, -2)
    assert response3 == -4, "Expected -2 + -2 to equal -4"