bl_info = {
    "name": "FontAnim",
    "author": "Baklanov Ilya",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "location": "Tool bar > FontAnim ",
    "description": "Создание простых текстовых анимаций",
    "category": "Animation"
}

import bpy
import random
from bpy.types import Panel, Operator
from bpy.props import *

wm = bpy.context.window_manager
#Запамнающе настроки
bpy.types.WindowManager.list_start = StringProperty()

bpy.types.WindowManager.list_end = StringProperty()

bpy.types.WindowManager.name_end = StringProperty()

bpy.types.WindowManager.name_start = StringProperty()

bpy.types.WindowManager.last_frame = IntProperty()

bpy.types.Object.start_location_x = FloatProperty()
###Своства панели "Добавить текст"
bpy.types.WindowManager.text = StringProperty(
    name = '')

bpy.types.WindowManager.text_font = StringProperty(
    name='Шрифт',
    subtype='FILE_PATH')
    
bpy.types.WindowManager.offset = FloatProperty(
    name = 'Offset',
    soft_min = -1,
    soft_max = 1)
wm.offset = 0

bpy.types.WindowManager.extrude = FloatProperty(
    name = 'Extrude',
    soft_min = 0)
wm.extrude = 0

bpy.types.WindowManager.depth = FloatProperty(
    name = 'Depth',
    soft_min = 0)
wm.depth = 0

bpy.types.WindowManager.resolution = IntProperty(
    name = 'Resolution',
    soft_min = 0)
wm.resolution = 0

bpy.types.WindowManager.shear = FloatProperty(
    name = 'Shear',
    soft_min = -1,
    soft_max = 1)
wm.shear = 0

bpy.types.WindowManager.s_b_l = FloatProperty(
    name = 'Буквами',
    soft_min = 0)
wm.s_b_l = 0.01

bpy.types.WindowManager.s_b_w = FloatProperty(
    name = 'Словами',
    soft_min = 0)
wm.s_b_w = 0.5
###Своства панели "Создание анимации"
interpolation_type =  [
    ('CONSTANT','Constant','CONSTANT','IPO_CONSTANT',0),
    ('LINEAR','Linear','LINEAR','IPO_LINEAR',1),
    ('BEZIER','Bezier','BEZIER','IPO_BEZIER',2),
    ('SINE','Sinusoidal','SINE','IPO_SINE',3),
    ('QUAD','Quadratic','QUAD','IPO_QUAD',4),
    ('CUBIC','Cubic','CUBIC','IPO_CUBIC',5),
    ('QUART','Quartic','QUART','IPO_QUART',6),
    ('QUINT','Quintic','QUINT','IPO_QUINT',7),
    ('EXPO','Exponential','EXPO','IPO_EXPO',8),
    ('CIRC','Circular','CIRC','IPO_CIRC',9),
    ('BACK','Back','BACK','IPO_BACK',10),
    ('BOUNCE','Bounce','BOUNCE','IPO_BOUNCE',11),
    ('ELASTIC','Elastic','ELASTIC','IPO_ELASTIC',12),
    ]
    
easing_type = [
    ('AUTO','Automatic Easing','Automatic Easing','IPO_EASE_IN_OUT',0),
    ('EASE_IN','Ease In','Ease In','IPO_EASE_IN',1),
    ('EASE_OUT','Ease Out','Ease Out','IPO_EASE_OUT',2),
    ('EASE_IN_OUT','Ease In and Out','Ease In and Out','IPO_EASE_IN_OUT',3),
    ]
#    
bpy.types.WindowManager.interpol_l = EnumProperty(
    items = interpolation_type,
    name = 'Interpolation Mode')
        
bpy.types.WindowManager.interpol_r = EnumProperty(
    items = interpolation_type,
    name = 'Interpolation Mode')
        
bpy.types.WindowManager.interpol_s = EnumProperty(
    items = interpolation_type,
    name = 'Interpolation Mode')    
#
bpy.types.WindowManager.easing_l = EnumProperty(
    items = easing_type,
    name = 'Easing Type')
        
bpy.types.WindowManager.easing_r = EnumProperty(
    items = easing_type,
    name = 'Easing Type')
        
bpy.types.WindowManager.easing_s = EnumProperty(
    items = easing_type,
    name = 'Easing Type')    
#
bpy.types.WindowManager.back_l = FloatVectorProperty(
    name = 'Back',
    default = (1.702,1.702,1.702),
    precision = 3,
    subtype = 'XYZ')
    
