`setTimeout` 函数需要传入一个回调函数作为第一个参数，第二个参数为延迟时间（以毫秒为单位），以及一个可选参数列表：

```js
// timer to open file and read contents to HTTP response object
function openAndReadFile(filename, res) {
    console.log('opening ' + filename)
    // open and read in file contents
    fs.readFile(filename, 'utf8', (err, data) => {
        if (err) {
            res.write('Could not find or open file for reading\n')
        } else {
            res.write(data)
        }
        // reponse is done
        res.end()
    })
}

setTimeout(openAndReadFile, 2000, filename, res)
```

函数 `clearTimeout` 可以清除通过 `setTimeout` 预设的定时器。

可以使用 `setInterval` 函数来设置时间间隔，在每隔 n 毫秒（n 是传递给函数的第二个参数）后调用一个回调函数（第一个参数）。函数 `clearInterval` 可以用来清除时间间隔设置。