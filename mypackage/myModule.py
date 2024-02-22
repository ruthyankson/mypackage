def top_n (items, n):
    # Doctsring
    """Return the top n items in an array in descending order.

    Args:
        items (array): list or array-like object
        n (int): num of items to return

    Return:
        array: top n items, in desc order

    Egs: Input top_n([4,5,3,8,4], 2)
         Output - [8,5]
    """

    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: # if this item is bigger than next item...
                items[j], items[j+1] = items[j+1], items[j] # swap the two

    # get last n items
    top_items = items[-n:]

    # return in descending order
    return top_items[::-1]
