今天要说的是 Amlogic 平台的 property_service.c 文件的修改点，它位于 system/core/init/property_service.c 下。

首先是添加属性修改白名单：

```c
/* White list of permissions for setting property services. */
struct {
    const char *prefix;
    unsigned int uid;
    unsigned int gid;
} property_perms[] = {
    ......
    { "net.dhcp.",            AID_DHCP,     0 },
    ......
    { "libplayer.tcp.",	    AID_MEDIA,    0 },
    ......
};
```

项目添加了上面两个白名单，以这两个字符串开头的属性在设置值时，将会受到权限的限制。

第二个修改就是根据 mac 地址设置 ro.stb.manu 属性的值:

```c
void start_property_service(void)
{
    int fd;
    char mac[PROP_VALUE_MAX];
    int ret;

    load_properties_from_file(PROP_PATH_SYSTEM_BUILD);
    load_properties_from_file(PROP_PATH_SYSTEM_DEFAULT);
    load_override_properties();
    /* Read persistent properties after all default values have been loaded. */
    load_persistent_properties();

    fd = create_socket(PROP_SERVICE_NAME, SOCK_STREAM, 0666, 0, 0);
    if(fd < 0) return;
    fcntl(fd, F_SETFD, FD_CLOEXEC);
    fcntl(fd, F_SETFL, O_NONBLOCK);

    listen(fd, 8);
    property_set_fd = fd;
    set_properties_from_unifykey();



    ret = property_get("ro.mac", mac);
	if(ret &&  (strstr(mac, "00:E4:00") || strstr(mac, "84:2C:80") || strstr(mac, "C0:13:2B") )) {
        property_set("ro.stb.manu", "ch");
	}
	else
        property_set("ro.stb.manu", "zg");
}
```

其实还有一处修改，就是在 start_property_service() 方法中添加了 set_properties_from_unifykey() 方法的调用。该方法会调用 swunifykey.c 中的 sw_unifykey_set_properties 方法。其实现代码位于 device/sunniwell/system/core/swunifykey/swunifykey.c 文件中：

```c
int sw_unifykey_set_properties(void)
{
	if( m_init != 1 ) {
		if( unifykey_init() != 0 )
			return -1;
	}
    
	int ret;
	int fd = open( UNIFYKEY_LIST_NODE, O_RDONLY, 0644 );
    if( fd < 0 ) {
        sw_log_error( "error: could not open '%s'\n", UNIFYKEY_LIST_NODE );
        return -1;
    }
	sw_log_info( "unifykey list:\n" );
	
	char buf[1024] = {0};
	char prop[PROP_NAME_MAX];
	char value[PROP_VALUE_MAX] = {0};
	char * name;
	char * name_end;
	while( readline( fd, buf, 1024 ) > 0 ) {
		name = strstr( buf, ": " );
		if ( name == NULL ) {
			continue;
		} else {
			name = name + 2;
		}
		name_end = strstr( buf, ",");
		if ( name_end != NULL )
			name_end[0] = '\0';

		ret = sw_unifykey_value_get( name, value, sizeof(value), NULL );
		sw_log_info( "name %s value %s\n", name, value );
		if( ret != -1 ) {
			memset(prop, 0, sizeof(prop));
			snprintf(prop, sizeof(prop), "ro.%s", name);
			property_set(prop, value);
		} else {
			sw_log_error("failed to get value!!\n");
			break;
		}

		memset( buf, 0, sizeof(buf) );
		memset( value, 0, sizeof(value) );
	}

	return ret;
}
```

它的功能是读取设备 /sys/class/unifykeys/list 文件中的内容，将其内容以 ro. 属性的形式写入到系统属性中。