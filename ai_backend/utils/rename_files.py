import os


# Function to rename multiple files
def main():

    path = '/Users/davidbanda/Desktop/Object/'
    name = 'popo'

    for count, filename in enumerate(os.listdir(path)):
        dst = name + str(count) + ".jpg"
        src = path + filename
        dst = path + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)


if __name__ == '__main__':
    main()
