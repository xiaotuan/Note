一个页面只有一个部分代表其主要内容。可以将这样的内容包在 `main` 元素中，该元素在一个页面仅使用一次。

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Marking the Main Area of a Webpage</title>
    </head>
    <body>
        <header role="banner">
            <nav role="navigation">
                <ul>
                    <li><a href="#gaudi">Barcelona's Architect</a></li>
                    <li lang="es"><a href="#sagrada-familia">La Sagrada Família</a></li>
                    <li><a href="#park-guell">Park Guell</a></li>
                </ul>
            </nav>
        </header>

        <!-- ==== START MAIN ==== -->
        <main role="main">
            <article>
                <h1 id="gaudi">Barcelona's Architect</h1>

                <p>Antoni Gaudí's incredible buildings bring millions ...</p>

                ... [rest of main page content] ...
            </article>
        </main>
        <!-- end main -->

        <aside role="complementary">
            <h1>Architectural Wonders of Barcelona</h1>

            ... [rest of aside] ...
        </aside>

        <footer role="contentinfo">
            ... [copyright] ...
        </footer>
    </body>
</html>
```

最好在 `main` 开始标签中加上 `role="main"`。

> 不能将 `main` 放置在 `article`、`aside`、`footer`、`header` 或 `nav` 元素中。