import xlrd

class excel(object):

    def __init__(self):
        self.path = 'D:\\1111.xlsx'


    def read(self, sheetnm):

        book = xlrd.open_workbook(self.path)
        #获取sheetname的值
        sheetname = book.sheet_names()
        for sheetnm in sheetname:
            sheet = book.sheet_by_name(sheetnm)
            nrow = sheet.nrows

            for i in range(1, nrow):
                content = sheet.row_values(i)
                formatercontent = self.formater(content)
                self.content.append(formatercontent)
            else:
                print('sheetname{} 不存在，请检查！'\
                      .format(sheetnm))
            return self.content

    def formater(self, txt):
        '''

        :param txt:
        :return:newlist列表
        '''
        newlist= []
        for ct in txt:
            if isinstance(ct, float):
                newlist.append(int(ct))
            else:
                newlist.append(ct)
        return newlist

    def parse_excel(self, config_path, sheetnm):
        '''

        :param config_path: 传入文件路径
        :param sheetnm:传入excel的sheet页的名字
        :return:返回
        '''
        initial_excel = excel(config_path)
        content = initial_excel.read(sheetnm)
        return content


    def gettestcase_by_name(self, content_list, casename):
        '''

        :param content_list: 内容列表
        :param casename: 测试用例的名称
        :return: 返回excel行内容
        '''

        if len(content_list) == 0:
            raise ("excel,内容为空！")
        else:
            for subrow in content_list:
                if casename in subrow:
                    return subrow

    def read_excel(path='', colnameindex=0, by_name='Sheet1'):
        book = xlrd.open_workbook(path)
        table = book.sheet_by_name(by_name)
        colnames = table.row_values(colnameindex)
        nrow = table.nrows
        list = []
        for rownum in range(0, nrow):
            row = table.row_values(rownum)
            if row:
                app = []
                for i in range(len(colnames)):
                    app.append(row[i])
                list.append(app)
        return list

if __name__ == '__main__':
    # path =
    # a = excel.read_excel()
    # print(a)
    a = excel.read(sheetnm='Sheet1', )
    print(a)