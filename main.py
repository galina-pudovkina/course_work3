from utils import load_operations, select_data, sort_data, create_operations

PATH_TO_OPERATIONS = "operations.json"


def main():

    data = load_operations(PATH_TO_OPERATIONS)
    data = select_data(data)
    data = sort_data(data)
    data = create_operations(data)
    print(*data)


if __name__ == "__main__":
    main()
