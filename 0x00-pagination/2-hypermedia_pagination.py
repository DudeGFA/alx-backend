#!/usr/bin/env python3
"""
    contains function index_range
"""
import csv
from typing import List, Tuple
from math import ceil


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            returns a page of size page_size
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        idx_range = index_range(page, page_size)
        self.dataset()
        try:
            return(self.__dataset[idx_range[0]: idx_range[1]])
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            takes the same arguments (and defaults) as get_page and returns
            a dictionary containing the following key-value pairs:
                page_size: the length of the returned page
                page: the current page number
                data: the dataset page
                next_page: number of the next page
                prev_page: number of the previous page
                total_pages: the total number of pages in the dataset
        """
        data = self.get_page(page, page_size)
        next_page = page + 1
        prev_page = page - 1
        total_pages = ceil(len(self.__dataset) / page_size)
        if prev_page < 1:
            prev_page = None
        try:
            self.__dataset[page * page_size]
        except IndexError:
            next_page = None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages

        }
