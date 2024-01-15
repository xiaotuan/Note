1. 通过 `@JsonIgnore` 注解忽略类实例域

   ```java
   import com.alibaba.fastjson.annotation.JSONField;
   import com.fasterxml.jackson.annotation.JsonIgnore;
   
   import java.util.Date;
   
   public class Book {
   
       private String name;
       private String author;
       @JsonIgnore
       private Float price;
       @JSONField(format = "yyyy-MM-dd")
       private Date publicationDate;
    	// 省略 getter/setter   
   }
   ```

2. 通过 `@JSONField(serialize = false)` 注解忽略类实例域

   ```java
   import com.alibaba.fastjson.annotation.JSONField;
   import com.fasterxml.jackson.annotation.JsonIgnore;
   
   import java.util.Date;
   
   public class Book {
   
       private String name;
       private String author;
       @JSONField(serialize = false)
       private Float price;
       @JSONField(format = "yyyy-MM-dd")
       private Date publicationDate;
    	// 省略 getter/setter   
   }
   ```

   