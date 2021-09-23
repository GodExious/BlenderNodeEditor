# NodeEditor
NodeEditor addon for blender  
Reference @atticus-lv  
Will re-write to build model-editor  



## Show

![1](./doc/1.png)



![2](./doc/2.png)



## Current

* 基本框架：自定义的tree-node-socket、tree中的node与socket采用字典查询、基于socket入度的拓扑排序

* 浮点数的输入输出与运算

* Vector的输入输出





## TODO

* 增加更多的节点
* 建模系统、颜色系统
* socket与节点内置值的联动
* socket的缺省
* 更好的UI和交互
* 节点的UI-update和process-Update
* 优化socket_values的参数传递 与 key
* 数据结果的自动刷新
* 将入度判断从socket数量的prepare_num改为input-link的num+必须连接的函数判断
* 封装string2list与list2string
* 封装init文件自动加载路径下模块
* 让process返回True/False，确定节点是否完成计算，以便决定是否执行transfer



## Large Change

* 原来socket父类内置有被继承的socket_value，但是由于子类数据类型的变化，父类中的socket_value已经删除，所有的子类必须自己定义socket_value才能满足transfer 传递socket_value的需求(已弃用)
* 原来使用原生list类型用于存储bmesh的点边面数据，但是存在覆盖的问题无法解决，采用转换StringProperty代替



## Develop Need

fake-bpy-module  
Blender Development  



## Reference

Blender/3.0/scripts/templates_py  
https://gitlab.com/AquaticNightmare/rigging_nodes  
https://github.com/atticus-lv/simple_node_tree  
https://github.com/aachman98/Sorcar  
https://github.com/nortikin/sverchok  




## notice

建立object需要mesh，删除object时不会删除mesh,需要清理未使用数据clean  

