import docx
import shutil
import re
import os

class Operation:
    @classmethod
    def segregate(cls, src:str)->str:
        """
        This method will segregate all the files at the specific source location into the folders, which the program creates itself based on the name of the file.
        :param src: str
        :return: str
        """
        meta_dict = {}
        patt_lst = []

        for file in os.listdir(src):

            # Rename the files without '_'
            if not ("_" in file) and not (file.endswith(".py")):
                # print(file)
                name = re.findall(r"^[A-Za-z][A-Za-z0-9_]+[^_^.]", file)[0] # Assignment1
                ext = re.findall(r"[.].+", file)[0] #.docx
                # print(name,ext)
                rename_file = f"Programming_" + name + " (1)" + ext  # Programming_Assignment1 (1).docx
                os.rename(src=file, dst=rename_file)

        # Rename the duplicate files
        # # Replacing () with Advanced
        for file in os.listdir(src):
            if not os.path.isdir(file):

                if re.search(r"\(\d\)", file):
                    rename_file = re.sub(r"\s\(\d\)", "(Advanced)", file)
                    os.rename(src=file, dst=rename_file)
                else:
                    rename_file = file

                # Create the respective folders
                cat = re.findall(r"^[A-Za-z_\(\)]+[^0-9^.^_^\s]", rename_file)[0]


                patt = re.findall(r"[A-Za-z]+[^_]", cat)[0]

                # Creating the respective directories...
                if not (rename_file.endswith(".py")):
                    if re.search("\(Advanced\)", rename_file):
                        cat += "_Advanced"  # Assignment_Advanced
                        patt += "_A"
                        meta_dict[patt] = cat
                    else:
                        cat += "_Basic"
                        patt += "_B"
                        meta_dict[patt] = cat


                    if patt not in patt_lst:
                        patt_lst.append(patt)
                        os.mkdir(meta_dict[patt])

                # Moving the files to respective folders
                if not rename_file.endswith(".py"):
                    shutil.move(src=rename_file, dst=f".\\{meta_dict[patt]}")
    print("All files segregated successfully")

    @classmethod
    def write_to_file(cls, src, dst, ext):
        """
        This will write all the data of the files in the source location to a single destination file with the proper formatting. This function has the
        power to extract all the file with given extension (ext) even from the sub-directories. Thus, you can give the source location as the outermost directory.
        :param src:
        :param dst:
        :param ext:
        :return:
        """
        combined = open(dst, "w+", encoding="utf-8")
        for dir_path, dir_names, file_names in os.walk(src):
            for file in file_names:
                if file.endswith(ext):
                    path = os.path.join(dir_path, file)
                    heading = re.findall(r"[A-Za-z_0-9\(\)]+[^.]", file)[0]

                    try:
                        doc = docx.Document(path)
                        data = ""
                        full_text = []
                        combined.writelines(f"\n\n----------------- {heading} ------------------\n\n")

                        for para in doc.paragraphs:

                            full_text.append(para.text)
                            data = '\n'.join(full_text)

                        combined.write(data)

                    except IOError:
                        print("There was an error opening the file.")
                        return

        combined.close()
        print(f"All the files data copied to {dst}")