bpy.types.WindowManager.back_r = FloatVectorProperty(
    name = 'Back',
    default = (1.702,1.702,1.702),
    precision = 3,
    subtype = 'XYZ')

bpy.types.WindowManager.back_s = FloatVectorProperty(
    name = 'Back',
    default = (1.702,1.702,1.702),
    precision = 3,
    subtype = 'XYZ')
    
bpy.types.WindowManager.amplitude_l = FloatVectorProperty(
    name = 'Amplitude',
    default = (0.800,0.800,0.800),
    precision = 3,
    subtype = 'XYZ')
    
bpy.types.WindowManager.amplitude_r = FloatVectorProperty(
    name = 'Amplitude',
    default = (0.800,0.800,0.800),
    precision = 3,
    subtype = 'XYZ')

bpy.types.WindowManager.amplitude_s = FloatVectorProperty(
    name = 'Amplitude',
    default = (0.800,0.800,0.800),
    precision = 3,
    subtype = 'XYZ')
    
bpy.types.WindowManager.period_l = FloatVectorProperty(
    name = 'Period',
    default = (4.100,4.100,4.100),
    precision = 3,
    subtype = 'XYZ')
    
bpy.types.WindowManager.period_r = FloatVectorProperty(
    name = 'Period',
    default = (4.100,4.100,4.100),
    precision = 3,
    subtype = 'XYZ')

bpy.types.WindowManager.period_s = FloatVectorProperty(
    name = 'Period',
    default = (4.100,4.100,4.100),
    precision = 3,
    subtype = 'XYZ')
#
bpy.types.WindowManager.step_frame_assymetry = IntProperty(
    name = 'Задержка между буквами',
    soft_min = 0,
    description = 'Кол-во кадров между анимациями букв')
wm.step_frame_assymetry = 0

bpy.types.WindowManager.max_st_frame = IntProperty(
    name = 'Макс. значение',
    soft_min = 0)
wm.max_st_frame = 0

bpy.types.WindowManager.min_st_frame = IntProperty(
    name = 'Мин. значение',
    soft_min = 0)
wm.min_st_frame = 0

bpy.types.WindowManager.assymetry_random = BoolProperty(
    name = 'Random')
wm.assymetry_random = False
#
bpy.types.WindowManager.derection = EnumProperty(
    items = [
        ('left','Слева направо','',1),
        ('right','Справа налево','',2),
        ('random','Random','',4),
        ],
    name = ' ',
    options = {'ENUM_FLAG'})
#
bpy.types.WindowManager.loc_rot_scale = EnumProperty(
    items = [
        ('location','Loc','Loc','MAN_TRANS',1),
        ('rotation','Rot','Rot','MAN_ROT',2),
        ('scale','Scale','Scale','MAN_SCALE',4),
        ],
    name = 'Loc Rot Scale',
    options={'ENUM_FLAG'})
#
bpy.types.WindowManager.speed = IntProperty(
    name = 'Продолжительность анимации',
    description = 'Продолжительность анимации буквы в секундах',
    soft_min = 0)
wm.speed = 0

bpy.types.WindowManager.start_frame_ft = IntProperty(
    name = 'Начальный кадр',
    soft_min = 0)
wm.start_frame_ft = 0
#
    
class AddTextPanel(Panel):
    bl_label = "Добавть текст"
    bl_idname = "SCENE_PT_layout_font"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'FontAnim'
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator('anim.font',text='Добавить текст',icon='ZOOMIN')
        
        row = layout.row()
        row.operator('anim.font_delete',text='Удалить текст',icon='ZOOMOUT')
        
        row = layout.row()
        row.prop(wm,'text')
        
        row = layout.row()
        row.prop(wm,'text_font')
        
        row = layout.row()
        row.label(text='Расстояние между:')
        
        split = layout.split()
        
        col = split.column(align=True)
        col.prop(wm,'s_b_l')
        col.prop(wm,'s_b_w')
        
        row = layout.row()
        row.operator('anim.font_update',text='Обновить текст',icon='ZOOMIN')
        
        row = layout.row()
        row.prop(wm,'shear')
        
        split = layout.split()
                        
        col = split.column(align=True)
        col.prop(wm,'offset')
        col.prop(wm,'extrude')
        
        col = split.column(align=True)
        col.prop(wm,'depth')
        col.prop(wm,'resolution')

