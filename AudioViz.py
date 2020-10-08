
bl_info = {
    "name": "AudioViz",
    "author": "Baklanov Ilya",
    "version": (0, 1),
    "blender": (2, 72, 0),
    "location": "Tool bar > Animation tab > Аудиовизуализация",
    "description": "Копирование и визуализация активных объектов",
    "category": "Animation"
}


import bpy
from bpy.types import Panel, Operator
from bpy.props import *
#
# Определения свойств
#
wm = bpy.context.window_manager
bpy.types.WindowManager.xyz = EnumProperty(
    items = [('XYZ','XYZ',"Маcштабирование объекта по всем осям"),
             ('XY','XY',"Маcштабирование объекта по осям XY"),
             ('XZ','XZ',"Маcштабирование объекта по осям XZ"),
             ('YZ','YZ',"Маcштабирование объекта по осям YZ"),
             ('X','X',"Маcштабирование объекта по оси X"),
             ('Y','Y',"Маcштабирование объекта по оси Y"),
             ('Z','Z',"Маcштабирование объекта по оси Z")],    
    name = '')        
wm.xyz = 'XYZ'
    
bpy.types.WindowManager.max_value = FloatProperty(
    name = 'Макс. размер',
    default = 1.0,
    soft_min = 0.0,
    description = "Размер маштабирования объекта по заданным осям")
wm.max_value = 1.0

bpy.types.WindowManager.min_value = FloatProperty(
    name = 'Мин. размер',
    default = 0.1,
    soft_min = 0.0,
    description = "Минимальный размер объектов")
wm.min_value = 0.1
                        
bpy.types.WindowManager.x_value = IntProperty(
    name = 'X',
    default = 10,
    soft_min = 1,
    soft_max = 200,
    description = "Кол-во объектов по X")
wm.x_value = 10

bpy.types.WindowManager.y_value = IntProperty(
    name = 'Y',
    default = 1,
    soft_min = 1,
    soft_max = 20,
    description = "Кол-во объектов по Y")
wm.y_value = 1
  
bpy.types.WindowManager.x_step = FloatProperty(
    name = 'X',
    default = 1.0,
    soft_min = 0,
    soft_max = 100.0,
    description = "Расстояние мажду объектами по оси X")
wm.x_step = 1.0
      
bpy.types.WindowManager.y_step = FloatProperty(
    name = 'Y',
    default = 1.0,
    soft_min = 0,
    soft_max = 100.0,
    description = "Расстояние между объектами по оси Y")
wm.y_step = 1.0     
       
bpy.types.WindowManager.max_column = IntProperty(
    name = '',
    default = 1,
    soft_min = 1,
    soft_max = 20,
    description = "Наибольший ряд")
wm.max_column = 1
    
bpy.types.WindowManager.wave = BoolProperty(
    name = 'Волна',
    description = "Эффект отставания рядов")
wm.wave = False
        
bpy.types.WindowManager.wave_step = IntProperty(
    name = '',
    default = 1,
    soft_min = 1,
    soft_max = 20,
    description = "Задержка между рядами в кадрах")
wm.wave_step = 1

bpy.types.WindowManager.layer = IntProperty(
    name = 'Свободный слой',
    default = 2,
    soft_min = 1,
    soft_max = 20)
wm.layer = 2

bpy.types.WindowManager.bake_frame = IntProperty(
    name = "Кадр начала запекания",
    default = 1,
    description = "Кадр начала запекания")
wm.bake_frame = 1
         
bpy.types.WindowManager.max_freq = IntProperty(
    name = "Максимальная частота",
    default = 20000,
    soft_min = 1,
    description = "Максимальная частота")
wm.max_freq = 20000
     
bpy.types.WindowManager.min_freq = IntProperty(
    name = "Минимальная частота",
    default = 20,
    soft_min = 1,
    description = "Минимальная частота")
wm.min_freq
       
bpy.types.WindowManager.size_color = BoolProperty(
    name = "Изменение цвета от размера",
    description = "Изменение цвета от размера объекта")
wm.size_color = False
    
bpy.types.WindowManager.FilePath = StringProperty(
    name = "",
    description = "Путь до аудиозаписи",
    subtype = 'FILE_PATH')
    
bpy.types.WindowManager.attack = FloatProperty(
    name = "attack",
    description = "attack",
    default = 0.005,
    soft_min = 0)
wm.attack = 0.005

bpy.types.WindowManager.release = FloatProperty(
    name = "release",
    description = "release",
    default = 0.2,
    soft_min = 0)
wm.release = 0.2
  
bpy.types.WindowManager.threshold = FloatProperty(
    name = "threshold",
    description = "threshold",
    default = 0.0,
    soft_min = 0)
wm.threshold = 0.0
    
bpy.types.WindowManager.sthreshold = FloatProperty(
    name = "sthreshold",
    description = "sthreshold",
    default = 0.5,
    soft_min = 0)
wm.sthreshold = 0.5
    
bpy.types.WindowManager.use_accumulate = BoolProperty(
    name = "accumulate",
    description = "accumulate")
