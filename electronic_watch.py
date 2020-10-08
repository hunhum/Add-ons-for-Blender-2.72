bl_info = {
    "name": "electronic_watсh",
    "author": "Baklanov Ilya",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "location": "Tool bar > Watсh > Електронные часы",
    "description": "Анимация циферблата электронных часов",
    "category": "Animation"
}

import bpy
from bpy.types import Panel, Operator
from bpy.props import*
#
#Определение своств
#
wm = bpy.context.window_manager
bpy.types.WindowManager.start_days = IntProperty(
    name = 'Дни',
    default = 0,
    soft_min = 0,
    description = "Начальное значение дне")
wm.start_days = 0

bpy.types.WindowManager.start_hours = IntProperty(
    name = 'Часы',
    default = 0,
    soft_min = 0,
    soft_max = 23,
    description = "Начальное значение часов")
wm.start_hours = 0

bpy.types.WindowManager.start_minutes = IntProperty(
    name = 'Минуты',
    default = 0,
    soft_min = 0,
    soft_max = 59,
    description = "Начальное значение минут")
wm.start_minutes = 0

bpy.types.WindowManager.start_seconds = IntProperty(
    name = 'Секунды',
    default = 0,
    soft_min = 0,
    soft_max = 59,
    description = "Начальное значение секунд")
wm.start_seconds = 0

wm = bpy.context.window_manager
bpy.types.WindowManager.end_days = IntProperty(
    name = 'Дни',
    default = 0,
    soft_min = 0,
    description = "Конечное значение дне")
wm.start_days = 0

bpy.types.WindowManager.end_hours = IntProperty(
    name = 'Часы',
    default = 0,
    soft_min = 0,
    soft_max = 23,
    description = "Конечное значение часов")
wm.start_hours = 0

bpy.types.WindowManager.end_minutes = IntProperty(
    name = 'Минуты',
    default = 0,
    soft_min = 0,
    soft_max = 59,
    description = "Конечное значение минут")
wm.end_minutes = 0

bpy.types.WindowManager.end_seconds = IntProperty(
    name = 'Секунды',
    default = 0,
    soft_min = 0,
    soft_max = 59,
    description = "Конечное значение значение секунд")
wm.end_seconds = 0

bpy.types.WindowManager.hours = BoolProperty(
    name = 'Часы')
wm.hours = True

bpy.types.WindowManager.minutes = BoolProperty(
    name = 'Минуты')
wm.minutes= True

bpy.types.WindowManager.seconds = BoolProperty(
    name = 'Секунды')
wm.seconds = True

bpy.types.WindowManager.fps = IntProperty(
    name='Кол-во кадров в секунду',
    soft_min = 1)
wm.fps = 24

bpy.types.WindowManager.second_step = IntProperty(
    name = '',
    soft_min = 1)
wm.second_step = 1    

bpy.types.WindowManager.minutes_step = IntProperty(
    name='',
    soft_min = 1)
wm.minutes_step = 1
 
bpy.types.WindowManager.hours_step = IntProperty(
    name='',
    soft_min = 1)
wm.hours_step = 1

bpy.types.WindowManager.start_frame = IntProperty(
    name='Кадр начала анимации',
    soft_min = 0)
    
bpy.types.WindowManager.fps = IntProperty(
    name='Кол-во кадров в секунду',
    soft_min = 0)
wm.fps = 24
#Секунды цифра 1
bpy.types.WindowManager.offset_s1 = FloatProperty(
    name='Offset',
    soft_min = -1,
    soft_max = 1)
wm.offset_s1 = 0
    
bpy.types.WindowManager.extrude_s1 = FloatProperty(
    name='Extrude',
    soft_min = 0)
wm.extrude_s1 = 0
    
bpy.types.WindowManager.depth_s1 = FloatProperty(
    name='Depth',
    soft_min = 0)
wm.depth_s1 = 0

bpy.types.WindowManager.resolution_s1 = IntProperty(
    name='Resolution',
    soft_min = 0,
    soft_max = 32)
wm.resolution_s1 = 0
#Секунды вторая цифра
bpy.types.WindowManager.offset_s2 = FloatProperty(
    name='Offset',
    soft_min = -1,
    soft_max = 1)
wm.offset_s2 = 0
    
