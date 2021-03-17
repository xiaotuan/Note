```html
<!DOCTYPE html>
<html lang="utf-8">
    <head>
        <title>SPA Chapter 1 section 1.2.5</title>
        <script src="http://libs.baidu.com/jquery/2.1.4/jquery.min.js"></script>

        <style>
            #textarea {
                width: 860px;
                height: 480px;
                border: 1px solid #000;
            }
        </style>
    </head>
    <body>
        <textarea id="textarea"></textarea>

        <script>
            var lastKeyCode = -1;
            var timeoutId = -1;
            var editTimeoutId = -1;
            const textArea = $('#textarea');
            textArea.keyup(function(event){
                if (timeoutId != -1) {
                    clearTimeout(timeoutId);
                }
                if (editTimeoutId != -1) {
                    clearTimeout(editTimeoutId);
                }
                if (event.which == 32) {
                    console.log("html: " + textArea.val());
                } else if (event.which == 229) {
                    timeoutId = setTimeout(function() {
                        if (lastKeyCode == 229) {
                            console.log("html: " + textArea.val());
                        }
                    }, 100);
                    lastKeyCode = event.which;
                } else {
                    editTimeoutId = setTimeout(function() {
                        console.log("html: " + textArea.val());
                    }, 1000);
                }
            });
            
        </script>
    </body>
</html>
```

