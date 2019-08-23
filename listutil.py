import unittest


def unique(list):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ["b","a"]
    >>> unique([])
    []
    >>> unique(['a', 'b', 'c', 'd', 'd', 'e', 'e'])
    ['a', 'b', 'c', 'd', 'e']
    >>> unique(['Hello','Bye','Bye','Hello','Ok','Ok'])
    ['Hello','Bye','Ok']
    >>> unique([ 1, 2, 3,[ 7, 8, 9]])
    [ 1, 2, 3, [7, 8, 9]]
    >>> unique ([ 1, 1, 1, 1, 1, 1])
    [1]
    """
    result_list = []
    for item in list:
        # if i not in result_listist append(add) it in list
        if item not in result_list:
            result_list.append(item)  # if i in list do noting
    return result_list


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
