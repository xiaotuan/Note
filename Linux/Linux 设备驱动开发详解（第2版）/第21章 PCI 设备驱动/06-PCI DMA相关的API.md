### 21.1.4 PCI DMA相关的API

内核中定义了一组专门针对PCI设备的DMA操作接口，这些API的原型和作用与第11章介绍的通用DMA API非常相似，主要包括如下。

● 设置DMA缓冲区掩码。

int pci_set_dma_mask(struct pci_dev *dev, u64 mask);

● 一致性DMA缓冲区分配/释放。

void *pci_alloc_consistent(struct pci_dev *pdev, size_t size, dma_addr_t *dma_handle); 
 
 void pci_free_consistent(struct pci_dev *hwdev, size_t size, void *vaddr, dma_addr_t 
 
 dma_handle);

● 流式DMA缓冲区映射/去映射。

dma_addr_t pci_map_single(struct pci_dev *pdev, void *ptr, size_t size, int direction);

int pci_map_sg(struct pci_dev *pdev,struct scatterlist *sgl,int num_entries, int 
 
 direction); 
 
 void pci_unmap_single(struct pci_dev *pdev, dma_addr_t dma_addr, size_t size, 
 
 int direction); 
 
 void pci_unmap_sg(struct pci_dev *pdev, struct scatterlist *sg, int nents, int 
 
 direction);

这些API的用法与第11章中介绍的dma_alloc_consistent()、dma_map_single()、dma_map_sg()相似，只是以pci_开头的API用于PCI设备驱动。

