# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ToolShed
class Favorite:
    def __init__(self, name, category, notes=""):
        self.name = name
        self.category = category
        self.notes = notes

    def to_dict(self):
        return {"name": self.name, "category": self.category, "notes": self.notes}

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["category"], d.get("notes", ""))

    def __repr__(self):
        return f"<Favorite {self.name} [{self.category}]>"

class FavoriteList:
    def __init__(self):
        self._items = []

    def add(self, fav):
        if isinstance(fav, Favorite):
            self._items.append(fav)
        else:
            self._items.append(Favorite(**fav))

    def remove(self, name):
        self._items = [f for f in self._items if f.name != name]

    def get(self, name):
        for f in self._items:
            if f.name == name:
                return f
        return None

    def list_favorites(self):
        return [f for f in self._items if f is not None]

    def to_dict(self):
        return [f.to_dict() for f in self.list_favorites()]

    @classmethod
    def from_dict(cls, d):
        lst = cls()
        for item in d:
            lst.add(item)
        return lst
