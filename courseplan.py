#sivulta https://tira.mooc.fi/kevat-2025/osa13/#suunnatun-verkon-esitt%C3%A4minen
class TopologicalSort:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def visit(self, node):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return

        self.state[node] = 1
        for next_node in self.graph[node]:
            self.visit(next_node)

        self.state[node] = 2
        self.order.append(node)

    def create(self):
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0

        self.order = []
        self.cycle = False

        for node in self.nodes:
            if self.state[node] == 0:
                self.visit(node)

        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order


class CoursePlan:
    def __init__(self):
        self.kurssit = []
        self.vaatimukset = []

    def add_course(self, course):
        self.kurssit.append(course)

    def add_requisite(self, course1, course2):
        self.vaatimukset.append((course1, course2))

    def find_order(self):
        sorttaaja = TopologicalSort(self.kurssit)

        for req, dep in self.vaatimukset:
            sorttaaja.add_edge(req, dep)

        sortattu = sorttaaja.create()
        return sortattu

if __name__ == "__main__":
    courses = CoursePlan()

    courses.add_course("Ohpe")
    courses.add_course("Ohja")
    courses.add_course("Tira")
    courses.add_course("Jym")

    courses.add_requisite("Ohpe", "Ohja")
    courses.add_requisite("Ohja", "Tira")
    courses.add_requisite("Jym", "Tira")

    print(courses.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]

    courses.add_requisite("Tira", "Tira")

    print(courses.find_order()) # None