class AnimationTextPanel(Panel):
    bl_label = "Создание анимации"
    bl_idname = "SCENE_PT_layout_font_anim"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'FontAnim'
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator('anim.font_anim',text='Создать анимацию',icon='ZOOMIN')
        
        row = layout.row()
        row.operator('anim.font_anim_del',text='Удалить последнюю анимацию',icon='ZOOMOUT')
               
        row = layout.row()
        row.operator('anim.font_trans',text='Перейти к настройке положения',icon='OBJECT_DATAMODE')
        
        row = layout.row()
        row.label(text='Направление:')
        
        row = layout.row()
        row.prop(wm,'derection')
        
        row = layout.row()
        row.prop(wm,'start_frame_ft')
        
        row = layout.row()
        row.prop(wm,'speed')
        
        row = layout.row()
        row.prop(wm,'step_frame_assymetry')
        row.prop(wm,'assymetry_random')
        if wm.assymetry_random:
            row = layout.row(align=True)
            row.prop(wm,'min_st_frame')
            row.prop(wm,'max_st_frame')
        
        row = layout.row()
        row.label(text='Выберете тип редактирования')
        
        row = layout.row()
        row.prop(wm,'loc_rot_scale')
        
        if 'location' in wm.loc_rot_scale:
            row = layout.row()
            row.prop(wm,'interpol_l')
            if not wm.interpol_l in ['CONSTANT','LINEAR','BEZIER']:
                row = layout.row()
                row.prop(wm,'easing_l')
            if wm.interpol_l == 'BACK':
                row = layout.row()
                row.prop(wm,'back_l')
            elif wm.interpol_l == 'ELASTIC':
                row = layout.row()
                row.prop(wm,'amplitude_l')
                
                row = layout.row()
                row.prop(wm,'period_l')
                
        if 'rotation' in wm.loc_rot_scale:
            row = layout.row()
            row.prop(wm,'interpol_r')
            if not wm.interpol_r in ['CONSTANT','LINEAR','BEZIER']:
                row = layout.row()
                row.prop(wm,'easing_r')
            if wm.interpol_r == 'BACK':
                row = layout.row()
                row.prop(wm,'back_r')
            elif wm.interpol_r == 'ELASTIC':
                row = layout.row()
                row.prop(wm,'amplitude_r')
                
                row = layout.row()
                row.prop(wm,'period_r')
                
        if 'scale' in wm.loc_rot_scale:
            row = layout.row()
            row.prop(wm,'interpol_s')
            if not wm.interpol_s in ['CONSTANT','LINEAR','BEZIER']:
                row = layout.row()
                row.prop(wm,'easing_s')
            if wm.interpol_s == 'BACK':
                row = layout.row()
                row.prop(wm,'back_s')
            elif wm.interpol_s == 'ELASTIC':
                row = layout.row()
                row.prop(wm,'amplitude_s')
                
                row = layout.row()
                row.prop(wm,'period_s')
                         
def driver(type,obj,parent_obj):
    C = bpy.context
    D = bpy.data
    
    if type == 'location':
        x_value = 'LOC_X'
        y_value = 'LOC_Y'
        z_value = 'LOC_Z'
        count = 0
    elif type == 'rotation_euler':
        x_value = 'ROT_X'
        y_value = 'ROT_Y'
        z_value = 'ROT_Z'
        count = 3
    else:
        x_value = 'SCALE_X'
        y_value = 'SCALE_Y'
        z_value = 'SCALE_Z'
        count = 6
        
    obj.driver_add(type)
    C.area.type = 'GRAPH_EDITOR'
    C.space_data.mode = 'DRIVERS'
    
    driver_x = obj.animation_data.drivers[count].driver
    driver_y = obj.animation_data.drivers[count+1].driver
    driver_z = obj.animation_data.drivers[count+2].driver
    
    if type == 'location':
        driver_x.variables.new()
        variables = driver_x.variables['var']
        variables.type = 'SINGLE_PROP'            
        targets = variables.targets[0]
        targets.id_type = 'OBJECT'
        targets.id = D.objects[obj.name]
        targets.data_path = 'start_location_x'
        
        driver_x.variables.new()
        variables = driver_x.variables['var_001']
        variables.type = 'TRANSFORMS'
        targets = variables.targets[0]
        targets.id = D.objects[parent_obj]
        targets.transform_type = x_value
        
        driver_x.variables.new()
        variables = driver_x.variables['var_002']
        variables.type = 'TRANSFORMS'
        targets = variables.targets[0]
        targets.id = D.objects[parent_obj]
        targets.transform_type = 'SCALE_X'
        
        driver_x.expression = 'var_001+var*var_002'
    else:
        driver_x.variables.new()
        driver_x.expression = 'var'
        variables = driver_x.variables['var']
        variables.type = 'TRANSFORMS'
        targets = variables.targets[0]
        targets.id = D.objects[parent_obj]
        targets.transform_type = x_value
        
    driver_z.variables.new()
    driver_z.expression = 'var'
    variables = driver_z.variables['var']
    variables.type = 'TRANSFORMS'
    targets = variables.targets[0]
    targets.id = D.objects[parent_obj]
    targets.transform_type = z_value
 
    driver_y.variables.new()
    driver_y.expression = 'var'
    variables = driver_y.variables['var']
    variables.type = 'TRANSFORMS'
    targets = variables.targets[0]
    targets.id = D.objects[parent_obj]
    targets.transform_type = y_value

