from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: [List] = []
        self.topics: [List] = []
        self.documents: [List] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category in self.categories:
            if category.id == category_id:
                category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.edit(new_file_name)

    def delete_category(self, category_id: int):
        self.categories.remove([category for category in self.categories if category.id == category_id][0])

    def delete_topic(self, topic_id: int,):
        self.topics.remove([topic for topic in self.topics if topic.id == topic_id][0])

    def delete_document(self, document_id: int):
        self.documents.remove(self.get_document(document_id))

    def get_document(self, document_id: int):
        return [document for document in self.documents if document.id == document_id][0]

    def __repr__(self):
        return "\n".join(str(document) for document in self.documents)
