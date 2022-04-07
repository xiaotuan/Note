[toc]

SQLite 的 **LIKE** 运算符是用来匹配通配符指定模式的文本值。如果搜索表达式与模式表达式匹配，LIKE 运算符将返回真（true），也就是 1。这里有两个通配符与 LIKE 运算符一起使用：

- 百分号 （`%`）
- 下划线 （`_`）

百分号（`%`）代表零个、一个或多个数字或字符。下划线（`_`）代表一个单一的数字或字符。这些符号可以被组合使用。

下面一些实例演示了 带有 '%' 和 '_' 运算符的 LIKE 子句不同的地方

| 语句                      | 描述                                            |
| :------------------------ | :---------------------------------------------- |
| WHERE SALARY LIKE '200%'  | 查找以 200 开头的任意值                         |
| WHERE SALARY LIKE '%200%' | 查找任意位置包含 200 的任意值                   |
| WHERE SALARY LIKE '_00%'  | 查找第二位和第三位为 00 的任意值                |
| WHERE SALARY LIKE '2_%_%' | 查找以 2 开头，且长度至少为 3 个字符的任意值    |
| WHERE SALARY LIKE '%2'    | 查找以 2 结尾的任意值                           |
| WHERE SALARY LIKE '_2%3'  | 查找第二位为 2，且以 3 结尾的任意值             |
| WHERE SALARY LIKE '2___3' | 查找长度为 5 位数，且以 2 开头以 3 结尾的任意值 |

> 提示
>
> 您可以使用 AND 或 OR 运算符来结合 N 个数量的条件。

**示例代码**

```java
String sql  = "select * from " + TABLE_USER + " where people_name like ? or phone_number_text like ? or office_number_text like ? or family_number_text like ?"; 
String [] selectionArgs  = new String[]{"%" + search_context + "%", 
                                        "%" + search_context + "%", 
                                        "%" + search_context + "%",  
                                        "%" + search_context + "%"}; 
Cursor cursor = sqldb.rawQuery(sql, selectionArgs); 
```

或者

```java
String where = MediaStore.Audio.Media.DATA + " LIKE ?";
Cursor recordingFileCursor = getContentResolver().query(
    MediaStore.Audio.Media.EXTERNAL_CONTENT_URI,
    new String[] {
        MediaStore.Audio.Media.ARTIST, MediaStore.Audio.Media.ALBUM,
        MediaStore.Audio.Media.DATA, MediaStore.Audio.Media.DURATION,
        MediaStore.Audio.Media.DISPLAY_NAME, MediaStore.Audio.Media.DATE_ADDED,
        MediaStore.Audio.Media.TITLE, MediaStore.Audio.Media._ID
    }, where, new String[] {"%Recording/record%.amr"}, null);
```



