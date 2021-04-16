### 21.2.2 实例：PCI骨架程序

drivers/net/pci-skeleton.c给出了一个PCI接口网络设备驱动程序的“骨架”，其pci_driver中probe()成员函数netdrv_init_one()及其调用的netdrv_init_board()完成了PCI设备初始化及对应的网络设备注册工作，代码清单21.8所示为这两个函数的实现。

代码清单21.8 pci-skeleton设备驱动的probe()函数

1 static int __devinit netdrv_init_one (struct pci_dev *pdev, 
 
 2 const struct pci_device_id *ent) 
 
 3 { 
 
 4 struct net_device *dev = NULL; 
 
 5 struct netdrv_private *tp; 
 
 6 ... 
 
 7 i = netdrv_init_board (pdev, &dev, &ioaddr); 
 
 8 ... 
 
 9 
 
 10 dev→open = netdrv_open; 
 
 11 dev→hard_start_xmit = netdrv_start_xmit; 
 
 12 dev→stop = netdrv_close; 
 
 13 dev→set_multicast_list = netdrv_set_rx_mode; 
 
 14 dev→do_ioctl = netdrv_ioctl; 
 
 15 dev→tx_timeout = netdrv_tx_timeout; 
 
 16 dev→watchdog_timeo = TX_TIMEOUT; 
 
 17



18 dev→irq = pdev→irq; 
 
 19 dev→base_addr = (unsigned long) ioaddr; 
 
 20 
 
 21 tp = netdev_priv(dev); 
 
 22 
 
 23 ... 
 
 24 pci_set_drvdata(pdev, dev); 
 
 25 ... 
 
 26 return 0; 
 
 27 } 
 
 28 
 
 29 static int __devinit netdrv_init_board (struct pci_dev *pdev, 
 
 30 struct net_device **dev_out, 
 
 31 void **ioaddr_out) 
 
 32 { 
 
 33 ... 
 
 34 dev = alloc_etherdev (sizeof (*tp)); 
 
 35 if (dev == NULL) { 
 
 36 dev_err(&pdev→dev, "unable to alloc new ethernet\n"); 
 
 37 DPRINTK ("EXIT, returning -ENOMEM\n"); 
 
 38 return -ENOMEM; 
 
 39 } 
 
 40 SET_NETDEV_DEV(dev, &pdev→dev); 
 
 41 tp = netdev_priv(dev); 
 
 42 ... 
 
 43 }

从上述代码可以看出，probe()函数中进行了网络设备的初始化和注册。pci_driver的remove()成员函数完成相反的工作，即注销网络设备，如代码清单21.9所示。

代码清单21.9 pci-skeleton设备驱动的remove()函数

1 static void __devexit netdrv_remove_one (struct pci_dev *pdev) 
 
 2 { 
 
 3 struct net_device *dev = pci_get_drvdata (pdev); 
 
 4 struct netdrv_private *np; 
 
 5 
 
 6 ... 
 
 7 np = netdev_priv(dev); 
 
 8 assert (np != NULL); 
 
 9 
 
 10 unregister_netdev (dev); 
 
 11 
 
 12 #ifndef USE_IO_OPS 
 
 13 iounmap (np→mmio_addr); 
 
 14 #endif /* !USE_IO_OPS */ 
 
 15 
 
 16 pci_release_regions (pdev); 
 
 17 
 
 18 free_netdev (dev); 
 
 19 
 
 20 pci_set_drvdata (pdev, NULL); 
 
 21 
 
 22 pci_disable_device (pdev); 
 
 23 
 
 24 DPRINTK ("EXIT\n"); 
 
 25 }

/drivers/net/pci-skeleton.c中定义的pci_device_id结构体数组及MODULE_DEVICE_TABLE导出代码如清单21.10所示。

代码清单21.10 PCI设备驱动的pci_device_id数组及MODULE_DEVICE_TABLE

1 static struct pci_device_id netdrv_pci_tbl[] = { 
 
 2 {0x10ec, 0x8139, PCI_ANY_ID, PCI_ANY_ID, 0, 0, RTL8139 }, 
 
 3 {0x10ec, 0x8138, PCI_ANY_ID, PCI_ANY_ID, 0, 0, NETDRV_CB }, 
 
 4 {0x1113, 0x1211, PCI_ANY_ID, PCI_ANY_ID, 0, 0, SMC1211TX }, 
 
 5 /* {0x1113, 0x1211, PCI_ANY_ID, PCI_ANY_ID, 0, 0, MPX5030 },*/ 
 
 6 {0x1500, 0x1360, PCI_ANY_ID, PCI_ANY_ID, 0, 0, DELTA8139 }, 
 
 7 {0x4033, 0x1360, PCI_ANY_ID, PCI_ANY_ID, 0, 0, ADDTRON8139 }, 
 
 8 {0,} 
 
 9 }; 
 
 10 MODULE_DEVICE_TABLE (pci, netdrv_pci_tbl);

除此之外，pci-skeleton的主体即是完成网络设备驱动相关的工作，完全符合本书第6章的模板。

