在子线程是不能直接对 UI 控件进行操作的，必须在主线程中进行，因此可以使用主线程的 SynchronizationContext .Current 对象的 post() 方法进行操作。如果直接在子线程中使用 SynchronizationContext.Current 对象，将会产生空指针错误，因为在子线程中没有该对象，因此需要将主线程的 SynchronizationContext.Current 对象传递给子线程。由于初学，暂时不知如何传递，但是可以将 SynchronizationContext.Current 对象保存成类的成员变量即可在子线程中使用 SynchronizationContext.Current 了。代码如下：

```vb
Public Class Form1

    Private context As SynchronizationContext
    
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        context = SynchronizationContext.Current
    End Sub

    Private Async Sub btnConnect_ClickAsync(sender As Object, e As EventArgs) Handles btnConnect.Click
        Dim t As Thread = New Thread(AddressOf readData)
        t.Start()
    End Sub

    Private Sub readData()
        ShowThreadInfo("readData")
        serialPort.ReadTimeout = 100
        Do
            If stopRead Then
                Exit Do
            Else
                Try
                    Dim Incomming As String = serialPort.ReadLine()
                    If Incomming IsNot Nothing Then
                        Console.WriteLine(Incomming)
                        context.Post(New SendOrPostCallback(Function(s As String) {addItem(s)}), Incomming)
                    End If
                Catch te As TimeoutException
                Catch ex As Exception
                    Console.WriteLine("Error: " & ex.StackTrace)
                End Try
            End If
        Loop
        Console.WriteLine("read data end.")
    End Sub

    Private Function addItem(s As String)
        lbReceiver.Items.Add(s)
        lbReceiver.TopIndex = lbReceiver.Items.Count - (lbReceiver.Height / lbReceiver.ItemHeight)
    End Function

End Class

```

