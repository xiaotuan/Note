[toc]

`SQLiteDatabase` 中 `query()` 有如下三种：

```java
public Cursor query(String table, String[] columns, String selection,
            String[] selectionArgs, String groupBy, String having,
            String orderBy)

public Cursor query(String table, String[] columns, String selection,
            String[] selectionArgs, String groupBy, String having,
            String orderBy, String limit) {
    
public Cursor query(boolean distinct, String table, String[] columns,
            String selection, String[] selectionArgs, String groupBy,
            String having, String orderBy, String limit)
```

第一个 `query()` 方法是标准方法，在第一个参数中指定表，然后在第二个参数中返回哪些列。这相当于在标准 `SQL` 中执行 `SELECT` 语句。然后，在第三个参数中，我们开始过滤查询，这些过滤器的语法相当于在 `SELECT` 查询的末尾包含一个 `WHERE` 子句。例如：

```
WHERE course_id = ?
```

在这里，问号充当了我们将传递到过滤器中的任何值的位置。换句话说，`WHERE` 语句的格式是存在的，但我们只需要在问号中替换我们想要筛选的实际值。在这种情况下，我们将给定的课程 `ID` 传递给第四个参数。

最后三个参数（ `groupBy`、`have` 和 `orderBy` ）对于熟悉 `SQL` 的人来说应该很有意义，但对于不熟悉 `SQL` 的人们来说，以下是对每一个参数的快速解释：

+ `groupBy`——添加此项将允许您按指定列对结果进行分组。如果你需要获得一个包含课程 `ID` 和该课程注册学生人数的表，这将派上用场：只需在 `Class` 表中按课程 `ID` 分组即可实现这一点。
+ `having`——与 `groupBy` 子句一起使用，该子句允许您筛选聚合结果。假设您在“班级”表中按课程 ID 分组，并希望筛选出注册学生少于 10 人的所有班级，您可以使用 `have` 子句来实现这一点。
+ `orderBy`—— `orderBy` 子句是一个非常简单的子句，它允许我们按照指定的列以及升序或降序对查询结果的子表进行排序。例如，假设您想按年级然后按姓名对 `Students` 表进行排序——指定 `orderBy` 子句将允许您这样做。

最后，在两个 `query()` 变体中，您将看到添加的参数 `limit` 和 `distinct` ：`limit` 参数允许您限制要返回的行数，而 `distinct` 布尔值允许您指定是否只返回不同的行。

### 1. Kotlin 版本

#### 1.1 StudentTable.kt

```kotlin
package com.android.advancedsqlite

object StudentTable {

    // EACH STUDENT HAS UNIQUE ID
    const val ID = "_id"

    // NAME OF THE STUDENT
    const val NAME = "student_name"

    // STATE OF STUDENT'S RESIDENCE
    const val STATE = "state"

    // GRADE IN SCHOOL OF STUDENT
    const val GRADE = "grade"

    // NAME OF THE TABLE
    const val TABLE_NAME = "students"
}
```

#### 1.2 CourseTable.kt

```kotlin
package com.android.advancedsqlite

object CourseTable {

    // UNIQUE ID OF THE COURSE
    const val ID = "_id"

    // NAME OF THE COURSE
    const val NAME = "course_name"

    // NAME OF THE TABLE
    const val TABLE_NAME = "courses"
}
```

#### 1.3 ClassTable.kt

```kotlin
package com.android.advancedsqlite

// This essentially represents a mapping from students to courses
object ClassTable {

    // Unique id of each row - no real meaning here
    const val ID = "_id"

    // The id of the student
    const val STUDENT_ID = "student_id"

    // The id of associated course
    const val COURSE_ID = "course_id"

    // The name of the table
    const val TABLE_NAME= "classes"
}
```

#### 1.4 SchemaHelper.kt

