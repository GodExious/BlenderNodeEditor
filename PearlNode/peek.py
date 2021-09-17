bl_info = {
    "name": "nodes_example",
    "author": "imdjs",
    "version": (1,0),
    "blender": (2,93,0),
    "location": "Node Editor > nodes_example",
    "description": "this script is for study only not for use  purpose",
    "wiki_url": "http://",
    "warning": "",
    "category": "Node"}

# ----导入必须的模块--------------------------
import bpy,os,sys,imp
from bpy.app.handlers import persistent
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
from bpy.props import BoolProperty,IntProperty,StringProperty,FloatProperty,FloatVectorProperty,EnumProperty,PointerProperty
from bpy.types import NodeTree, Node,NodeSocket

#----------------------------------------------------
pathTestNODE = os.path.dirname(__file__) #本py文件所在目录 where this py file is
TEST_NODE=os.path.basename(pathTestNODE) #Node_imdjs


#----刷新手柄  handler---------------------------------------------------
@persistent
def 刷新手柄函数(scene):
    for nt in bpy.data.node_groups:
        if(nt.bl_idname=="Node_imdjs"):
            for n in nt.nodes:
                #print("N==",n.name)
                if (n.bl_idname =="TEST_NodeStartPre"):#如果是开始节点
                    n.升级节点函数(scene)#升级开始节点


# 主节点树类型---------------------------------------------
class Node_imdjs(NodeTree):
    bl_idname = "Node_imdjs"
    bl_label = 'Node_imdjs'
    bl_icon = 'MONKEY'

#  ---节点的接口,输入输出接口都可以用这个-------------------------------------
class TEST_NodeSocket(NodeSocket):
    bl_idname = "TEST_NodeSocket"
    bl_label = "输出输入"

    ip开始帧 :IntProperty()

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (1.0, 1.0, 0.0, 1.0)
#bpy.utils.register_class(TEST_NodeSocket);


#////主要的节点树///////////////////////////////////////
class TEST_NODES():
    @classmethod
    def poll(cls, ntree):
        return (ntree.bl_idname == Node_imdjs.bl_idname)
        
#////连接物体的 入口节点///////////////////////////////////    
class object_TEST_NODES(Node,TEST_NODES):
    bl_idname = "TEST_NodeObject"
    bl_label = "物体"

    spObject:StringProperty(name='object',description='选择一个物体',default='',maxlen=0,subtype='NONE',update=None,get=None,set=None);
    #--------------------------------------------------------------
    def init(self,context):
        self.outputs.new(TEST_NodeSocket.bl_idname,name="输出",identifier = "out_put")

    #-------------------------------------------------------------
    def draw_buttons(self,context,layout):
        layout.prop_search(self, "spObject", context.scene, "objects", text="物体们", icon = "OBJECT_DATA");
#////开始节点//////////////////////////////////////
#每个节点树都要增加这个开始节点.
class 开始节点TEST_NODES(Node,TEST_NODES):
    bl_idname = "TEST_NodeStartPre"
    bl_label = "开始节点"
    bl_width_default=200;
    bl_width_min=200;
    bl_width_max=500;
  
    ip开始帧 :IntProperty()
    spInfo:StringProperty(name='',description='',default='')
    #------------------------------------------------------------
    def init(self,context):
        self.inputs.new(TEST_NodeSocket.bl_idname,name="输入",identifier = "in_put")
        self.outputs.new(TEST_NodeSocket.bl_idname,name="输出",identifier = "out_put")
        self.ip开始帧 = 1

    #======================================================
    def 升级节点函数(self,scene):
        #----如果有输入节点链接-----------------------------------------------
        if(self.inputs["输入"].links):
            self.outputs["输出"].ip开始帧 = self.ip开始帧
            nInput=self.inputs["输入"].links[0].from_node
            #print("GROUP==",nInput.name);
            if(not nInput):
                self.report({"ERROR"},"NO  输入 NODE!!!");#"INFO" "ERROR" "DEBUG" "WARNING"
                return ;
            
            nOutput=self.outputs["输出"].links[0].to_node
            if(nOutput):
                o=scene.objects[nInput.spObject]
                nOutput.升级节点函数(scene,o)

    #-------------------------------------------------------------
    def draw_buttons(self,context,layout):
        layout.prop(self, "ip开始帧", text = "开始帧",slider=False);
        OP=layout.operator(operator=DebugTestNodes.bl_idname,text='debug',text_ctxt='',translate=True,icon='NONE',emboss=True,icon_value=0);OP.spThisNode=self.name;#self.spInfo=OP.spInfo;
        
        uil=layout.row(align=False);
        uil.prop(self,"spInfo",text = "Info",icon="NONE",slider=False,emboss=True)
        uil.enabled=False;
   
#====Debug调试节点,===========================================
class DebugTestNodes(bpy.types.Operator):
    bl_idname = "op.update_node_debug";
    bl_label = "刷新物体";
    bl_description = "debug节点,尝试执行节点以检查它是否有问题";
    spThisNode:StringProperty(name='',description='',default='',maxlen=0,subtype='NONE',update=None,get=None,set=None);
    #spInfo=StringProperty(name='',description='',default='')    
  
    def execute(self, context):
        scene=context.scene;
        if(self.spThisNode!=None):
            Lnt=[nt for nt in bpy.data.node_groups if(nt.bl_idname=="Node_imdjs")];
            for nt in Lnt:
                for n in nt.nodes:
                    if (n.bl_idname =="TEST_NodeStartPre" and n.name==self.spThisNode):
                        n.升级节点函数(scene);
                        n.spInfo="ok"
                        return {"FINISHED"};
        n.spInfo="没有开始节点!!!"
        return {"FINISHED"};


  
