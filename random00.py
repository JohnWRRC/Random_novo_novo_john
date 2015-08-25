# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:17:09 2015

@author: john

                
                #cursor.updateRow([[row[0][0] + (resultadoX or 0),row[0][1] + (resultadoX or 0)]])
                contador_rnd_point=contador_rnd_point+1
     
    

class principal(funcArcpy):
    def __init__(self,mapa_original,limite):
        funcArcpy.__init__(self)
        self.mapa_vegetation=mapa_original
        self.mapa_limite=limite
        self.x_pnt,self.y_pnt,self.x_frag,self.x_frag='','','',''
    def FuncsArcpy(self):    
        funcArcpy.createDb(self)
        funcArcpy.createRandomPoint(self)
        self.x_frag,self.y_frag=funcArcpy.get_XfragYfrag(self)
        self.x_pnt,self.y_pnt=funcArcpy.get_xpnt_ypnt(self)
        
       
        
        
pc=principal("frags_SJ_MN_export_dissolv - Copy","Limite_SJ_MN")
pc.get_XfragYfrag()    
        
    

        
        
        
        
    




resultadoX=x_pnt-x_frag
resultadoY=y_pnt-y_frag

arcpy.CreateRandomPoints_management(pacth_files, 'pnt_rnd',"Limite_SJ_MN", '', x, '0 Meters', 'POINT', '0')
def shift_features(in_features):
    
    """
    Shifts features by an x and/or y value. The shift values are in
    the units of the in_features coordinate system.
 
    Parameters:
    in_features: string
        An existing feature class or feature layer.  If using a
        feature layer with a selection, only the selected features
        will be modified.
 
    x_shift: float
        The distance the x coordinates will be shifted.
 
    y_shift: float
        The distance the y coordinates will be shifted.
    """
    
    with arcpy.da.UpdateCursor(in_features, ['SHAPE@XY']) as cursor:
        contador_rnd_point=0
        for row in cursor:
            
            resultadoX=x_pnt-x_frag
            resultadoY=y_pnt-y_frag
            
            cursor.updateRow([[row[0][0] + (x_shift or 0),row[0][1] + (y_shift or 0)]])
 
    return


    
cont_lines=arcpy.GetCount_management("frags_SJ_MN_export_dissolv - Copy")
x=int(x[0])

arcpy.AddGeometryAttributes_management('pnt_rnd', 'POINT_X_Y_Z_M', '#', '#', '#')

class random():
    def __ini__(self):
        pass

    
