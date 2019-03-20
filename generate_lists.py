
def main():
    jack = {
        "name": "jack",
        "car": "bmw"
    }

    john = {
        "name": "john",
    }
    users = [jack, john]
    names = ['jack', 'john', 'oleg', 'ulya']

    # generate list in one string
    def gen_list_from_dict_list(users):
        cars = [person.get("car", "no car") for person in users]
        return cars

    # generate list with filters for elements
    def gen_list_with_filters(names):
        new_names = [n for n in names if n.startswith('j')]
        return new_names

    print(gen_list_from_dict_list(users))
    print(gen_list_with_filters(names))

if __name__ == "__main__":
    main()
