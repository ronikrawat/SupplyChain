from xlrd import open_workbook


def worksheet(worksheet_name):
    def get_locators(cls):
        book = open_workbook(r"D:\supplychain\pythonProject\locator.xls")
        sheet = book.sheet_by_name(worksheet_name)
        used_rows = sheet.nrows
        for i in range(1, used_rows):
            row = sheet.row_values(i)
            setattr(cls, row[0], (row[1], row[2]))
        return cls
    return get_locators