wm.use_accumulate = False
   
bpy.types.WindowManager.use_additive = BoolProperty(
    name = "additive",
    description = "additive")
wm.use_additive = False
    
bpy.types.WindowManager.use_square = BoolProperty(
    name = "square",
    description = "square")
wm.use_square = False         
#
# Создание панели
#                   
class AudioVizPanel(Panel):    
    bl_label = "Аудиовизуализация"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Animation'
    bl_context = "objectmode"
    
    def draw(self, context):
                                   
        layout = self.layout
        
        try:
            bpy.context.active_object.scale
        except AttributeError:
            row = layout.row()
            row.label(text="Нет активного объекта", icon='ERROR')
            
        if wm.FilePath[-3:] != 'mp3':
            row = layout.row()
            row.label(text="Неверный формат аудиофайла", icon='ERROR')
                                           
        if wm.max_column > wm.y_value:
            row = layout.row()
            row.label(text="Нет ряда №"+str(wm.max_column), icon='ERROR')
        
        row = layout.row()
       
        row.operator('anim.bake',text="Создание визуализации",icon='BLENDER')
        
        split = layout.split()
                
        col = split.column(align=True)        
        col.label(text="Размеры сетки")
        col.prop(wm, 'x_value')
        col.prop(wm, 'y_value')
        col.label(text="Наибольший ряд")
        col.prop(wm, 'max_column')
        
        row = layout.row(align=True)        
        row.label(text="Ось маcштабирования")
        row.prop(wm, 'xyz')
        
        row = layout.row()
        row.prop(wm, 'wave')        
        if wm.wave:
            row = layout.row()
            row.label(text="Задержка волны")
            row.prop(wm, 'wave_step')
            
        if wm.size_color and bpy.context.scene.render.engine != 'CYCLES':
            row = layout.row()
            row.label(text="Данный режим поддерживается только в Cycles Render",
                      icon='ERROR')        
        if wm.size_color:               
            try:
                bpy.context.active_object.active_material.node_tree.nodes['Value']
            except AttributeError:
                row = layout.row()
                row.label(text="У данного объекта нет материала",
                          icon='ERROR')
            except KeyError:
                row = layout.row()
                row.label(text="У данного объекта неподходящий материал",
                          icon='ERROR')
                   
        row = layout.row()
        row.prop(wm,'size_color')
                    
        row = layout.row()
        row.prop(wm, 'layer')
        
        row = layout.row()
        row.prop(wm, 'bake_frame')
        
        col = split.column(align=True)
        col.label(text="Расстояние")
        col.prop(wm, 'x_step')
        col.prop(wm, 'y_step')
        col.label()
        col.prop(wm, 'max_value')
        col.prop(wm, 'min_value')
                                                     
        box = layout.box()
        
        box.label(text="Запекание аудиозаписи")
        
        row = box.row()
        row.label(text="Путь до аудиозаписи")
        row = box.row()
        row.prop(wm, 'FilePath')
        
        split = box.split()
        col = split.column(align=True)
        col.prop(wm, 'max_freq')
        col.prop(wm, 'min_freq')
        
        row = box.row()
        row.label(text="Опции запекания")
        
        split = box.split()
        
        col = split.column(align=True)
        col.prop(wm,'attack')
        col.prop(wm, 'release')
        
        col = split.column(align=True)
        col.prop(wm, 'threshold')
        col.prop(wm, 'sthreshold')
        
        split = box.split()
        
        col = split.column()
        col.prop(wm, 'use_accumulate')
        
        col = split.column()
        col.prop(wm, 'use_additive')
        
        col = split.column()
        col.prop(wm, 'use_square')        
#
# Функции аудиовизуализации
#                               
def l_size(xyz,list,size):
    for i in xyz:
        if i == 'X':
            list[0] *= size
        elif i == 'Y':
            list[1] *= size
        else:
            list[2] *= size
    return list
    
def list_lock(xyz,list):
        for i in xyz:
            if i == 'X':
                list.remove(0)
            elif i == 'Y':
                list.remove(1)
            else:
                list.remove(2)
        return list

def active_size(xyz,list):
    for i in xyz:
        if i == 'X':
            list[0] = 1
        elif i == 'Y':
            list[1] = 1
        else:
            list[2] = 1
    return list
       
