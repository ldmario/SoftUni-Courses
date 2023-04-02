from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.category: [List] = []
        self.topics: [List] = []
        self.documents: [List] = []

    def add_category(self, category: Category):
        pass

    def add_topic(self, topic: Topic):
        pass

    def add_document(self, document: Document):
        pass

    def edit_category(self, category_id: int, new_name: str):
        pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        pass

    def edit_document(self, document_id: int, new_document: str):
        pass

    def delete_category(self, category_id: int):
        pass

    def delete_topic(self, topic_id: int,):
        pass

    def delete_document(self, document_id: int):
        pass

    def __repr__(self):
        pass