#////功能节点,在这里可以写任何想实现的功能/////////////////////////
class TEST_NODES_FUNCION(Node, TEST_NODES):
    bl_idname = "TEST_NodeFuncion"
    bl_label = '移动物体'
    bl_icon = 'MONKEY'
  
    fvpp:FloatVectorProperty(size=3, default=(1.0, 1.0, 1.0));
    #====layout============================================
    def init(self, context):
        self.inputs.new(TEST_NodeSocket.bl_idname,"输入")

        self.inputs.new("NodeSocketInt","TIME")
        self.outputs.new(TEST_NodeSocket.bl_idname,"输出")

    #======================================================
    def 升级节点函数(self,scene,o): #每帧刷新一次
        fStartTime=self.inputs["输入"].ip开始帧 = self.inputs["输入"].links[0].from_socket.ip开始帧+1#前面的时刻传给自己 get the time  from front socket
        #----看输入接口是否有节点--if there is a node front--------------------
        for s in ["TIME"]:
            if (len(self.inputs[s].links) > 0):#有链接
                nFront = self.inputs[s].links[0].from_node
                self.inputs[s].default_value = self.inputs[s].links[0].from_socket.default_value#把对方的值 赋予自己 get the value  from front node

        #----如果在本节点时间内    within the node time--------------------------
        nsNext=self.outputs["输出"]
        iTime_this=self.inputs["TIME"].default_value
        if(iTime_this==0 and iTime_this!=100000):
            iTime_this=100000
        nsNext.ip开始帧 = fStartTime + iTime_this#决定 本节点结束时间  decide the end time
        iFrame=scene.frame_current
        if (iFrame>fStartTime and iFrame<=nsNext.ip开始帧 ):#在本节点时间内就...during this node time
            #o.location=(o.location.x+0.02)0.1;
            o.location=o.location.x+0.02,o.location.y+0.02,o.location.z+0.01;
            self.fvpp=o.location;#显示坐标
            刷新界面函数("NODE_EDITOR","WINDOW");
        #----如果有下一个节点 并且时间已过本节点时间  就升级它-out of node time-----------------
        if(len(nsNext.links) > 0):
            if (iFrame>= nsNext.ip开始帧):
                for link in nsNext.links:
                    link.to_node.升级节点函数(scene,o)

    #===按钮界面==layout======================================
    def draw_buttons(self, context, layout):
        layout.prop(self,"fvpp",text = "坐标",icon="NONE",slider=False,emboss=True)

#////每修改了物体位置 都要刷新一下界面/////////////////////////////
def 刷新界面函数(area,region):
    screen=bpy.context.screen;
    if(area):
        for a in screen.areas:
            if(a.type==area):#EMPTY", "VIEW_3D", "TIMELINE", "GRAPH_EDITOR", "DOPESHEET_EDITOR", "NLA_EDITOR", "IMAGE_EDITOR", "SEQUENCE_EDITOR", "CLIP_EDITOR", "TEXT_EDITOR", "NODE_EDITOR", "LOGIC_EDITOR", "PROPERTIES", "OUTLINER", "USER_PREFERENCES", "INFO", "FILE_BROWSER", "CONSOLE"
                #a.tag_redraw();#■■这个能刷新所有 region画面
                if(region):
                    for r in a.regions:#WINDOW", "HEADER", "CHANNELS", "TEMPORARY", "UI", "TOOLS", "TOOL_PROPS", "PREVIEW
                        if(r.type==region):
                            r.tag_redraw();
                            break;
                    break;

#---------------------------------------------------------------
class TEST_NodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return (context.space_data.tree_type == Node_imdjs.bl_idname);
 
#====增加节点面板与条目============================================
TEST_node_list = [
    TEST_NodeCategory("TEST_NodeCategory2", "开始",
    items=[ NodeItem(开始节点TEST_NODES.bl_idname),
        NodeItem(TEST_NODES_FUNCION.bl_idname) ]),
    TEST_NodeCategory("TEST_NodeCategory1", "物体输入",
    items=[ NodeItem(object_TEST_NODES.bl_idname) ]

)
]
# 注册插件函数---------------------------------------------------
def 注册类(LL类,b打印=False):
    for L类 in LL类:
        for 类 in L类:
            if(b打印):print("REGISTER_CLASS==",类);
            try:
                bpy.utils.register_class(类);
            except:
                print("!!!不能注册类 ==",类);
            
def 注销类(LL类,b打印=False):
    for L类 in LL类:
        for 类 in L类:
            if(b打印):print("UNREGISTER_CLASS==",类);
            try:
                bpy.utils.unregister_class(类);
            except:
                print("!!!不能注销类==",类);


            
#----注册插件------------------------------------
def register():
    注册类([(Node_imdjs,TEST_NodeSocket,TEST_NODES,object_TEST_NODES,开始节点TEST_NODES,DebugTestNodes,TEST_NODES_FUNCION,TEST_NodeCategory)],True);

    nodeitems_utils.register_node_categories("Node_imdjs", TEST_node_list)
    bpy.app.handlers.frame_change_pre.append(刷新手柄函数)#刷新手柄



def unregister():
    nodeitems_utils.unregister_node_categories("Node_imdjs")
    注销类([(Node_imdjs,TEST_NodeSocket,TEST_NODES,object_TEST_NODES,开始节点TEST_NODES,DebugTestNodes,TEST_NODES_FUNCION,TEST_NodeCategory)]);
    try:
        bpy.app.handlers.frame_change_pre.remove(刷新手柄函数)
    except:pass;



#//////////////////////////////////////////////////
if (__name__ == "__main__"):
    register()
