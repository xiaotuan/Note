使用 `Pygame` 编写的游戏的基本结构如下：

```python
import sys
import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # 开始游戏的主循环
    while True:
      	# 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
run_game()
```

`pygame.init()` 初始化背景设置，让 `Pygame` 能够正确地工作。调用 `pygame.display.set_mode()` 来创建一个名为 screen 的显示窗口，这个游戏的所有图形元素都将在其中绘制。

对象 `screen` 是一个 `surface`。在 `Pygame` 中，`surface` 是屏幕的一部分，用于显示游戏元素。`display.set_mode()` 返回的 `surface` 表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个 `surface`。

为访问 `Pygame` 检测到的事件，我们使用方法 `pygame.event.get()`。所有鼠标和键盘事件都将促使 `for` 循环运行。

调用 `pygame.display.flip()` 方法命令 `Pygame` 让最近绘制的屏幕可见。