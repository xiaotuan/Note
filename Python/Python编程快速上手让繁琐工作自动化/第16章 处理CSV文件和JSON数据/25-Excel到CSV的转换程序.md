### Excel到CSV的转换程序

Excel可以将电子表格保存为CSV文件，实现只需要点几下鼠标。但如果有几百个Excel文件要转换为CSV，就需要单击几小时。利用第12章的 `openpyxl` 模块，编程读取当前工作目录中的所有Excel文件，并输出为CSV文件。

一个Excel文件可能包含多个工作表，必须为每个表创建一个CSV文件。CSV文件的文件名应该是<Excel文件名>_<表标题>.csv，其中<Excel文件名>是没有扩展名的Excel文件名（例如 `'spam_data'` ，而不是 `'spam_data.xlsx'` ），<表标题>是 `Worksheet` 对象的 `title` 变量中的字符串。

该程序将包含许多嵌套的 `for` 循环。程序的框架看起来像这样：

```javascript
for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)
        # Create the CSV filename from the Excel filename and sheet title.
        # Create the csv.writer object for this CSV file.
        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []  # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
            # Write the rowData list to the CSV file. 
        csvFile.close()
```

从异步社区本书对应页面下载ZIP文件excelSpreadsheets.zip，并将这些电子表格解压缩到程序所在的目录中。可以使用这些文件来测试程序。



