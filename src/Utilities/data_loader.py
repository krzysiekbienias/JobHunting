import os
class DataLoader:

    @staticmethod
    def feed_from_txt(file_name,as_type,sep=" "):
        file=open(file_name)
        data=file.read()
        data_list=data.split(sep)
        print(f"input sample has length {len(data_list)}")
        if as_type=="int":
            data_list=[int(i) for i in data_list]

            return data_list

        else:
            return data_list


