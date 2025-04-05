import cal
def main() -> int:
    response:cal.add = cal.add(2, 3)
    assert response == 4, "Expected 2 + 3 to equal 5"
    return response

if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")