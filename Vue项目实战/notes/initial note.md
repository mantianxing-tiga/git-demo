# Vue 项目实战笔记——电商项目
## 开发思想：<font color='red'>前后端分离模式</font>
---
## 前端技术栈
* Vue (主体框架)
* Vue-router (路由)
* Element-UI (前端常用库)
* Axios (网络通信用)
* Echarts (利用数据制作图表)
---
## 知识回顾
* 安装 vue 之前需要先安装 nodeJs
* npm 是 nodeJs 的安装包管理工具，它的作用是对 nodeJs 的扩展包进行管理，我们平常使用最多的是他的 install（下载功能），执行 `npm install` 命令在**默认**情况下是将 nodeJs 存储在国外的官方服务器里的扩展包下载到本地进行使用
* nrm 是 nodeJs 的一个扩展包，使用 `npm install nrm -g` 可以从 nodeJs 的服务器里下载 nrm 到本地。
nrm 的功能是切换 npm 命令的下载源，因为 npm 默认的下载源是 nodeJs 的官方服务器，下载速度会比较慢，国内的大公司——比如阿里巴巴会将 nodeJs 的所有库文件复制一份放在其内部服务器上，中国的用户连接这些**镜像源**进行下载，速度会有极大提升。