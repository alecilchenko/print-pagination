def print_pagination(current_page, total_pages, boundaries, around):
    # Check exceptions
    ## Is any input parametrs negative or incorrect?

    if current_page < 1:
        print('Current page should be at least 1 or bigger')
        return

    if total_pages < 1:
        print('Total page should be at least 1 or bigger')
        return

    elif current_page > total_pages:
        print('Current page cannot be bigget than total')
        return
    
    ## Is boundaries negative or have incorrect value?
    if boundaries < 0:
        print('Boundaries cannot be negative')
        return
    elif boundaries > total_pages/2:
        print('Boundaries cannot be more than half of total')
        return
    
    ## Is around negative or have incorrect value?
    if around < 0:
        print('Around cannot be negative')
        return
    elif around > total_pages/2:
        print('Around cannot be more than half of total')
        return
    
    # Handle edge cases, whene around and boundaries equil zero
    if current_page==total_pages and (around, boundaries) == (0,0):
        print(current_page)
        return
    
    pages_to_link = []
    count = 1 # Count was implemented to check all possible conditions of each pages 

    # Add start boundaries
    for i in range(1, boundaries+1):
        pages_to_link.append(i)
        count += 1

    # Add hide link if count is outside range of current page BEFORE
    if count < current_page - around:
        pages_to_link.append('...')  

    # Check that count not inside current page range and initionalize as a first page of range
    if count not in range(current_page-around, current_page+around+1):
        count = current_page-around
    
    # Add current page with his range and check that it isn't more than total or not in start boundaries
    for i in range(count, current_page+around+1):
        if i < total_pages and i not in range(1, boundaries+1):
            pages_to_link.append(i)
            count += 1
    
    # Add hide link if count is outside of current page range but don't achive boundaries
    if count > current_page+around and count < total_pages-boundaries+1:
        pages_to_link.append('...')
    
    # Check that count not in end boundaries range and initionalize as a first page of range
    if count not in range(total_pages-boundaries+1, total_pages+1):
        count = total_pages-boundaries+1

    # Add end boudaries
    for i in range(count, total_pages+1):
        pages_to_link.append(i)
    
    # Print the pagination
    print(' '.join([str(page) for page in pages_to_link]))

if __name__ == '__main__':
    # Example usage
    print_pagination(1, 10, 2, 2)
    print_pagination(5, 10, 2, 2)
    print_pagination(8, 10, 2, 2)
    print_pagination(10, 10, 2, 2)
    print_pagination(1, 10, 5, 5)
    print_pagination(100, 101, 3, 1)
    print_pagination(39, 333, 3, 3)
    print_pagination(10, 10, 0, 0)
    print_pagination(1, 1, 0, 1)
    print_pagination(9, 10, 1, 1)