```kotlin
package com.android.advancedsqlite

import android.content.ContentValues
import android.content.Context
import android.database.Cursor
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import android.util.Log

private const val TAG = "SchemaHelper"
private const val DATABASE_NAME = "adv_data.db"
private const val DATABASE_VERSION = 1

class SchemaHelper(context: Context): SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {

    override fun onCreate(db: SQLiteDatabase?) {
        // Create students table
        db?.execSQL("CREATE TABLE ${StudentTable.TABLE_NAME} (${StudentTable.ID} INTEGER PRIMARY KEY AUTOINCREMENT," +
                "${StudentTable.NAME} TEXT," +
                "${StudentTable.STATE} TEXT," +
                "${StudentTable.GRADE} INTEGER);")
        // Create courses table
        db?.execSQL("CREATE TABLE ${CourseTable.TABLE_NAME} (${CourseTable.ID} INTEGER PRIMARY KEY AUTOINCREMENT," +
                "${CourseTable.NAME} TEXT);")
        // Create classes mapping table
        db?.execSQL("CREATE TABLE ${ClassTable.TABLE_NAME} (${ClassTable.ID} INTEGER PRIMARY KEY AUTOINCREMENT," +
                "${ClassTable.STUDENT_ID} INTEGER," +
                "${ClassTable.COURSE_ID} INTEGER);")
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        Log.w(TAG, "Upgrading database from version $oldVersion to $newVersion which will destroy all old data")

        // Kill previous tables if upgraded
        db?.execSQL("DROP TABLE IF EXISTS ${StudentTable.TABLE_NAME}")
        db?.execSQL("DROP TABLE IF EXISTS ${CourseTable.TABLE_NAME}")
        db?.execSQL("DROP TABLE IF EXISTS ${ClassTable.TABLE_NAME}")

        // Create new instance of schema
        onCreate(db)
    }

    // Wrapper method for adding a student
    fun addStudent(name: String, state: String, grade: Int): Long {
        // Create a contentvalue object
        val cv = ContentValues().apply {
            put(StudentTable.NAME, name)
            put(StudentTable.STATE, state)
            put(StudentTable.GRADE, grade)
        }

        // Retrieve writeable database and insert
        return writableDatabase.run {
            insert(StudentTable.TABLE_NAME, StudentTable.NAME, cv)
        }
    }

    // Wrapper method for adding a course
    fun addCourse(name: String): Long {
        val cv = ContentValues().apply {
            put(CourseTable.NAME, name)
        }

        return writableDatabase.run {
            insert(CourseTable.TABLE_NAME, CourseTable.NAME, cv)
        }
    }

    // Wrapper method for enrolling a student into a course
    fun enrollStudentClass(studentId: Int, courseId: Int): Boolean {
        val cv = ContentValues().apply {
            put(ClassTable.STUDENT_ID, studentId)
            put(ClassTable.COURSE_ID, courseId)
        }

        return writableDatabase.run {
            insert(ClassTable.TABLE_NAME, ClassTable.STUDENT_ID, cv)
        } >= 0
    }

    // Get all students in a course
    fun getStudentsForCourse(courseId: Int): Cursor {
        // We only need to return student IDs
        val cols = arrayOf( ClassTable.STUDENT_ID )

        val selectionArgs = arrayOf( courseId.toString() )

        // Query class map for students in course
        return readableDatabase.query(ClassTable.TABLE_NAME, cols, "${ClassTable.COURSE_ID} = ?",
            selectionArgs, null, null, null)
    }

    // Get all courses for a given student
    fun getCoursesForStudent(studentId: Int): Cursor {
        // We only need to return course IDs
        val cols = arrayOf( ClassTable.COURSE_ID )

        val selectionArgs = arrayOf( studentId.toString() )

        return readableDatabase.query(ClassTable.TABLE_NAME, cols, "${ClassTable.STUDENT_ID} = ?",
            selectionArgs, null, null, null)
    }

    fun getStudentsByGradeForCourse(courseId: Int, grade: Int): Set<Int> {
        // We only need to return course IDs
        var cols = arrayOf( ClassTable.STUDENT_ID )

        var selectionArgs = arrayOf( courseId.toString() )

        // Query class map for students in course
        var c = readableDatabase.query(ClassTable.TABLE_NAME, cols, "${ClassTable.COURSE_ID} = ?",
            selectionArgs, null, null, null)

        val returnIds = mutableSetOf<Int>()
        var index = c.getColumnIndex(ClassTable.STUDENT_ID)
        if (index != -1) {
            while (c.moveToNext()) {
                returnIds.add(c.getInt(index))
            }
        }

        // Make second query
        cols = arrayOf( StudentTable.ID )
        selectionArgs = arrayOf( grade.toString() )

        c = readableDatabase.query(StudentTable.TABLE_NAME, cols, "${StudentTable.GRADE} = ?",
            selectionArgs, null, null, null)
        val gradeIds = mutableSetOf<Int>()
        index = c.getColumnIndex(StudentTable.ID)
        if (index != -1) {
            while (c.moveToNext()) {
                gradeIds.add(c.getInt(index))
            }
        }

        // Return intersection of id sets
        returnIds.retainAll(gradeIds)

        return returnIds
    }

    // Method for safely removing a studeng
    fun removeStudent(studentId: Int): Boolean {
        val whereArgs = arrayOf( studentId.toString() )
        // Delete all class mappings student is signed up for
        writableDatabase.delete(ClassTable.TABLE_NAME, "${ClassTable.STUDENT_ID} = ?", whereArgs)

        // Then delete student
        return writableDatabase.delete(StudentTable.TABLE_NAME, "${StudentTable.ID} = ?", whereArgs) > 0
    }

    // Method for safely removing a student
    fun removeCourse(courseId: Int): Boolean {
        val whereArgs = arrayOf( courseId.toString() )
        // Make sure you remove course from all students enrolled
        writableDatabase.delete(ClassTable.TABLE_NAME, "${ClassTable.COURSE_ID} = ?", whereArgs)

        // The delete course
        return writableDatabase.delete(CourseTable.TABLE_NAME, "${CourseTable.ID} = ?", whereArgs) > 0
    }

}
```

