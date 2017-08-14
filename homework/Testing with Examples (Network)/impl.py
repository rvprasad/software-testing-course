class Node(object):
    def __init__(self):
        super().__init__()
        self.name = None


class Edge(object):
    def __init__(self, node1, node2):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.friend = None


class Network(object):
    NAME_PROP = "name"     # NAME_PROP is an optional string property
    FRIEND_PROP = "friend" # FRIEND_PROP is an optional boolean property

    
    def __init__(self):
        self.nodes = set()
        self.edges = set()
        
    def create_person(self):
        node = Node()
        self.nodes.add(node)
        return node
    
    # add prop to value; overwrite if prop exists
    def add_person_property(self, person, prop, value):
        # flag non-existent person
        if person not in self.nodes:
            raise RuntimeError("person does not exist")
        # disallow non-string values for NAME_PROP property
        if prop == Network.NAME_PROP:
            if not isinstance(value, str):
                raise TypeError(
                    "{0} is a string property".format(Network.NAME_PROP))

            # disallow multiple people to have the same name
            for p in self.nodes:
                if p.name == value and p is not person:
                    raise ValueError("{0} name already taken".format(value))
            person.name = value
        
    def add_relation(self, person1, person2):
        # flag non-existent persons
        if person1 not in self.nodes:
            raise RuntimeError("person1 does not exist")
        if person2 not in self.nodes:
            raise RuntimeError("person2 does not exist")
        # flag existing edge
        for e in self.edges:
            if (e.node1 is person1 and e.node2 is person2) or \
                (e.node1 is person2 and e.node2 is person1):
                raise ValueError("relation exists")
        self.edges.add(Edge(person1, person2))

    def add_relation_property(self, person1, person2, prop, value):
        edge = None
        for e in self.edges:
            if (e.node1 is person1 and e.node2 is person2) or \
                (e.node1 is person2 and e.node2 is person1):
                edge = e
                break
        else:
            # flag non-existent relation
            raise RuntimeError("Non-existent relation")
        # disallow non-boolean values for FRIEND_PROP property
        if prop == Network.FRIEND_PROP:
            if not isinstance(value, bool):
                raise TypeError(
                    "{0} is a boolean property".format(Network.FRIEND_PROP))
            edge.friend = value

    # get a person with given name
    def get_person(self, name):
        # disallow non-string values for name
        if not isinstance(name, str):
            raise TypeError(
                "{0} is a string argument".format(Network.NAME_PROP))
        for n in self.nodes:
            if n.name == name:
                return n
        # flag non-existent person
        raise RuntimeError("No person named {0}".format(name))

    # get friends of friends of a person with given name
    def friends_of_friends(self, name):
        # disallow non-string values for name
        if not isinstance(name, str):
            raise TypeError(
                "{0} is a string argument".format(Network.NAME_PROP))
        # flag non-existent person
        person = self.get_person(name)
        visited = set([person])
        i = 0
        while i < 2:
            newly_visited = set()
            for p in (x for x in visited):
                for e in (x for x in self.edges if x.friend == True):
                    n1 = e.node1
                    n2 = e.node2
                    if n1 == p:
                        newly_visited.add(e.node2)
                    elif n2 == p:
                        newly_visited.add(e.node1)
            visited = newly_visited
            i += 1
        return list(visited)