def add_text(text):
    wm.list_end = ''
    wm.list_start = ''
                
    C = bpy.context
    D = bpy.data
        
    bpy.ops.object.empty_add(location=(0,0,0))
    C.active_object.name = 'end_empty'
    wm.name_end = C.active_object.name
    
    bpy.ops.object.empty_add(type='ARROWS',location=(0,0,1))
    C.active_object.name = 'start_empty'
    wm.name_start = C.active_object.name
    
    def driver_text_geometry(obj):
        obj.data.driver_add('offset')
        obj.data.driver_add('extrude')
        obj.data.driver_add('bevel_depth')
        obj.data.driver_add('bevel_resolution')
        obj.data.driver_add('shear')
        
        C.area.type = 'GRAPH_EDITOR'
        C.space_data.mode = 'DRIVERS'
        
        driver = obj.data.animation_data.drivers[0].driver       
        
        driver.variables.new()
        driver.expression = 'var'
        variables = driver.variables['var']
        variables.type = 'SINGLE_PROP'            
        targets = variables.targets[0]
        targets.id_type = 'WINDOWMANAGER'
        targets.id = D.window_managers["WinMan"]
        targets.data_path = 'offset'
        
        driver = obj.data.animation_data.drivers[1].driver  
        
        driver.variables.new()
        driver.expression = 'var'
        variables = driver.variables['var']
        variables.type = 'SINGLE_PROP'            
        targets = variables.targets[0]
        targets.id_type = 'WINDOWMANAGER'
        targets.id = D.window_managers["WinMan"]
        targets.data_path = 'extrude'
        
        driver = obj.data.animation_data.drivers[2].driver
        
        driver.variables.new()
        driver.expression = 'var'
        variables = driver.variables['var']
        variables.type = 'SINGLE_PROP'            
        targets = variables.targets[0]
        targets.id_type = 'WINDOWMANAGER'
        targets.id = D.window_managers["WinMan"]
        targets.data_path = 'depth'
        
        driver = obj.data.animation_data.drivers[3].driver
        
        driver.variables.new()
        driver.expression = 'var'
        variables = driver.variables['var']
        variables.type = 'SINGLE_PROP'            
        targets = variables.targets[0]
        targets.id_type = 'WINDOWMANAGER'
        targets.id = D.window_managers["WinMan"]
        targets.data_path = 'resolution'
        
        driver = obj.data.animation_data.drivers[4].driver
        
        driver.variables.new()
        driver.expression = 'var'
        variables = driver.variables['var']
        variables.type = 'SINGLE_PROP'            
        targets = variables.targets[0]
        targets.id_type = 'WINDOWMANAGER'
        targets.id = D.window_managers["WinMan"]
        targets.data_path = 'shear'
    
    s_b_l = wm.s_b_l
    s_b_w = wm.s_b_w
    def text_add(type):        
        
        l_in_w = 0
        word = 0
        for i in text:
            if i == ' ':
                l_in_w = 0
                word += 1
                continue
            bpy.ops.object.text_add(location=(0,0,0))
            obj = C.active_object           
            
            bpy.ops.object.editmode_toggle()
            bpy.ops.font.delete(type='ALL')
            bpy.ops.font.text_insert(text=i)
            bpy.ops.object.editmode_toggle()
            
            if wm.text_font:
                obj.data.font = bpy.data.fonts.load(wm.text_font)
            
            if type == 'WIRE':               
                obj.draw_type = type
                obj.hide_render = True
                wm.list_end += ' '+str(obj.name)
                name_parent = wm.name_end
            else:
                name_parent = wm.name_start
                wm.list_start += ' '+str(obj.name)
                if not word and not l_in_w:        
                    obj.active_material = D.materials.new('Anim_text_materials')
                    name_material = obj.active_material.name
                else:
                    obj.active_material = D.materials[name_material]
                                            
            C.scene.cursor_location = (0,0,0)
            bpy.context.object.data.align = 'CENTER'
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            C.scene.cursor_location.x = obj.location.x
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            
            if l_in_w:
                obj.location.x = dimensions+s_b_l+obj.dimensions[0]/2
            else:
                if word:
                    obj.location.x = dimensions+s_b_w+obj.dimensions[0]/2
                else:
                    obj.location.x = 0
                    
            obj.start_location_x = obj.location.x
                    
            driver_text_geometry(obj)
            
            driver('location',obj,name_parent)
            driver('rotation_euler',obj,name_parent)
            driver('scale',obj,name_parent)
                
            dimensions = obj.dimensions[0]/2+obj.location.x
            
            l_in_w += 1
            
    text_add('WIRE')
    text_add('SOLID')
    
    C.scene.cursor_location = (0,0,0)    

