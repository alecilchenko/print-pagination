def print_pagination(current_page, total_pages, boundaries, around):
    # Check exceptions

    # Is current_page/total_pages negative or incorrect?
    if current_page < 1:
        raise ValueError('Current page should be at least 1 or bigger')

    if total_pages < 1:
        raise ValueError('Total page should be at least 1 or bigger')
    elif current_page > total_pages:
        raise ValueError('Current page cannot be bigger than total')

    # Is boundaries negative or around have negative value?
    if boundaries < 0:
        raise ValueError('Boundaries cannot be negative')
    elif around < 0:
        raise ValueError('Around cannot be negative')

    # Handle edge cases
    # When around or boundaries more than half of total
    if around >= total_pages/2 or boundaries >= total_pages/2:
        for page in range(1, total_pages+1):
            print(page, end=' ')
        print()
        return

    pages_to_link = []
    marker = 1
    # marker was implemented to check all possible conditions of each pages
    current_min = current_page - around
    current_max = current_page + around
    start_boundaries_max = boundaries
    end_boudaries_min = total_pages - boundaries + 1

    # Add start boundaries
    while 1 <= marker <= start_boundaries_max:
        pages_to_link.append(marker)
        marker += 1

    # Add hide links if marker is outside range of current page BEFORE
    if marker < current_min:
        pages_to_link.append('...')

    # Check that marker not inside current page range
    # and initialization as a first page of range
    if end_boudaries_min < current_min:
        marker = end_boudaries_min
    elif (not current_min <= marker <= current_page) and marker < current_min:
        marker = current_min

    # Add current page with his range
    # and check that it isn't more than total pages
    while marker <= current_max and marker <= total_pages:
        pages_to_link.append(marker)
        marker += 1

    # Add hide link if marker is outside of current
    # page range but don't achieve boundaries
    if (not current_page <= marker <= current_max) and (current_max < marker < end_boudaries_min):
        pages_to_link.append('...')

    # Check that marker not in end boundaries range
    # and initialization as a first page of range
    if (not end_boudaries_min <= marker <= total_pages) and marker < end_boudaries_min:
        marker = end_boudaries_min

    # Add end boundaries
    while marker <= total_pages:
        pages_to_link.append(marker)
        marker += 1

    # Print the pagination
    print(' '.join([str(page) for page in pages_to_link]))


if __name__ == '__main__':
    # Example usage
    '''
    print_pagination(4, 5, 1, 0)
    print_pagination(4, 10, 2, 2)
    print_pagination(8, 10, 2, 2)
    print_pagination(10, 10, 2, 2)
    print_pagination(1, 10, 5, 5)
    print_pagination(100, 101, 3, 1)
    print_pagination(39, 333, 3, 3)
    print_pagination(10, 10, 0, 0)
    print_pagination(1, 1, 0, 1)
    print_pagination(9, 10, 1, 1)
    print()
    print_pagination(5, 10, 1, 11)
    print_pagination(5, 10, 11, 1)
    print_pagination(1, 10, 3, 1)
    print_pagination(9, 10, 0, 1)
    '''
    print_pagination(9, 10, 4, 1)
    # print_pagination(9, 10, -2, 1)
