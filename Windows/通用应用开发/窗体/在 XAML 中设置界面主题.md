可以在 `Page` 节点中添加 `RequestedTheme` 属性，该属性只有三个值 `Default`、`Dark` 和 `Light`。例如：

```xml
<Page
    x:Class="App2.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:local="using:App2"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    RequestedTheme="Dark"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">

    <Grid Name="contentGrid">
        <TextBlock Text="Hello, Windows 8!"
                   Foreground="Red"
                   HorizontalAlignment="Center"
                   VerticalAlignment="Center" />
    </Grid>

</Page>
```

