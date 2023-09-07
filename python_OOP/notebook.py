class Note:
    def __init__(self, content=None):
        self.content = content

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.content

    def write_content(self, content: str):
        self.content = content

    def remove(self):
        self.content = ""
        return self

    def __add__(self, other):
        return self.content + other.content


class Notebook:
    def __init__(self, title: str, notes: dict, page_number: int = 1):
        self.page_number = page_number
        self.title = title
        self.notes = notes

    def add_note(self, note: Note, pointing_page: int = -1):
        if self.page_number >= 300:
            print("최대 300 page가 다 찼습니다.")

        if pointing_page == -1:
            self.notes[self.page_number] = note
            self.page_number += 1
        else:
            self.notes[pointing_page] = note
            self.page_number += 1

    def remove_note(self, pointing_number: int):
        if pointing_number in self.notes.keys():
            return self.notes.pop(pointing_number)
        else:
            print("해당 페이지는 존재 하지 않습니다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())