def animation():
    def insert_keyframe():
        i.keyframe_insert('location')
        i.keyframe_insert('rotation_euler')
        i.keyframe_insert('scale')
        
    def interpolation_type(inter,easing,back,amplitude,period):
        fcurves = anim.fcurves[count]
        k = len(fcurves.keyframe_points.items())
        for j in range(k-2,k):
            fcurves.keyframe_points[j].interpolation = inter
            fcurves.keyframe_points[j].easing = easing
            if inter == 'BACK':
                fcurves.keyframe_points[j].back = back[0]
            elif inter == 'ELASTIC':
                fcurves.keyframe_points[j].amplitude = amplitude[0]
                fcurves.keyframe_points[j].period = period[0]
                
        fcurves = anim.fcurves[count+1]
        k = len(fcurves.keyframe_points.items())
        for j in range(k-2,k):
            fcurves.keyframe_points[j].interpolation = inter
            fcurves.keyframe_points[j].easing = easing
            if inter == 'BACK':
                fcurves.keyframe_points[j].back = back[1]
            elif inter == 'ELASTIC':
                fcurves.keyframe_points[j].amplitude = amplitude[1]
                fcurves.keyframe_points[j].period = period[1]
                
        fcurves = anim.fcurves[count+2]
        k = len(fcurves.keyframe_points.items())
        for j in range(k-2,k):
            fcurves.keyframe_points[j].interpolation = inter
            fcurves.keyframe_points[j].easing = easing
            if inter == 'BACK':
                fcurves.keyframe_points[j].back = back[2]
            elif inter == 'ELASTIC':
                fcurves.keyframe_points[j].amplitude = amplitude[2]
                fcurves.keyframe_points[j].period = period[2]
   
    C = bpy.context
    D = bpy.data
    
    list_start = [D.objects[i] for i in wm.list_start[1:].split(' ')]
    list_end = [D.objects[i] for i in wm.list_end[1:].split(' ')]
    
    direction_list = []
    
    direction_list = []
    if wm.derection == {'right'}:
        for i in range(len(list_start)-1,-1,-1):
            direction_list.append(list_start[i])
    else:
        direction_list += list_start
        
    if wm.derection == {'random'}:
        random.shuffle(direction_list)
        
    start_frame = wm.start_frame_ft
    
    for i in direction_list:
        i.driver_remove('location')
        i.driver_remove('rotation_euler')
        i.driver_remove('scale')
        
        C.scene.frame_current = start_frame
        insert_keyframe()
        
        C.scene.frame_current = start_frame+wm.speed*C.scene.render.fps
        i.location = list_end[list_start.index(i)].location
        i.rotation_euler = list_end[list_start.index(i)].rotation_euler
        i.scale = list_end[list_start.index(i)].scale
        insert_keyframe()
        
        anim = i.animation_data.action
        
        count = 0
        interpolation_type(wm.interpol_l,wm.easing_l,wm.back_l,wm.amplitude_l,wm.period_l)
                    
        count = 3
        interpolation_type(wm.interpol_r,wm.easing_r,wm.back_r,wm.amplitude_r,wm.period_r)
        
        count = 6
        interpolation_type(wm.interpol_s,wm.easing_s,wm.back_s,wm.amplitude_s,wm.period_s)
        
        if wm.assymetry_random:
            step_frame_assymetry = random.randint(wm.min_st_frame,wm.max_st_frame)
        else:
            step_frame_assymetry = wm.step_frame_assymetry
                                                 
        start_frame += step_frame_assymetry
        