def bake():
    xyz = wm.xyz
    x = wm.x_value
    y = wm.y_value
    
    x_step = wm.x_step
    y_step = wm.y_step
    
    x_loc = 0
    y_loc = wm.y_value//2
        
    y_count = wm.y_value//2
    x_count = 0
    
    h_column = y_loc+1-wm.max_column
    
    hightest = wm.max_value
    hight = hightest/2**(y_loc-h_column)
    
    obj = bpy.context.active_object
  
    list_size = [obj.scale[i] for i in range(3)]
    list_size = active_size(xyz, list_size)
    
    path = wm.FilePath
    
    layer = wm.layer-1
    
    step_l = wm.min_freq
    step_h = abs(wm.max_freq-wm.min_freq)/x+wm.min_freq
    
     
    for i in range(x*y):
        bpy.ops.object.duplicate()        
        obj = bpy.context.active_object  
              
    # Создание списка с размерами объектов        
        if i < 1:
            list_size = l_size(xyz, list_size, hight)
        else:
            list_size = [1, 1, 1]
        
        if x_count == x:
            y_loc -= y_step
            x_loc = 0
            
            y_count -= 1           
            x_count = 0
            
            step_l = wm.min_freq
            step_h = abs(wm.max_freq-wm.min_freq)/x+wm.min_freq
                                     
            if wm.wave:
                bpy.context.scene.frame_current += wm.wave_step
                
            if y_count < h_column:
                list_size = l_size(xyz, list_size, 0.5)
                hight /= 2
            else:
                list_size = l_size(xyz, list_size, 2)
                hight *= 2
                                
        # Изменение размера и положения объектов                   
        obj.location.x = x_loc
        obj.location.y = y_loc
        
        obj.scale = list_size
                   
        bpy.ops.object.transform_apply(location=0, rotation=0, scale=1)
     
        if not i:
            bpy.context.scene.frame_current = wm.bake_frame
            bpy.ops.anim.keyframe_insert_menu(type='Scaling')
                     
        # Запекание аудиозаписи
        bpy.context.area.type = 'GRAPH_EDITOR'
        bpy.context.space_data.mode = 'FCURVES'
                
        anim = obj.animation_data.action
                               
        l_lock = [0, 1, 2]
        lock = []        
        if len(xyz) < 3:
            lock = list_lock(xyz, l_lock)
            for n in lock:
                anim.fcurves[n].lock = 1
                
        bpy.ops.graph.sound_bake(
               filepath=path,
               low = step_l,
               high = step_h,
               attack = wm.attack,
               release = wm.release,
               threshold = wm.threshold,
               sthreshold = wm.sthreshold,
               use_accumulate = wm.use_accumulate,
               use_additive = wm.use_additive,
               use_square = wm.use_square
        )
                                                              
        active_fcurves = [0, 1, 2]
        
        min_value = wm.min_value/hight
                    
        for n in lock:
            active_fcurves.remove(n) #Удаляем заблокированные оси из списка
                                                               
        for n in active_fcurves:
            anim.fcurves[n].modifiers.new('LIMITS')
            anim.fcurves[n].modifiers.active.use_min_y = 1
            anim.fcurves[n].modifiers.active.min_y = min_value
            
        # Изменение цвета объекта от его размера        
        if wm.size_color:
            
            obj.active_material = obj.active_material.copy()
            
            bpy.context.area.type = 'NODE_EDITOR'
          
            node_tree = obj.active_material.node_tree
            node = node_tree.nodes['Value']
                
            node.outputs[0].default_value = 1
            node.outputs[0].driver_add('default_value')
            
            bpy.context.area.type = 'GRAPH_EDITOR'
            bpy.context.space_data.mode = 'DRIVERS'
            
            driver = node_tree.animation_data.drivers[0].driver
            
            driver.expression ='var-var_001'
            if not i:            
                driver.variables.new()
            
            variables = driver.variables['var']
            variables.type = 'TRANSFORMS'
            
            targets = variables.targets[0]
            targets.id = bpy.data.objects[obj.name]
            
            if active_fcurves[0] == 0:
                targets.transform_type = 'SCALE_X'
            elif active_fcurves[0] == 1:
                targets.transform_type = 'SCALE_Y'
            else:
                targets.transform_type = 'SCALE_Z'
                
            if not i:
                driver.variables.new()
            
            variables = driver.variables['var_001']
            variables.type = 'SINGLE_PROP'
            
            targets = variables.targets[0]
            targets.id_type = 'WINDOWMANAGER'
            targets.id = bpy.data.window_managers['WinMan']
            targets.data_path = 'min_value'
                                                                                                                                                                              
        # Перемецение на объектов на выбранны сло         
        active_layer = bpy.context.scene.active_layer
                       
        list_layers = [False for i in range(20)]
        list_layers[layer] = True
        bpy.ops.object.move_to_layer(layers=list_layers)
                                                    
        if not bpy.context.scene.layers[layer]:           
            bpy.context.scene.layers[layer] = True
            bpy.context.scene.layers[active_layer] = False                          

            
        x_loc += x_step
        x_count += 1
        
        step_l = step_h
        step_h = abs(wm.max_freq-wm.min_freq)/x*(x_count+1)+wm.min_freq
                                  
    bpy.context.area.type = 'VIEW_3D'

class AudioViz(Operator):
    bl_idname = 'anim.bake'
    bl_label = ''
    bl_description = 'Создание аудиовизуализации'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bake()
        return{'FINISHED'}
                 
def register():
    bpy.utils.register_class(AudioVizPanel)
    bpy.utils.register_class(AudioViz)


def unregister():
    bpy.utils.unregister_class(AudioVizPanel)
    bpy.utils.unregister_class(AudioViz)


if __name__ == "__main__":
    register()    