#### 1.5 SchemaActivity.kt

```kotlin
package com.android.advancedsqlite

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

private const val TAG = "SchemaActivity"

class SchemaActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val sh = SchemaHelper(this)

        // Add students and return their IDs
        val sid1 = sh.addStudent("Jason Wei", "IL", 12)
        val sid2 = sh.addStudent("Du Chung", "AR", 12)
        val sid3 = sh.addStudent("George Tang", "CA", 11)
        val sid4 = sh.addStudent("Mark Bocanegra", "CA", 11)
        val sid5 = sh.addStudent("Bobby Wei", "IL", 12)

        // Add courses and return their IDs
        val cid1 = sh.addCourse("Math51")
        val cid2 = sh.addCourse("CS106A")
        val cid3 = sh.addCourse("Econ1A")

        // Enroll students in classes
        sh.enrollStudentClass(sid1.toInt(), cid1.toInt())
        sh.enrollStudentClass(sid1.toInt(), cid2.toInt())
        sh.enrollStudentClass(sid2.toInt(), cid2.toInt())
        sh.enrollStudentClass(sid3.toInt(), cid1.toInt())
        sh.enrollStudentClass(sid3.toInt(), cid2.toInt())
        sh.enrollStudentClass(sid4.toInt(), cid3.toInt())
        sh.enrollStudentClass(sid5.toInt(), cid2.toInt())

        // Get students for course
        var c = sh.getStudentsForCourse(cid2.toInt())
        var colid = c.getColumnIndex(ClassTable.STUDENT_ID)
        if (colid != -1) {
            while (c.moveToNext()) {
                val sid = c.getInt(colid)
                Log.d(TAG, "onCreate=>Student $sid is enrolled in course $cid2")
            }
        }
        // Get students for course and filter by grade
        val sids = sh.getStudentsByGradeForCourse(cid2.toInt(), 11)
        for (sid in sids) {
            Log.d(TAG, "onCreate=>Student $sid of grade 11 is enrolled in course $cid2")
        }

        // Get Classes I'm Taking
        c = sh.getCoursesForStudent(sid1.toInt())
        colid = c.getColumnIndex(ClassTable.COURSE_ID)
        if (colid != -1) {
            while (c.moveToNext()) {
                val cid = c.getInt(colid);
                Log.d(TAG, "onCreate=>Student $sid1 is enrolled in course $cid")
            }
        }

        // Try removing a course
        sh.removeCourse(cid1.toInt())

        Log.d(TAG, "onCreate=>===================================================")

        // Set if removal kept schema consistent
        c = sh.getCoursesForStudent(sid1.toInt())
        colid = c.getColumnIndex(ClassTable.COURSE_ID)
        if (colid != -1) {
            while (c.moveToNext()) {
                val cid = c.getInt(colid)
                Log.d(TAG, "onCreate=>Student $sid1 is enrolled in course $cid")
            }
        }
    }

}
```

