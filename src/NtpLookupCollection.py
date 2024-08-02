import json
from .NtpLookup import NtpLookup

class NtpLookupCollection(object):

 def __init__(self) -> None:
  super().__init__()
  self._data = None

 def validate(self):
  names: set[str] = set()
  for lookup in self._data:

   if not lookup.has_name():
    raise ValueError("A lookup within {} does not have a name".format(__class__.__name__))

   if lookup.get_name().startswith("#"):
    raise ValueError("{} may not begin with a # in {}".format(lookup.get_name(), __class__.__name__))

   if lookup.get_name() in names:
    raise ValueError("{} is duplicated in {}".format(lookup.get_name(), __class__.__name__))

   names.add(lookup.get_name())
  return True

 def get_by_name(self, name: str) -> NtpLookup:
  for lookup in self._data:
   if name == lookup.get_name():
    return lookup
  return None
 
 def get_by_category(self, category: str) -> set[NtpLookup]:
  results: set[NtpLookup] = set()
  category = category.lower().strip().lstrip("#")
  for lookup in self._data:
   if lookup.has_categories() and category in lookup.get_categories():
    results.add(lookup)
  return results

 def get_categories(self) -> set[str]:
  cats = set()
  for l in self._data:
   cats |= l.get_categories()
  return cats
 
 def __bool__(self) -> bool:
  return self._data is not None

 def __len__(self) -> int:
  return len(self._data)

 def __iter__(self):
  return iter(self._data)
 
 def __getitem__(self, index: int|str) -> NtpLookup|None:
  if type(index) == int:
   return self._data[index]
  elif type(index) == str:
   if index.startswith("#"):
    return self.get_by_category(index)
   else:
    return self.get_by_name(index)
  raise TypeError("index type is invalid for {}".format(__class__.__name__))

 @classmethod
 def fromfile(cls, filepath: str):
  lc = cls()
  with open(filepath) as f:
   data = json.load(f)
  lc._data = list(map(lambda e: NtpLookup(e), data))
  lc._data.sort(key=lambda l: l.get_name())
  return lc
