Cache = __import__('exercise').Cache
# Create an instance of the Cache class
cache = Cache()

# Define the test cases
TEST_CASES = {
    b"foo": None,                          # bytes case, no conversion needed
    123: int,                              # int case, using int conversion
    "bar": lambda d: d.decode("utf-8")     # str case, using lambda to decode
}

# Iterate over the test cases
for value, fn in TEST_CASES.items():
    # Store the value in the cache and get the generated key
    key = cache.store(value)
    # Retrieve the value from the cache using the key and the specified conversion function
    retrieved_value = cache.get(key, fn=fn)
    # Assert that the retrieved value matches the original value
    assert retrieved_value == value, f"Test failed for value: {value} with function: {fn}"

print("All test cases passed!")