bpy.types.WindowManager.extrude_s2 = FloatProperty(
    name='Extrude',
    soft_min = 0)
wm.extrude_s2 = 0
    
bpy.types.WindowManager.depth_s2 = FloatProperty(
    name='Depth',
    soft_min = 0)
wm.depth_s2 = 0

bpy.types.WindowManager.resolution_s2 = IntProperty(
    name='Resolution',
    soft_min = 0,
    soft_max = 32)
wm.resolution_s2 = 0
#Минуты цифра 1
bpy.types.WindowManager.offset_m1 = FloatProperty(
    name='Offset',
    soft_min = -1,
    soft_max = 1)
wm.offset_m1 = 0
    
bpy.types.WindowManager.extrude_m1 = FloatProperty(
    name='Extrude',
    soft_min = 0)
wm.extrude_m1 = 0
    
bpy.types.WindowManager.depth_m1 = FloatProperty(
    name='Depth',
    soft_min = 0)
wm.depth_m1 = 0

bpy.types.WindowManager.resolution_m1 = IntProperty(
    name='Resolution',
    soft_min = 0,
    soft_max = 32)
wm.resolution_m1 = 0
#Минуты вторая цифра
bpy.types.WindowManager.offset_m2 = FloatProperty(
    name='Offset',
    soft_min = -1,
    soft_max = 1)
wm.offset_m2 = 0
    
bpy.types.WindowManager.extrude_m2 = FloatProperty(
    name='Extrude',
    soft_min = 0)
wm.extrude_m2 = 0
    
bpy.types.WindowManager.depth_m2 = FloatProperty(
    name='Depth',
    soft_min = 0)
wm.depth_m2 = 0

bpy.types.WindowManager.resolution_m2 = IntProperty(
    name='Resolution',
    soft_min = 0,
    soft_max = 32)
wm.resolution_m2 = 0
#Часы первая цифра
bpy.types.WindowManager.offset_h1 = FloatProperty(
    name='Offset',
    soft_min = -1,
    soft_max = 1)
wm.offset_h1 = 0
    
bpy.types.WindowManager.extrude_h1 = FloatProperty(
    name='Extrude',
    soft_min = 0)
wm.extrude_h1 = 0
    
bpy.types.WindowManager.depth_h1 = FloatProperty(
    name='Depth',
    soft_min = 0)
wm.depth_h1 = 0

bpy.types.WindowManager.resolution_h1 = IntProperty(
    name='Resolution',
    soft_min = 0,
    soft_max = 32)
wm.resolution_h1 = 0
#Часы вторая цифра
bpy.types.WindowManager.offset_h2 = FloatProperty(
    name='Offset',
    soft_min = -1,
    soft_max = 1)
wm.offset_h2 = 0
    
bpy.types.WindowManager.extrude_h2 = FloatProperty(
    name='Extrude',
    soft_min = 0)
wm.extrude_h2 = 0
    
bpy.types.WindowManager.depth_h2 = FloatProperty(
    name='Depth',
    soft_min = 0)
wm.depth_h2 = 0

bpy.types.WindowManager.resolution_h2 = IntProperty(
    name='Resolution',
    soft_min = 0,
    soft_max = 32)
wm.resolution_h2 = 0
    
bpy.types.WindowManager.filepath_s1 = StringProperty(
    name = 'Шрифт',
    subtype = 'FILE_PATH')
wm.filepath_s1 = ''
    
bpy.types.WindowManager.filepath_s2 = StringProperty(
    name = 'Шрифт',
    subtype = 'FILE_PATH')
wm.filepath_s2 = ''

bpy.types.WindowManager.filepath_m1 = StringProperty(
    name = 'Шрифт',
    subtype = 'FILE_PATH')
wm.filepath_m1 = ''
    
bpy.types.WindowManager.filepath_m2 = StringProperty(
    name = 'Шрифт',
    subtype = 'FILE_PATH')
wm.filepath_m2 = ''
    
bpy.types.WindowManager.filepath_h1 = StringProperty(
    name = 'Шрифт',
    subtype = 'FILE_PATH')
wm.filepath_h1 = ''

bpy.types.WindowManager.filepath_h2 = StringProperty(
    name = 'Шрифт',
    subtype = 'FILE_PATH')
wm.filepath_h2 = ''

