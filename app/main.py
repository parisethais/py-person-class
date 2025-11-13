from typing import List, Dict, Any


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[Dict[str, Any]]) -> List[Person]:
    Person.people = {}

    person_list: List[Person] = []

    for data in people:
        person = Person(name=data["name"], age=data["age"])
        person_list.append(person)

    for data in people:
        name = data["name"]
        person = Person.people[name]

        if "wife" in data:
            spouse_name = data["wife"]
            if spouse_name is not None:
                spouse = Person.people[spouse_name]
                setattr(person, "wife", spouse)

        if "husband" in data:
            spouse_name = data["husband"]
            if spouse_name is not None:
                spouse = Person.people[spouse_name]
                setattr(person, "husband", spouse)

    return person_list
