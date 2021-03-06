from my_modules.my_functions import get_root_path, get_photo_files, get_photo_data


def main():
    # get root path and validate it (a bekért utvonal ellenőrzése és rögzítése)
    root_folder = get_root_path()

    # list jpg files in path (listázza a jpg fájlokat az elérési utban megadott könyvtárból)
    photos = get_photo_files(root_folder)

    # collect data from images
    photo_data_list = [get_photo_data(i) for i in photos]


if __name__ == '__main__':
    main()