bpy.types.WindowManager.sbn = FloatProperty(
    name = '',
    soft_min = 0)
wm.sbn = 0.5

bpy.types.WindowManager.sbd = FloatProperty(
    name = '',
    soft_min = 0)
wm.sbd = 1
                            
class ElectronicWatсhPanel(Panel):
    bl_label = "Електронные часы"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Watсh'
    bl_context = "objectmode"
    
    def draw(self, context):
        
        layout = self.layout
        
        sub = layout.row()
        sub.active = not(wm.hours and wm.seconds and not wm.minutes)
        sub.operator('anim.wath',text="Создать анимацию",icon='TIME')
            
        row = layout.row()
        row.label(text='Начальное значение времени')
        row = layout.row(align=True)
        row.prop(wm,'start_days')
        row.prop(wm,'start_hours')
        row.prop(wm,'start_minutes')
        row.prop(wm,'start_seconds')
        
        row = layout.row()
        row.label(text='Конечное значение времени')
        row = layout.row(align=True)
        row.prop(wm,'end_days')
        row.prop(wm,'end_hours')
        row.prop(wm,'end_minutes')
        row.prop(wm,'end_seconds')
        
        row = layout.row()
        row.prop(wm,'hours')
        row.prop(wm,'minutes')
        row.prop(wm,'seconds')
        
        if wm.second_step > wm.fps or wm.minutes_step > wm.fps*60 or wm.hours_step > wm.fps*3600:
            row = layout.row()
            row.label(text='Недопустимое значение',icon='ERROR')
            
        sub = layout.row()
        sub.active = wm.seconds
        sub.label(text='1 секунда = ')
        sub.prop(wm,'second_step')
        sub.label(text='секунд в Blender')
        
        sub = layout.row()
        sub.active = not wm.seconds and wm.minutes
        sub.label(text='1 минута = ')
        sub.prop(wm,'minutes_step')
        sub.label(text='минут в Blender')
        
        sub = layout.row()
        sub.active = not wm.seconds and not wm.minutes and wm.hours
        sub.label(text='1 час = ')
        sub.prop(wm,'hours_step')
        sub.label(text='часов в Blender')
        
        row = layout.row()
        row.prop(wm,'fps')
        
        row = layout.row()
        row.prop(wm,'start_frame')
        
        split = layout.split()
        col = split.column()
        col.label(text='Расстояние между цифрами')
        col.prop(wm,'sbn')
        
        col = split.column()
        col.label(text='Расстояние между разрядами')
        col.prop(wm,'sbd')
        
        row = layout.row()
        row.label(text='Перед созданием анимации нужно выставить шрифты',icon='ERROR')
                
        box = layout.box()
        box.label(text='Секунды')
        box_in_box = box.box()
        box_in_box.label(text='Первая цифра')
        
        row = box_in_box.row()
        row.prop(wm,'filepath_s1')
        
        split = box_in_box.split()
        
        col = split.column()
        col.label(text='Modification')
        col.prop(wm,'offset_s1')
        col.prop(wm,'extrude_s1')
        
        col = split.column()
        col.label(text='Bevel')
        col.prop(wm,'depth_s1')
        col.prop(wm,'resolution_s1')
        
        box_in_box = box.box()
        box_in_box.label(text='Вторая цифра')
        
        row = box_in_box.row()
        row.prop(wm,'filepath_s2')
        
        split = box_in_box.split()
        
        col = split.column()
        col.label(text='Modification')
        col.prop(wm,'offset_s2')
        col.prop(wm,'extrude_s2')
        
        col = split.column()
        col.label(text='Bevel')
        col.prop(wm,'depth_s2')
        col.prop(wm,'resolution_s2')
        
        box = layout.box()
        box.label(text='Минуты')
        box_in_box = box.box()
        box_in_box.label(text='Первая цифра')
        
        row = box_in_box.row()
        row.prop(wm,'filepath_m1')
        
        split = box_in_box.split()
        
        col = split.column()
        col.label(text='Modification')
        col.prop(wm,'offset_m1')
        col.prop(wm,'extrude_m1')
        
        col = split.column()
        col.label(text='Bevel')
        col.prop(wm,'depth_m1')
        col.prop(wm,'resolution_m1')
        
        box_in_box = box.box()
        box_in_box.label(text='Вторая цифра')
        
        row = box_in_box.row()
        row.prop(wm,'filepath_m2')
        
        split = box_in_box.split()
        
        col = split.column()
        col.label(text='Modification')
        col.prop(wm,'offset_m2')
        col.prop(wm,'extrude_m2')
        
        col = split.column()
        col.label(text='Bevel')
        col.prop(wm,'depth_m2')
        col.prop(wm,'resolution_m2')
        
        box = layout.box()
        box.label(text='Часы')
        box_in_box = box.box()
        box_in_box.label(text='Первая цифра')
        
        row = box_in_box.row()
        row.prop(wm,'filepath_h1')
        
        split = box_in_box.split()
        
        col = split.column()
        col.label(text='Modification')
        col.prop(wm,'offset_h1')
        col.prop(wm,'extrude_h1')
        
        col = split.column()
        col.label(text='Bevel')
        col.prop(wm,'depth_h1')
        col.prop(wm,'resolution_h1')
        
        box_in_box = box.box()
        box_in_box.label(text='Вторая цифра')
        
        row = box_in_box.row()
        row.prop(wm,'filepath_h2')
        
        split = box_in_box.split()
        
        col = split.column()
        col.label(text='Modification')
        col.prop(wm,'offset_h2')
        col.prop(wm,'extrude_h2')
        
        col = split.column()
        col.label(text='Bevel')
        col.prop(wm,'depth_h2')
        col.prop(wm,'resolution_h2')
                 
                       
