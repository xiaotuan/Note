下面以 Sensor 传感器为例：

+ Native code 通过 `hw_get_module` 调用获取 HAL stub。

  ```c
  hw_get_module(LED_HARDWARE_MODULE_ID, (const hw_module_t**)$module)
  ```

+ 通过继承 `hw_module_methods_t` 的 callback 来打开设备。

  ```c
  module->methods->open(module, LED_HARDWARE_MODULE_ID, (struct hw_device_t**)device);
  ```

+ 通过继承 `hw_device_t` 的 callback 来控制设备。

  ```c
  sLedDevice->set_on(sLedDevice, led);
  sLedDevice->set_off(sLedDevice, led);
  ```

  