### 2. Java 版本

#### 1.1 StudentTable.java

```java
package com.android.advancedsqlite;

public class StudentTable {

    // Each student has unique id
    public static final String ID = "_id";

    // Name of the student
    public static final String NAME = "student_name";

    // State of student's residence
    public static final String STATE = "state";

    // Grade in school of student
    public static final String GRADE = "grade";

    // Name of the table
    public static final String TABLE_NAME = "students";
}
```

#### 1.2 CourseTable.java

```java
package com.android.advancedsqlite;

public class CourseTable {

    // Unique id of the course
    public static final String ID = "_id";

    // Name of the course
    public static final String NAME= "course_name";

    // Name of the table
    public static final String TABLE_NAME = "courses";
}
```

#### 1.3 ClassTable.java

```java
package com.android.advancedsqlite;

// This essentially represents a mapping from students to courses
public class ClassTable {

    // Unique id of each row - No real meaning here
    public static final String ID = "_id";

    // The id of the student
    public static final String STUDENT_ID = "student_id";

    // The id of associated course
    public static final String COURSE_ID = "course_id";

    // The name of the table
    public static final String TABLE_NAME = "classes";
}
```

#### 1.4 SchemaHelper.java

```java
package com.android.advancedsqlite;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.media.audiofx.AcousticEchoCanceler;
import android.util.Log;

import java.util.HashSet;
import java.util.Set;

public class SchemaHelper extends SQLiteOpenHelper {

    private static final String TAG = "SchemaHelper";
    private static final String DATABASE_NAME = "adv_data.db";

    // Toggle this number for updating tables and database
    private static final int DATABASE_VERSION = 1;

    public SchemaHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create students table
        db.execSQL("CREATE TABLE " + StudentTable.TABLE_NAME + " (" + StudentTable.ID
                + " INTEGER PRIMARY KEY AUTOINCREMENT," + StudentTable.NAME + " TEXT,"
                + StudentTable.STATE + " TEXT," + StudentTable.GRADE + " INTEGER);");
        // Create courses table
        db.execSQL("CREATE TABLE " + CourseTable.TABLE_NAME + " (" + CourseTable.ID
                + " INTEGER PRIMARY KEY AUTOINCREMENT," + CourseTable.NAME + " TEXT);");
        // Create classes mapping table
        db.execSQL("CREATE TABLE " +ClassTable.TABLE_NAME + " (" + ClassTable.ID
                + " INTEGER PRIMARY KEY AUTOINCREMENT," + ClassTable.STUDENT_ID
                + " INTEGER," + ClassTable.COURSE_ID + " INTEGER);");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        Log.w(TAG, "Upgrading database from version " + oldVersion + " to "
                + newVersion + ", which will destroy all old data");
        // Kill previous tables if upgraded
        db.execSQL("DROP TABLE IF EXISTS " + StudentTable.TABLE_NAME);
        db.execSQL("DROP TABLE IF EXISTS " + CourseTable.TABLE_NAME);
        db.execSQL("DROP TABLE IF EXISTS " + ClassTable.TABLE_NAME);

        // Create new instance of schema
        onCreate(db);
    }

    // Wrapper method for adding a student
    public long addStudent(String name, String state, int grade) {
        // Create a contentvalue object
        ContentValues cv = new ContentValues();
        cv.put(StudentTable.NAME, name);
        cv.put(StudentTable.STATE, state);
        cv.put(StudentTable.GRADE, grade);

        // Retrieve writeable database and insert
        SQLiteDatabase db = getWritableDatabase();
        long result = db.insert(StudentTable.TABLE_NAME, StudentTable.NAME, cv);
        return result;
    }

    // Wrapper method for adding a course
    public long addCourse(String name) {
        ContentValues cv = new ContentValues();
        cv.put(CourseTable.NAME, name);

        SQLiteDatabase db = getWritableDatabase();
        long result = db.insert(CourseTable.TABLE_NAME, CourseTable.NAME, cv);
        return result;
    }

    // Wrapper method for enrolling a student into a course
    public boolean enrollStudentClass(int studentId, int courseId) {
        ContentValues cv = new ContentValues();
        cv.put(ClassTable.STUDENT_ID, studentId);
        cv.put(ClassTable.COURSE_ID, courseId);

        SQLiteDatabase db = getWritableDatabase();
        long result = db.insert(ClassTable.TABLE_NAME, ClassTable.STUDENT_ID, cv);
        return (result >= 0);
    }

    // Get all students in a course
    public Cursor getStudentsForCourse(int courseId) {
        SQLiteDatabase db = getReadableDatabase();

        // We only need to return student ids
        String[] cols = new String[] { ClassTable.STUDENT_ID };

        String[] selectionArgs = new String[] { String.valueOf(courseId) };

        // Query class map for students in course
        Cursor c = db.query(ClassTable.TABLE_NAME, cols, ClassTable.COURSE_ID + "= ?",
                selectionArgs, null, null, null);

        return c;
    }

    // Get all courses for a given student
    public Cursor getCoursesForStudent(int studentId) {
        SQLiteDatabase db = getReadableDatabase();

        // We only need to return course ids
        String[] cols = new String[] { ClassTable.COURSE_ID };

        String[] selectionArgs = new String[] { String.valueOf(studentId) };

        Cursor c = db.query(ClassTable.TABLE_NAME, cols, ClassTable.STUDENT_ID + "= ?",
                selectionArgs, null, null, null);

        return c;
    }

    public Set<Integer> getStudentsByGradeForCourse(int courseId, int grade) {
        SQLiteDatabase db = getReadableDatabase();

        // We only need to return course ids
        String[] cols = new String[] { ClassTable.STUDENT_ID };

        String[] selectionArgs = new String[] { String.valueOf(courseId) };

        // Query class map for students in course
        Cursor c = db.query(ClassTable.TABLE_NAME, cols, ClassTable.COURSE_ID + "= ?",
                selectionArgs, null, null, null);

        Set<Integer> returnIds = new HashSet<>();
        int studentIdIndex = c.getColumnIndex(StudentTable.ID);
        if (studentIdIndex != -1) {
            while (c.moveToNext()) {
                int id = c.getInt(studentIdIndex);
                returnIds.add(id);
            }
        }

        // Make second query
        cols = new String[] { StudentTable.ID };
        selectionArgs = new String[] { String.valueOf(grade) };

        c = db.query(StudentTable.TABLE_NAME, cols, StudentTable.GRADE + "= ?",
                selectionArgs, null, null, null);
        Set<Integer> gradeIds = new HashSet<>();
        studentIdIndex = c.getColumnIndex(StudentTable.ID);
        if (studentIdIndex != -1) {
            while (c.moveToNext()) {
                int id = c.getInt(studentIdIndex);
                gradeIds.add(id);
            }
        }

        // Return intersection of id sets
        returnIds.retainAll(gradeIds);

        return returnIds;
    }

    // Method for safely removing a student
    public boolean removeStudent(int studentId) {
        SQLiteDatabase db = getWritableDatabase();
        String[] whereArgs = new String[] { String.valueOf(studentId) };

        // Delete all class mappings student is signed up for
        db.delete(ClassTable.TABLE_NAME, ClassTable.STUDENT_ID + "= ?", whereArgs);

        // The delete student
        int result = db.delete(StudentTable.TABLE_NAME, StudentTable.ID + "= ?", whereArgs);
        return (result > 0);
    }

    // Method for safely removing a student
    public boolean removeCourse(int courseId) {
        SQLiteDatabase db = getWritableDatabase();
        String[] whereArgs = new String[] { String.valueOf(courseId) };

        // Delete all class mappings student is signed up for
        db.delete(ClassTable.TABLE_NAME, ClassTable.STUDENT_ID + "= ?", whereArgs);

        // Then delete student
        int result = db.delete(StudentTable.TABLE_NAME, StudentTable.ID + "= ?", whereArgs);
        return (result > 0);
    }

}
```

