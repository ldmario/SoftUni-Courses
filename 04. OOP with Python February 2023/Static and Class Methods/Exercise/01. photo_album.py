from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: [] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.MAX_PHOTOS_ON_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < PhotoAlbum.MAX_PHOTOS_ON_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        result = ["-" * 11]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

        return "\n".join(result)

