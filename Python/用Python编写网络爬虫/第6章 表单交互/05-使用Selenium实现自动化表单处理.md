[toc]

### 6.3　使用Selenium实现自动化表单处理

尽管我们的例子现在已经可以正常运行了，但是我们会发现每个表单都需要大量的工作和测试。我们可以使用第5章中介绍的Selenium减轻这方面的工作。由于Selenium是基于浏览器的解决方案，因此它可以模拟许多用户交互操作，包括点击、滚动以及输入。如果你通过类似PhantomJS的无界面浏览器使用Selenium，那么你还能并行及扩展你的处理过程，因为它比完整浏览器的开销要更少一些。

> <img class="my_markdown" src="../images/55.jpg" style="zoom:50%;" />
> 使用完整的浏览器对于“人类化”交互来说同样是个很好的解决方案，尤其是当你使用的是知名浏览器，或类似浏览器的头部时，可以将你与其他更像机器人的标识区分开。

使用Selenium重写我们的登录和编辑脚本相当简单，不过我们必须先查看页面，找到要使用的CSS或XPath标识。通过浏览器工具进行该操作时，我们将会注意到对于登录表单和国家（或地区）编辑表单来说，登录表单拥有易于识别的CSS ID。现在，我们可以使用Selenium重写登录和编辑功能。

首先，编写获取驱动以及登录的方法。

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_driver():
    try:
        return webdriver.PhantomJS()
    except Exception:
        return webdriver.Firefox()
def login(driver):
    driver.get(LOGIN_URL)
    driver.find_element_by_id('auth_user_email').send_keys(LOGIN_EMAIL)
    driver.find_element_by_id('auth_user_password').send_keys(
        LOGIN_PASSWORD + Keys.RETURN)
    pg_loaded = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "results")))
    assert 'login' not in driver.current_url
```

在这里， `get_driver` 函数先尝试获得PhantomJS的驱动，因为它速度更快，并且在服务器上安装更加容易。如果获取失败，则使用Firefox。 `login` 函数使用作为参数传递的 `driver` 对象，并使用浏览器驱动在第一次加载页面时登录，然后使用驱动的 `send_keys` 方法向识别出的待输入元素中写入内容。 `Keys.RETURN` 发送的是回车键的信号，在许多表单中该键都会被映射为提交表单。

我们还使用了Selenium的显式等待（ `WebDriverWait` 以及表示期望条件的 `EC` ），这样我们可以告知浏览器进行等待，直到遇到指定的元素或条件。在本例中，我们知道登录后的主页显示中包含ID为“ `results` ”的CSS元素。 `WebDriverWait` 对象将会为该元素的加载等待10秒钟的时间，超过该时间后抛出异常。我们可以很容易地关闭该等待，或是使用其他期望条件来匹配我们当前加载的页面行为。

> <img class="my_markdown" src="../images/56.jpg" style="zoom:50%;" />
> 想要了解更多关于Selenium显式等待的知识，我推荐你阅读其Python版本的文档，地址为 `http://selenium-python.readthedocs.io/waits.html` 。显式等待优于隐式等待，因为你可以明确告知Selenium你想要等待的是什么，并且可以确保你希望交互的页面部分已经被加载。

既然我们已经获得了Web驱动，并且成功登录网站，那么此时我们希望可以与表单进行交互，修改人口数量。

```python
def add_population(driver):
    driver.get(COUNTRY_OR_DISTRICT_URL)
    population = driver.find_element_by_id('places_population')
    new_population = int(population.get_attribute('value')) + 1
    population.clear()
    population.send_keys(new_population)
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    pg_loaded = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "places_population__row")))
    test_population = int(driver.find_element_by_css_selector(
        '#places_population__row .w2p_fw').text.replace(',', ''))
    assert test_population == new_population
```

这里有关Selenium使用的唯一新功能是 `clear` 方法，它用于清空表单的输入值（而不是在输入域结尾处添加）。我们还使用了元素的 `get_attribute` 方法，从页面的HTML元素中获得指定的属性。因为我们正在处理的是HTML的 `input` 元素，因此我们需要得到 `value` 属性，而不是检查 `text` 属性。

现在我们已经实现了使用Selenium将人口数量加1的所有方法，下面我们可以运行该脚本，类似如下所示。

```python
>>> driver = get_driver()
>>> login(driver)
>>> add_population(driver)
>>> driver.quit()
```

由于我们的 `assert` 语句通过了，所以我们知道使用这个简单脚本更新人口数量的操作已经成功了。

使用Selenium与表单交互还有很多方式，我鼓励你通过阅读文档以更多地了解。Selenium对那些调试有问题的网站尤其有帮助，因为我们拥有使用它的 `save_screenshot` 方法查看已加载浏览器截图的能力。

