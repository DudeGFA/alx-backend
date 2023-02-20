#!/usr/bin/env python3
"""
    contains function index_range
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
        Args:
            page: int
            page_size: int (size of each page)
        Returns: tuple of size two containing a start index
            and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return tuple([start_index, end_index])
