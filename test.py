def split(start_month: int, start_year: int, end_month: int, end_year: int, number_splits: int) -> list:
    current_month, current_year = start_month, start_year
    month_diff = None
    if start_year == end_year:
        month_diff = end_month - start_month
    else:
        month_diff = (12 - start_month) + end_month + ((end_year - start_year - 1) * 12)
    split = month_diff // number_splits
    if month_diff % number_splits != 0:
        split += 1
    intervals = []
    for i in range(month_diff):
        if i % split == 0:
            intervals.append(list())
        intervals[-1].append((current_month, current_year))
        current_month += 1
        if current_month == 13:
            current_month = 1
            current_year += 1
    for index, interval in enumerate(intervals):
        print(index + 1, ': ', interval)
    return intervals

split(3, 2018, 2, 2024, 7)
split(3, 2018, 5, 2020, 4)
