import math


def cosine_similarity(a_keys, a_values, b_keys, b_values):
    # Create dictionaries from the keys and values
    a_dict = dict(zip(a_keys, a_values))
    b_dict = dict(zip(b_keys, b_values))

    # Find the common keys between the two dictionaries
    common_keys = set(a_keys) & set(b_keys)

    # Calculate dot product
    dot_product = sum(a_dict[key] * b_dict[key] for key in common_keys)

    # Calculate magnitudes
    a_magnitude = math.sqrt(sum(a_dict[key] ** 2 for key in a_keys))
    b_magnitude = math.sqrt(sum(b_dict[key] ** 2 for key in b_keys))

    # Check for the case where one of the magnitudes is zero
    if a_magnitude == 0 or b_magnitude == 0:
        return 0.0

    # Calculate and return cosine similarity
    cosine_similarity = dot_product / (a_magnitude * b_magnitude)
    return cosine_similarity