#### 1.5 SchemaActivity.java

```java
package com.android.advancedsqlite;

import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.os.Bundle;
import android.util.Log;

import java.util.Set;

public class SchemaActivity extends AppCompatActivity {

    private static final String TAG = "SchemaActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SchemaHelper sh = new SchemaHelper(this);

        // Add student and return their ids
        long sid1 = sh.addStudent("Jason Wei", "IL", 12);
        long sid2 = sh.addStudent("Du Chung", "AR", 12);
        long sid3 = sh.addStudent("George Tang", "CA", 11);
        long sid4 = sh.addStudent("Mark Bocanegra", "CA", 11);
        long sid5 = sh.addStudent("Bobby Wei", "IL", 12);

        // Add courses and return their ids
        long cid1 = sh.addCourse("Math51");
        long cid2 = sh.addCourse("CS106A");
        long cid3 = sh.addCourse("Econ1A");

        // Enroll student in classes
        sh.enrollStudentClass((int) sid1, (int) cid1);
        sh.enrollStudentClass((int) sid1, (int) cid2);
        sh.enrollStudentClass((int) sid2, (int) cid2);
        sh.enrollStudentClass((int) sid3, (int) cid1);
        sh.enrollStudentClass((int) sid3, (int) cid2);
        sh.enrollStudentClass((int) sid4, (int) cid3);
        sh.enrollStudentClass((int) sid5, (int) cid2);

        // get students for course
        Cursor c = sh.getStudentsForCourse((int) cid2);
        int studentIndex = c.getColumnIndex(ClassTable.STUDENT_ID);
        if (studentIndex != -1) {
            while (c.moveToNext()) {
                int sid = c.getInt(studentIndex);
                Log.d(TAG, "onCreate=>Student " + sid + " is enrolled in course " + cid2);
            }
        }
        // Get students for course and filter by grade
        Set<Integer> sids = sh.getStudentsByGradeForCourse((int) cid2, 11);
        for (Integer sid : sids) {
            Log.d(TAG, "onCreate=>Student " + sid + " of grade 11 is enrolled in course " + cid2);
        }
        // Get Classes I'm taking
        c = sh.getCoursesForStudent((int) sid1);
        int courseIdIndex = c.getColumnIndex(ClassTable.COURSE_ID);
        if (courseIdIndex != -1) {
            int cid = c.getInt(courseIdIndex);
            Log.d(TAG, "onCreate=>Student " + sid1 + " is enrolled in course " + cid);
        }

        // Try removing a course
        sh.removeCourse((int) cid1);

        Log.d(TAG, "onCreate=>====================================================");
        // See if removal kept schema consistent
        c = sh.getCoursesForStudent((int) sid1);
        courseIdIndex = c.getColumnIndex(ClassTable.COURSE_ID);
        if (courseIdIndex != -1) {
            while (c.moveToNext()) {
                int cid = c.getInt(courseIdIndex);
                Log.d(TAG, "onCreate=>Student " + sid1 + " is enrolled in course " + cid);
            }
        }
    }
}
```