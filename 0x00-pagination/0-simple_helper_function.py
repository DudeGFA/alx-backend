#!/usr/bin/env python3
"""
    contains function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Args:
            page: int
            page_size: int (size of each page)
        Returns: tuple of size two containing a start index
            and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