def digit(number_system,start_time,
          end_time,frame_step,start_frame,
          position,space_between_obj,
          wm_offset,wm_extrude,
          wm_depth,wm_res,wm_font,
          wm_offset1,wm_extrude1,
          wm_depth1,wm_res1,wm_font1):
           
    bpy.ops.mesh.primitive_cube_add(location=(position,0,0))
    bpy.context.active_object.scale.z = 0.2
    bpy.context.active_object.draw_type = 'WIRE'
    name = bpy.context.active_object.name
    bpy.context.active_object.hide_render = True
    bpy.context.active_object.active_material = bpy.data.materials.new(name)
    name_materials = bpy.context.active_object.active_material.name    
    
    bpy.ops.mesh.primitive_cube_add(location=(position+space_between_obj,0,0))
    bpy.context.active_object.scale.z = 0.2
    bpy.context.active_object.draw_type = 'WIRE'
    name_second = bpy.context.active_object.name
    bpy.context.active_object.hide_render = True
    bpy.context.active_object.active_material = bpy.data.materials.new(name_second)
    name_second_materials = bpy.context.active_object.active_material.name
    
    def hide(frame,invers,obj):
        inv = True
        if invers == 1:
            inv = not inv                                                                 
        bpy.context.scene.frame_current = frame
        obj.hide = inv
        obj.hide_render = inv
        obj.keyframe_insert('hide')                
        obj.keyframe_insert('hide_render')
        bpy.context.scene.frame_current -= 1
        obj.hide = not inv
        obj.hide_render = not inv
        obj.keyframe_insert('hide')                
        obj.keyframe_insert('hide_render')
    
    def add_text(parent_obj,parent_obj_material,offset,extrude,depth,resolution,filepath):
        bpy.ops.object.text_add()
        obj = bpy.context.active_object
            
        bpy.ops.object.editmode_toggle()
        bpy.ops.font.delete(type='ALL')
        bpy.ops.font.text_insert(text=str(i))
        bpy.ops.object.editmode_toggle()
        obj.data.font = bpy.data.fonts.load(filepath)
        obj.data.offset = offset
        obj.data.extrude = extrude
        obj.data.bevel_depth = depth
        obj.data.bevel_resolution = resolution
        bpy.context.object.data.align = 'CENTER'
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        obj.location.y = bpy.data.objects[parent_obj].location.y
        obj.parent = bpy.data.objects[parent_obj]
        obj.active_material = bpy.data.materials[parent_obj_material]
                    
    if number_system == 60: 
        start_value = (start_time%60)%10
        end_value = (end_time%60)%10    
        for i in range(10):
            if end_time-start_time < 10:
                if i < start_value:
                    if i+10 > start_value+end_time-start_time:
                        continue
                else:
                    if i > start_value+end_time-start_time:
                        continue
                   
            frame_lock = frame_step*(10-(start_value-i))+start_frame
            if i >= start_value:
                frame_lock = frame_step*(i-start_value)+start_frame
                
            add_text(name_second,name_second_materials,wm_offset,wm_extrude,wm_depth,wm_res,wm_font)
            
            obj = bpy.context.active_object
           
            number_cycles = 0
            
            for k in range(start_time,end_time+1):
                if k%10 == i:
                    number_cycles += 1
                   
            for k in range(number_cycles):
                if not(i == end_value and k == number_cycles-1):         
                    hide(frame_lock+frame_step+1,0,obj)                
                if not(i == start_value and k == 0):
                    hide(frame_lock+1,1,obj)
                        
                frame_lock += frame_step*10
        #####################################
        start_frame_six = (10-(start_time%60)%10)*frame_step-frame_step*10    
        start_value = (start_time%60)//10
        end_value = (end_time%60)//10
        for i in range(6):
            
            list_znacheniy = [(j%60)//10 for j in range(start_time,end_time+1)]
            
            if not (i in list_znacheniy):
                continue
            
            frame_lock = frame_step*10*(6-(start_value-i))+start_frame+start_frame_six
            if i >= start_value:
                frame_lock = frame_step*10*(i-start_value)+start_frame+start_frame_six
            
            add_text(name,name_materials,wm_offset1,wm_extrude1,wm_depth1,wm_res1,wm_font1)
            
            obj = bpy.context.active_object
            
            number_cycles = 0
            
            for k in range(start_time//10,end_time//10+1):
                if k%6 == i:
                    number_cycles += 1
           
            for k in range(number_cycles):
                if  not(i == end_value and k == number_cycles-1):         
                    hide(frame_lock+frame_step*10+1,0,obj)
                if not(i == start_value and k == 0):
                    hide(frame_lock+1,1,obj)
                frame_lock += frame_step*60
    else:
        start_value = start_time%24
        end_value = end_time%24
        for i in range(24):
            if end_time-start_time < 24:
                if i < start_value:
                    if i+24 > start_value+end_time-start_time:
                        continue
                else:
                    if i > start_value+end_time-start_time:
                        continue
            frame_lock = frame_step*(24-(start_value-i))+start_frame
            if i >= start_value:
                frame_lock = frame_step*(i-start_value)+start_frame
                                                  
            bpy.ops.object.text_add()
            obj = bpy.context.active_object
            
            bpy.ops.object.editmode_toggle()
            bpy.ops.font.delete(type='ALL')
            bpy.ops.font.text_insert(text=str(i%10))
            bpy.ops.object.editmode_toggle()
            obj.data.font = bpy.data.fonts.load(wm_font)
            obj.data.offset = wm_offset
            obj.data.extrude = wm_extrude
            obj.data.bevel_depth = wm_depth
            obj.data.bevel_resolution = wm_res
            bpy.context.object.data.align = 'CENTER'
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            obj.location.y = bpy.data.objects[name_second].location.y
            obj.parent = bpy.data.objects[name_second]
            obj.active_material = bpy.data.materials[name_second_materials]
                                               
            number_cycles = 0
            
            obj = bpy.context.active_object
            
            for k in range(start_time,end_time+1):
                if k%24 == i:
                    number_cycles += 1
                    
            for k in range(number_cycles):
                if  not(i == end_value and k == number_cycles-1):         
                    hide(frame_lock+frame_step+1,0,obj)
                if not(i == start_value and k == 0):
                    hide(frame_lock+1,1,obj)
                frame_lock += frame_step*24
                
        start_value = (start_time%24)//10
        end_value = (end_time%24)//10
        if start_value == 2:
            start_frame_hours = frame_step*(4-((start_time%24)%10))-4*frame_step
        else:
            start_frame_hours = frame_step*(10-((start_time%24)%10))-10*frame_step
                    
        for i in range(3):
                
            list_znacheniy = [(j%24)//10 for j in range(start_time,end_time+1)]
            
            if not (i in list_znacheniy):
                continue
                    
            frame_lock = frame_step*10*(3-(start_value-i))+start_frame+start_frame_hours
            if i >= start_value:
                frame_lock = frame_step*10*(i-start_value)+start_frame+start_frame_hours
            if start_value == 2 and i != 2:
                frame_lock = frame_step*(10*(2+i-start_value)+4)+start_frame+start_frame_hours
            if i == 0 and start_value != 0:
                frame_lock = frame_step*((2-start_value)*10+4)+start_frame+start_frame_hours
            
            add_text(name,name_materials,wm_offset1,wm_extrude1,wm_depth1,wm_res1,wm_font1)
            
            obj = bpy.context.active_object
            
            frame_step_false = 10*frame_step
            if i == 2:
                    frame_step_false = 4*frame_step
                                               
            number_cycles = 0
            last_value = 0
            
            for k in range(start_time,end_time+1):
                if k != start_time and last_value == (k%24)//10:
                    continue
                if (k%24)//10 == i:
                    number_cycles += 1
                last_value = (k%24)//10
                    
            for k in range(number_cycles):
                if  not(i == end_value and k == number_cycles-1):         
                    hide(frame_lock+frame_step_false+1,0,obj)
                if not(i == start_value and k == 0):
                    hide(frame_lock+1,1,obj)
                frame_lock += frame_step*24
               
           
                                                                                                                                            
def clock():
    
    space_between_obj = wm.sbn
    space_between_digit = wm.sbd
    position = space_between_digit
    
    start_value = wm.start_days*24*3600+wm.start_hours*3600+wm.start_minutes*60+wm.start_seconds
    end_value = wm.end_days*24*3600+wm.end_hours*3600+wm.end_minutes*60+wm.end_seconds
    
    frame_step = wm.fps//wm.second_step
    frame_step_min = 60*frame_step
    frame_step_hours = 60*frame_step_min
    
    start_frame = wm.start_frame
              
    seconds = wm.seconds
    minutes = wm.minutes
    hours = wm.hours
    
    if seconds == False:
        if minutes == True:
            frame_step_min = 60*wm.fps//wm.minutes_step
            frame_step_hours = 60*frame_step_min
        else:
            frame_step_hours = 3600*wm.fps//wm.hours_step
            
    if seconds == True:
        position -= space_between_digit
        digit(60,start_value,
              end_value,frame_step,
              start_frame,position,
              space_between_obj,
              wm.offset_s1,wm.extrude_s1,
              wm.depth_s1,wm.resolution_s1,
              wm.filepath_s1,wm.offset_s2,
              wm.extrude_s2,
              wm.depth_s2,wm.resolution_s2,
              wm.filepath_s2)
              
    if minutes == True:
        if seconds == True:
            start_frame_min = start_frame+frame_step*(60-start_value%60)-frame_step_min
        else:
            start_frame_min = start_frame
        position -= space_between_digit
        digit(60,start_value//60,
              end_value//60,frame_step_min,
              start_frame_min,position,
              space_between_obj,
              wm.offset_m1,wm.extrude_m1,
              wm.depth_m1,wm.resolution_m1,
              wm.filepath_m1,wm.offset_m2,
              wm.extrude_m2,
              wm.depth_m2,wm.resolution_m2,
              wm.filepath_m2)
    if hours == True:
        if minutes == True:
             start_frame_hours = start_frame_min+frame_step_min*(60-(start_value//60)%60)-frame_step_hours
        else:
            start_frame_hours = start_frame
        position -= space_between_digit
        digit(24,start_value//3600,
              end_value//3600,frame_step_hours,
              start_frame_hours,position,
              space_between_obj,
              wm.offset_h1,wm.extrude_h1,
              wm.depth_h1,wm.resolution_h1,
              wm.filepath_h1,wm.offset_h2,
              wm.extrude_h2,
              wm.depth_h2,wm.resolution_h2,
              wm.filepath_h2)
                                 
class ElectronicWatсh(Operator):
    bl_idname = 'anim.wath'
    bl_label = ''
    bl_description = 'Создание аудиовизуализации'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self,context):
        clock()
        return{'FINISHED'}

def register():
    bpy.utils.register_class(ElectronicWatсhPanel)
    bpy.utils.register_class(ElectronicWatсh)

def unregister():
    bpy.utils.unregister_class(ElectronicWatсhPanel)
    bpy.utils.unregister_class(ElectronicWatсh)

if __name__ == "__main__":
    register()     
