import xlrd
class ExcelData():

    def excel_login(self):
        xl = xlrd.open_workbook(r'.\data.xlsx')
        table = xl.sheets()[0]
        #   获取第一行所有内容
        keys = table.row_values(0)
        #   获取工作表有效行数
        rowNum = table.nrows
        #   获取工作表有效列数
        colNum = table.ncols
        datas = []
        for i in range(1,rowNum):
            sheet_data = {}
            for j in range(colNum):
                #   获取单元格得数据类型
                c_type = table.cell(i,j).ctype
                #   获取单元格得数据
                c_cell = table.cell_value(i,j)
                #   如果是整形
                if c_type == 2 and c_cell % 1 == 0:
                    c_cell = int(c_cell)
                sheet_data[keys[j]] = c_cell
                #   循环每一个有效得单元格，将字段与值对应存储到字典中
                #   字典的key就是excel中每列第一行得字段
            #   将字典追加到列表中
            datas.append(sheet_data)
        return datas

a = ExcelData()
b = a.excel_login()
print(b)




