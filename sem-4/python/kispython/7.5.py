class DecisionTree:
    def __init__(self, threshold=None, value=None, children=None):
        self.threshold = threshold
        self.value = value
        self.children = children if children is not None else {}

    def fit(self, data_points):
        for data_point, result in data_points.items():
            node = self
            for feature in data_point:
                if feature not in node.children:
                    node.children[feature] = DecisionTree()
                node = node.children[feature]
            node.value = result

    def predict(self, data_point):
        node = self
        for feature in data_point:
            if feature not in node.children:
                return None
            node = node.children[feature]
        return node.value


def main(data):  # Способ 5
    tree = DecisionTree()
    data_points = {
        (1989, 'ROFF', 1994, 1986, 2013): 0,
        (1989, 'ROFF', 1994, 1986, 2018): 1,
        (1989, 'SASS', 1994, 1986, 2013): 2,
        (1989, 'SASS', 1994, 1986, 2018): 3,
        (1989, 'EQ', 1994, 1986, 2013): 4,
        (1989, 'EQ', 1994, 1986, 2018): 5,
        (1962, 'EQ', 2003, 1986, 2013): 6,
        (1962, 'ROFF', 2003, 1986, 2018): 7,
        (1962, 'ROFF', 1994, 1986, 2018): 8,
        (1999, 'SASS', 1994, 1986, 2018): 9,
        (1999, 'SASS', 1994, 1960, 2013): 10,
        (1962, 'EQ', 2003, 1989, 2013): 11,
        (1989, 'SASS', 2003, 1986, 2018): 3,
        (1962, 'SASS', 2003, 1986, 2013): 6,
        (1989, 'EQ', 2003, 1986, 2013): 4,
        (1962, 'EQ', 1994, 1986, 2018): 8,
    }
    tree.fit(data_points)
    return tree.predict(data)
