from xlrd import open_workbook

_test_data_file = r"D:\supplychain\pythonProject\TestData.xls"
_locator_file = r"D:\supplychain\pythonProject\locator.xls"


def worksheet(worksheet_name):
    def get_locators(cls):
        book = open_workbook(_locator_file)
        sheet = book.sheet_by_name(worksheet_name)
        used_rows = sheet.nrows
        for i in range(1, used_rows):
            row = sheet.row_values(i)
            setattr(cls, row[0], (row[1], row[2]))
        return cls

    return get_locators


def get_test_data_header(worksheet, testcase):
    book = open_workbook(_test_data_file)
    sheet = book.sheet_by_name(worksheet)
    used_rows = sheet.nrows
    header = ""
    for i in range(0,used_rows):
        row = sheet.row_values(i)
        if row[0] == testcase:
            row1 = sheet.row_values(i-1)
            header = [i.strip() for i in row1[2:] if i.strip()]
            break
    return ",".join(header)


def get_test_data(worksheet, testcase):
    book = open_workbook(_test_data_file)
    sheet = book.sheet_by_name(worksheet)
    used_rows = sheet.nrows
    test_data = []
    for i in range(1, used_rows):
        row = sheet.row_values(i)
        if row[0] == testcase:
            row = [str(i).strip() for i in row[2:] if str(i).strip()]
            test_data.append(tuple(row))
    return test_data
