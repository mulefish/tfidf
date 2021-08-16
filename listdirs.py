import os
rootPath = "src/"
ignore = ["", ".."]
seen = {}


def step1_gatherData():
    for root, dirs, files in os.walk(rootPath):
        for filename in files:
            x = "{}/{}".format(root, filename)
            x = x.replace(os.sep, '/')
            print(x)


if __name__ == "__main__":
    step1_gatherData()
