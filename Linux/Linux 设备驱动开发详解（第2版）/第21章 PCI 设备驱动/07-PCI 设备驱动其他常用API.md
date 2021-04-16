### 21.1.5 PCI 设备驱动其他常用API

除了DMA API外，在PCI设备驱动中其他常用的函数（或宏）如下所示。

● 获取I/O或内存资源。

#define pci_resource_start(dev,bar) ((dev)→resource[(bar)].start) 
 
 #define pci_resource_end(dev,bar) ((dev)→resource[(bar)].end) 
 
 #define pci_resource_flags(dev,bar) ((dev)→resource[(bar)].flags) 
 
 #define pci_resource_len(dev,bar) \ 
 
 ((pci_resource_start((dev),(bar)) == 0 && \

pci_resource_end((dev),(bar)) == \ 
 
 pci_resource_start((dev),(bar))) ? 0 : \ 
 
 \ 
 
 (pci_resource_end((dev),(bar)) - \ 
 
 pci_resource_start((dev),(bar)) + 1))

● 申请/释放I/O或内存资源。

int pci_request_regions(struct pci_dev *pdev, const char *res_name); 
 
 void pci_release_regions(struct pci_dev *pdev);



● 获取/设置驱动私有数据。

void *pci_get_drvdata (struct pci_dev *pdev); 
 
 void pci_set_drvdata (struct pci_dev *pdev, void *data);

● 使能/禁止PCI设备。

int pci_enable_device(struct pci_dev *dev); 
 
 void pci_disable_device(struct pci_dev *dev);

● 设置为总线主DMA。

void pci_set_master(struct pci_dev *dev);

● 寻找指定总线指定槽位的PCI设备。

struct pci_dev *pci_find_slot (unsigned int bus, unsigned int devfn);

● 设置PCI能量管理状态（0=D0 ... 3=D3）。

int pci_set_power_state(struct pci_dev *dev, pci_power_t state);

● 在设备的能力表中找出指定的能力。

int pci_find_capability (struct pci_dev *dev, int cap);

● 启用设备内存写无效事务。

int pci_set_mwi(struct pci_dev *dev);

● 禁用设备内存写无效事务。

void pci_clear_mwi(struct pci_dev *dev);

