def print_pagination(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> None:
    check_errors = {
        "Current page should be at least 1 or bigger.":
            current_page >= 1,
        "Total page should be at least 1 or bigger.":
            total_pages >= 1,
        "Current page cannot be bigger than total.":
            current_page <= total_pages,
        "Boundaries cannot be negative.":
            boundaries >= 0,
        "Around cannot be negative.":
            around >= 0,
    }
    if False in check_errors.values():
        error_message = ""
        for error, pass_status in check_errors.items():
            if not pass_status:
                error_message += error + "\n"
        raise ValueError(error_message)

    start = {
        page for page in range(1, boundaries + 1)
        if page <= total_pages
    }
    middle = {
        page
        for page in range(current_page - around, current_page + around + 1)
        if 0 < page <= total_pages
    }
    end = {
        page
        for page in range(total_pages - boundaries + 1, total_pages + 1)
        if 0 < page <= total_pages
    }
    result = start.union(middle, end)
    result = list(result)
    all_pages = [page for page in range(1, total_pages + 1)]
    flag = True
    count = 0
    for number in all_pages:
        if number not in result and flag:
            result.insert(count, "...")
            flag = False
            count += 1
        if number in result:
            flag = True
            count += 1
    for i in result:
        print(i, end=" ")
    print()
