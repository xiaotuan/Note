你可能已在 Android 参考文档中注意到了 `MotionEvent` 类的 `recycle()` 方法。你可能希望回收在 `onTouch()` 或 `onTouchEvent()` 中收到的 `MotionEvent`，但请不要这么做。如果回调方法没有使用 `MotionEvent` 对象，并且你返回了 false，`MotionEvent` 对象可能会传递到其他某个方法、视图或我们的活动，所以你还不希望 Android 回收它。即使使用了该事件并返回了 true，该事件对象不属于你，也不应回收它。

如果查看 `MotionEvent`，将会看到方法 `obtain()` 的一些变体。它们创建一个 `MotionEvent` 的副本或全新的 `MotionEvent`。你的副本或全新的事件对象是再完成之后应该回收的对象。例如，如果希望找到通过回调传递给你的事件对象，应该使用 `obtain()` 来创建副本，因为从回调返回后，该时间对象就会由 Android 回收，如果继续使用它，可能会得到奇怪的结果。当完成副本的使用之后，调用它的 `recycle()`。

