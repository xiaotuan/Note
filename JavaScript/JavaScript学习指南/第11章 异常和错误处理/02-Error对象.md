### 11.1　Error对象

JavaScript有一个内建的Error对象，它可以用来处理任意类型的错误（异常或预期错误）。还可以在创建Error实例的时候提供一些错误信息：

```javascript
const err = new Error('invalid email');
```

创建出的 `Error` 实例本身不会做任何事。它只提供一个传递错误的载体。假设有一个验证邮箱地址的函数。如果验证成功，函数返回字符串格式的邮箱。否则返回一个 `Error` 实例。为了方便起见，把任何包含@符号的东西看做是合法邮箱（见第17章）：

```javascript
function validateEmail(email) {
   return email.match(/@/) ?
      email : 
      new Error('invalid email: ${email}');
}
```

为了使用返回值，可以用 `typeof` 运算符来判断返回的是不是 `Error` 实例。然后通过 `Error` 的 `message` 属性来获取错误信息：

```javascript
const email = "jane@doe.com";
const validatedEmail = validateEmail(email);
if(validatedEmail instanceof Error) {
   console.error(`Error: ${validatedEmail.message});
} else {
   console.log('Valid email: ${validatedEmail}');
}
```

虽然这样使用Error实例完全合法，也很有用，但实际上，它的大部分应用场景都在异常处理中，这也是接下来要讲的内容。

