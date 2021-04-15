# Формат входных данных:
# В первой строке указаны два числа разделенных пробелом: <число вершин> и <число ребер>.
# В следующих <число ребер> строках указаны пары вершин, соединенных ребром.
# Выполняются ограничения: 2≤v≤1000,0≤e≤1000.
#
# Формат выходных данных:
# "There isn't euler cycle.", если в графе нет эйлерова цикла,
# или список вершин в порядке обхода эйлерова цикла, если он есть.
#
# Пример ввода и вывода:
# '''
# 3 3
# 1 2
# 2 3
# 3 1
#
# 1 2 3
# '''


def main():
    e, vertex_count = input_data()

    if not check_vertexes_degree_for_parity(vertex_count, e):
        print("\nThere isn't euler cycle.")
        return

    paths = []
    while sum([1 for link in e if not link.used]) > 0:
        current_start = find_not_used_link(e).e[0]
        current_path = [current_start]
        paths.append(fill_path(current_path, e))

    result_path = get_merged_path(paths)
    print("\n" + " ".join(result_path))


def get_merged_path(paths):
    while len(paths) > 1:
        first_path = paths[0]
        second_path = get_intersecting_path(first_path, paths)
        merged = merge_paths(first_path, second_path)

        paths.remove(first_path)
        paths.remove(second_path)
        paths.append(merged)

    return paths[0]


def get_intersecting_path(first_path, paths):
    for second_path in paths[1:]:
        common_vertex = get_common_vertex(first_path, second_path)
        if common_vertex:
            return second_path

    return None


def merge_paths(first_path, second_path):
    common_vertex = get_common_vertex(first_path, second_path)

    common_vertex_index = second_path.index(common_vertex)
    path_for_embedding = second_path[common_vertex_index + 1:] + second_path[:common_vertex_index]
    # [second_path[(second_path.index(same_top)+1+k)%len(second_path)]
    # for k in range(len(second_path)-1)]

    merged = first_path[:(first_path.index(common_vertex) + 1)] + \
        path_for_embedding + \
        first_path[(first_path.index(common_vertex)):]

    return merged


def get_common_vertex(first_path, second_path):
    for i in first_path:
        for j in second_path:
            if i == j:
                return i
    return None


def fill_path(current_path, e):
    current_start = current_path[-1]
    for link in e:
        if current_start in link.e and not link.used:
            link.used = True
            current_start = link.get_another_vertex(current_start)
            if current_path[0] == current_start:
                return current_path
            current_path.append(current_start)
    return fill_path(current_path, e)


def check_vertexes_degree_for_parity(vertex_count, e):
    for i in range(1, vertex_count + 1):
        vertex_degree = sum([1 for link in e if str(i) in link.e])
        if vertex_degree % 2 != 0 or vertex_degree == 0:
            return False

    return True


def find_not_used_link(e):
    for link in e:
        if not link.used:
            return link
    return None


def input_data():
    vertex_count, edges_count = map(int, input().split())
    e = []
    for i in range(edges_count):
        e.append(Link(input().split()))
    return e, vertex_count


class Link:
    def __init__(self, edge):
        self.e = edge
        self.used = False

    def get_another_vertex(self, vertex):
        return self.e[self.e.index(vertex) - 1]


if __name__ == "__main__":
    main()
