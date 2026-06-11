import pickle
import os


def load_data(filename):

    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "rb") as file:
            return pickle.load(file)

    except EOFError:
        return []

    except Exception as e:
        print("Error Loading Data :", e)
        return []


def save_data(filename, data):

    try:
        with open(filename, "wb") as file:
            pickle.dump(data, file)

    except Exception as e:
        print("Error Saving Data :", e)