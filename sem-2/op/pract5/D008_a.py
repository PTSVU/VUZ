import pickle
import datetime


def loging(text):
    with open("D008_a.txt", 'a') as log:
        log.write(text)

class CoolClass:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        text = "\n\tCRE" + f" --- {str(datetime.datetime.now())} --- " + f"Create: {self.name}\n"
        loging(text)

    def update_data(self, new_data):
        self.data = new_data
        text = "\n\tCRE" + f" --- {str(datetime.datetime.now())} --- " + f"Change the data to: {self.data}\n"
        loging(text)

    def print_data(self):
        print(self.data)
        text = "\n\tCRE" + f" --- {str(datetime.datetime.now())} --- " + f"Print data: {self.data}\n"
        loging(text)


a = CoolClass("Ы", 2)

a.print_data()
a.update_data(777)
a.print_data()

with open("D008_a.pkl", "wb") as ser:
    pickle.dump(a, ser)

with open("D008_a.pkl", "rb") as deser:
    deser = pickle.load(deser)

deser.print_data()
deser.update_data("))))))))")
deser.print_data()