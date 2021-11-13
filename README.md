# 从scapy和wireshark学计算机网络

众所周知，计网被评为最困的计算机专业课，俗称计算机中的语文。👴看了《计算机网络－自顶向下方法》（后文简称CNTDA）之后，觉得翻译就像汤姆叔叔的烂苹果派一样糟糕，上帝啊，我发誓会狠狠踢他的屁股。建议带🔥去看英文原版。

但是👴最近接触的许多实验还是很好玩的，于是本文试图通过全程动手实操学习计网。

讲解部分参见博客原文：[从scapy和wireshark学计算机网络 | lonelyuan's Blog](https://lonelyuan.github.io/post/Computer_Network_Exp/)

---

实验来源：

- 👴自己
- SEEDLab，雪城大学的信息安全课配套实验，网络安全部分。国内知名度不高所以值得一做。[官方网站](https://seedsecuritylabs.org/Labs_20.04) 
- CNTDA 实验：[GIthub上抄的作业](https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)

主要工具：

- wireshark是坠nb的网络封包分析软件。就是用来抓包的。

> 下载：[https://www.wireshark.org/download.html](https://www.wireshark.org/download.html)
> 教程：[https://www.javatpoint.com/wireshark](https://www.javatpoint.com/wireshark) 

- scapy库是python的网络编程库，可以让你细致入微的操纵网络流量。就是用来发包的。
  - //不要和爬虫库scrapy混淆

> scapy文档：[https://scapy.readthedocs.io/en/latest/](https://scapy.readthedocs.io/en/latest/)
> 中文版：[https://www.osgeo.cn/scapy/introduction.html](https://www.osgeo.cn/scapy/introduction.html) //有些翻译错误

实验目录：

> 编号规则：0xabn
>
> - a：层级：1 - 应用层；2 - 传输层；3 - 网络层；4 - 链路层；5 - 物理层
> - b：难度：0 - ⭐；1 - ⭐⭐；2 - ⭐⭐⭐；3 - ⭐⭐⭐⭐；4 - ⭐⭐⭐⭐⭐；
> - n：重复难度则再加一位编号

#### 0x10 应用层: Web服务器 | ⭐ 

#### 0x20 传输层: TCP观察 | ⭐ | TODO

#### 0x30 网络层: 路由追踪 | ⭐ 

#### 0x301 网络层: 欺骗ping | ⭐ | TODO

#### 0x41 链路层: ARP缓存投毒 | ⭐⭐ | TODO

#### 0x31 网络层: NAT，DHCP和虚拟机 |  ⭐⭐ | TODO

#### 0x21 传输层: TCP攻击 | ⭐⭐ | TODO

#### 0x13 应用层: DNS本地攻击 | ⭐⭐⭐ | TODO

#### 0x14 应用层: SSL协议和HTTPS | ⭐⭐⭐⭐ | TODO

#### 0x15 应用层: 多线程Web代理服务器 | ⭐⭐⭐⭐⭐  | TODO

#### 0x151 应用层: VPN | ⭐⭐⭐⭐⭐ | TODO

#### 0x1? 应用层: V2Ray协议学习 | ？？？ | TODO