class AddText(Operator):
    bl_idname = 'anim.font'
    bl_label = ''
    bl_description = 'Добавление текста'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        add_text(wm.text)
        bpy.context.area.type = 'VIEW_3D'
        return{'FINISHED'}
    
class UpdateText(Operator):
    bl_idname = 'anim.font_update'
    bl_label = ''
    bl_description = 'Обновление текста'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        D = bpy.data        
        
        list_start = [D.objects[i] for i in wm.list_start[1:].split(' ')]
        list_end = [D.objects[i] for i in wm.list_end[1:].split(' ')]
        
        list_obj = list_start+list_end
        
        for i in list_obj:
            i.data.offset = wm.offset        
        return{'FINISHED'}
    
class DeleteText(Operator):
    bl_idname = 'anim.font_delete'
    bl_label = ''
    bl_description = 'Удаление текста'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        D = bpy.data        
        
        list_start = [D.objects[i] for i in wm.list_start[1:].split(' ')]
        list_end = [D.objects[i] for i in wm.list_end[1:].split(' ')]
        
        list_obj = list_start+list_end
        
        bpy.ops.object.select_all(action='DESELECT')
        
        for i in list_obj:
            i.select = True
        D.objects[wm.name_end].select = True 
        D.objects[wm.name_start].select = True
        bpy.ops.object.delete(use_global=False)
        return{'FINISHED'}
    
class AnimationText(Operator):
    bl_idname = 'anim.font_anim'
    bl_label = ''
    bl_description = 'Удаление текста'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        animation()
        return{'FINISHED'}
    
class TransformText(Operator):
    bl_idname = 'anim.font_trans'
    bl_label = ''
    bl_description = 'Создание анимации'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self,context):
        D = bpy.data
        
        list_start = [D.objects[i] for i in wm.list_start[1:].split(' ')]
               
        for i in list_start:
            driver('location',i,wm.name_start)
            driver('rotation_euler',i,wm.name_start)
            driver('scale',i,wm.name_start)
                    
        bpy.context.area.type = 'VIEW_3D'
        
        return{'FINISHED'}
    
class DeleteLastAnimation(Operator):
    bl_idname = 'anim.font_anim_del'
    bl_label = ''
    bl_description = 'Удаление анимации'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self,context):
        D = bpy.data
        
        list_start = [D.objects[i] for i in wm.list_start[1:].split(' ')]
        
        bpy.ops.object.select_all(action='DESELECT')
        
        bpy.context.area.type = 'GRAPH_EDITOR'
        bpy.context.space_data.mode = 'FCURVES'
                                         
        for i in list_start:
            i.select = True
            bpy.ops.graph.select_all_toggle(invert=False)            
            for j in range(9):
                k = len(i.animation_data.action.fcurves[j].keyframe_points.items())
                i.animation_data.action.fcurves[j].keyframe_points[k-1].select_control_point = True
                i.animation_data.action.fcurves[j].keyframe_points[k-2].select_control_point = True
            bpy.ops.graph.delete()
                    
        bpy.context.area.type = 'VIEW_3D'
        
        return{'FINISHED'}
    
def register():
    bpy.utils.register_class(AddTextPanel)
    bpy.utils.register_class(AddText)
    
    bpy.utils.register_class(UpdateText)
    bpy.utils.register_class(DeleteText)
    
    bpy.utils.register_class(AnimationTextPanel)
    bpy.utils.register_class(AnimationText)
    
    bpy.utils.register_class(DeleteLastAnimation)
    bpy.utils.register_class(TransformText)
    

def unregister():
    bpy.utils.unregister_class(AddTextPanel)
    bpy.utils.unregister_class(AddText)
    
    bpy.utils.unregister_class(UpdateText)
    bpy.utils.unregister_class(DeleteText)
    
    bpy.utils.unregister_class(AnimationTextPanel)
    bpy.utils.unregister_class(AnimationText)
    
    bpy.utils.unregister_class(DeleteLastAnimation)
    bpy.utils.unregister_class(TransformText)

if __name__ == "__main__":
    register()                   
