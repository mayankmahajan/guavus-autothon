class ObjectRepository(object):
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path) as csv_file:
            readcsv = csv_file.readlines()
            self.result = {}
            for i in range(len(readcsv)):
                self.result[readcsv[i].split(";")[0]] = [readcsv[i].split(";")[1].strip(),
                                                         readcsv[i].split(";")[2].strip(),
                                                         readcsv[i].split(";")[3].strip()]

    def get_type(self, name):
        print self.result[name][0]
        return self.result[name][0]

    def get_value(self, name):
        print self.result[name][1]
        return self.result[name][1]

    def get_frame(self, name):
        print self.result[name][2]
        return self.result[name][2]