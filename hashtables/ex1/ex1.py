def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Understand
    ## limit = Int
    ## weights = [Int]
    ## length = Int(of the weights count)

    # Plan
    ## We need to use a dictionary to store weights.

    weights_hash = {}

    for weight in range(len(weights)): # Looping through weights list count.
        weights_hash[weights[weight]] = weight # Setting the Key(Weights index) and Value(Weight Value)

    for index, weight in enumerate(weights_hash): # Iterating the Key:Value Pairs in Hash Table. Enumerate keeps count of iterations
        target_weight = limit - weight # Subtracting Limit value from weights list value literal.

        if target_weight in weights_hash: # Checking to see if target weight is in the hash
            i = weights_hash[target_weight] # Setting i to target_weight value
            return (index, i) if index > i else (i, index) # Returning the indices of the values that make up the weight. 


