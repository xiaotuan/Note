

为了统一字符编码，国际标准化组织 ISO（International Organization for Standardization）的一些成员国于 1984 年发起制定新的国际字符集标准，以容纳全世界各种语言文字和符号。这个标准最后叫做“Universal Multiple-Octet Coded Character Set”，简称UCS，标准编号则定为ISO-10646。ISO-10646标准采用4字节（32bit）编码，因此简称UCS-4。具体编码规则是：将代码空间划分为组（group）、面（plane）、行（row）和格（ceil）；第1个字节代表组（group），第2个字节代表面（plane），第3个字节代表行（row），第4个字节代表格（ceil），并规定字符编码的第32位必须为0，且每个面（plane）的最后两个码位FFFEh和FFFFh保留不用；因此，ISO-1064共有128个群组（0～0x7F），每个群组有256个字面（00～0xFF），每个字面有256行（00～0xFF），每行包括 256格（0～0xFF），共有 256×128=32 768个字面，每个字面有256×256-2=65 534个码位，合计 65534×32768=2 147 418 112个码位。

ISO-10646发布以后，遭到了部分美国计算机公司的反对。1988年Xerox公司提议制定新的以16位编码的统一字符集Unicode，并联合Apple、IBM、DEC、Sun、Microsoft、Novell等公司成立Unicode协会（The Unicode Consortium），并成立Unicode技术委员会（Unicode Technical Committee），专门负责Unicode文字的搜集、整理和编码，并于1991年推出了Unicode 1.0。

都是为了解决字符编码统一问题，ISO和Unicode协会却推出了两个不同的编码标准，这显然是不利的。后来，大家都认识到了这一点，经过双方谈判，1991年10月达成协议，ISO将Unicode编码并入 ISO-10646的0组0字面，叫做**基本多语言文字面**（Basic Multi-lingual Plane， BMP），共有 65 534个码位，并根据不同用途分为若干区域。除BMP外的 32 767个字面又分为**辅助字面**（supplementary planes）和**专用字面**（private use planes）两部分，辅助字面用以收录ISO-10646后续搜集的各国文字，专用字面供使用者自定义收录ISO-10646未收录的文字符号。其实，大部分用户只使用BMP字面就足够了，早期的ISO-10646-1标准也只要求实现BMP字面，这样只需要2字节来编码就足够了，Unicode也正是这么做的，这叫做ISO-10646编码的基本面形式，简称为UCS-2编码，UCS-2编码转换成UCS-4编码也很容易，只要在前面加两个取值为0的字节即可。

ISO-10646 的编码空间足以容纳人类从古至今使用过的所有文字和符号，但其实许多文字符号都已经很少使用了，超过 99%的在用文字符号都编入了 BMP，因此，绝大部分情况下， Unicode的双字节编码方式都能满足需求，而这种双字节编码方式比起ISO-10646的4字节原始编码来说，在节省内存和处理时间上都具有优势，这也是Unicode编码方式更流行的原因。但如果万一要使用 ISO-10646 BMP字面以外的文字怎么办呢？Unicode提出了名为UTF-16或代理法（surrogates）的解决方案，UTF是UCS/Unicode Transformation Format 的缩写。UTF-16的解决办法是：对BMP字面的编码保持二字节不变，对其他字面的文字按一定规则将其32位编码转换为两个16位的Unicode编码，其两个字节的取值范围分别限定为0xD800～0xDBFF和 0xDC00～0xDFFF，因此，UTF-16共有（4×256）×（4×256）＝1 048 576个码位。

虽然UTF-16解决了ISO-10646除BMP外第1～15字面的编码问题，但当时的计算机和网络世界还是ASCII的天下，只能处理单字节数据流，UTF-16在离开Unicode环境后，在传输和处理中都存在问题。于是Unicode又提出了名为UTF-8的解决方案，UTF-8按一定规则将一个ISO-10646或Unicode字元码转换成1～4个字节的编码，其中将ASCII码（0～0x7F）转换成单字节编码，也就是严格兼容ASCII字符集；UTF-8的2字节编码，用以转换ISO-10646标准 0x0080～0x07FF的UCS-4原始码；UTF-8的3字节编码，用以转换 ISO-10646标准0x0800～0xFFFF 的 UCS-4 原始码；UTF-8 的 4 字节编码，用以转换 ISO-10646 标准 0x00010000～0001FFFF的UCS-4原始码。

上述各种编码方式，看起来有点让人迷惑。其实，ISO-10646 只是给每一个文字符号分配了一个4字节无符号整数编号（UCS-4），并未规定在计算机中如何去表示这个无符号整数编号。UTF-16和UTF-8就是其两种变通表示方式。

ISO-10646与Unicode统一以后，两个组织虽然都继续发布各自的标准，但二者之间是一致的。由于Unicode最早投入应用，其编码方式更加普及，因此，许多人都知道Unicode，但对ISO-10646却了解不多。但由于二者是一致的，因此，区分ISO-10646和Unicode的意义也就不大了。现在，人们说Unicode和ISO-10646，一般指的是同一个东西，只是Unicode更直接、更普及罢了。二者不同版本的对应关系如下。

Unicode 2.0等同于 ISO/IEC 10646-1:1993。

Unicode 3.0等同于 ISO/IEC 10646-1:2000。

Unicode 4.0等同于 ISO/IEC 10646:2003。

最后要说的是，UTF-16和 UTF-32因字节序的不同，又有了 UTF-16BE（Big Endian）、UTF-16LE（Little Endian）和UTF-32BE（Big Endian）、UTF-32LE（Little Endian）等，在此不做进一步介绍。



