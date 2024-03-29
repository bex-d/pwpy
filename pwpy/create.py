from pointwise import GlyphClient
from pointwise.glyphapi import *
     
def createCon(pw,points=[[0,0,0]],linetype='con',seg="spline",slope='CatmullRom',shoulder=0,center=0,plane=(0,0,1),endAngle=0,setAngle=0,flipArc=0):
    #input point: [point] [point1,point2] [[x1,y1,z1][x2,y2,z2]]  
    #seg: "SegmentSpline", " SegmentConic"  
    #Slope: Linear, CatmullRom
    with pw.Application.begin("Create") as creator:
        if seg == "SegmentSpline" or seg=="Spline" or seg=="spline":
            seg = pw.SegmentSpline.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentConic" or seg=="Conic" or seg=="conic":
            seg = pw.SegmentConic.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentCircle" or seg=="Circle" or seg == "circle":
            seg = pw.SegmentCircle.create()
            for point in points:
                seg.addPoint(point)
            if shoulder!=0:
                seg.setShoulderPoint(shoulder)
            elif center!=0:
                seg.setCenterPoint(center,plane)
            elif setAngle!=0:
                seg.setAngle(setAngle)
            elif endAngle!=0:
                seg.setEndAngle(endAngle)

        else:
            print('Incorrect segment type: {}'.format(seg))
            
        if flipArc==1:
            seg.flipArc()

        con = pw.Connector.create()
        con.addSegment(seg)
        con.calculateDimension()
        return con
  
def createCurve(pw,points=[[0,0,0]],seg="spline",slope=0,shoulder=0,center=0,plane=(0,0,1),endAngle=0,angle=0):
    #input point: [point] [point1,point2] [[x1,y1,z1][x2,y2,z2]]  
    #seg: "SegmentSpline", " SegmentConic"  
    #Slope: Linear, CatmullRom
    # angle: [angle,normal]
    with pw.Application.begin("Create") as creator:
        if seg == "SegmentSpline" or seg=="Spline" or seg=="spline":
            seg = pw.SegmentSpline.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentConic" or seg=="Conic" or seg=="conic":
            seg = pw.SegmentConic.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentCircle" or seg=="Circle" or seg == "circle":
            seg = pw.SegmentCircle.create()
            for point in points:
                seg.addPoint(point)
            if shoulder!=0:
                seg.setShoulderPoint(shoulder)
            elif center!=0:
                seg.setCenterPoint(center,plane)
            elif endAngle!=0:
                seg.setEndAngle(endAngle)
            elif angle!=0:
                if type(angle) == list:
                    seg.setAngle(angle[0],angle[1])
                else:
                    seg.setAngle(angle)
            if slope != 0:
                seg.setSlope(slope)

        else:
            print('Incorrect segment type: {}'.format(seg))

        db = pw.Curve.create()
        db.addSegment(seg)
        return db
       
def createSource(pw,seg="spline",slope=0,points=[[0,0,0]],shoulder=0,center=0,plane=(0,0,1),endAngle=0):
    #input point: [point] [point1,point2] [[x1,y1,z1][x2,y2,z2]]  
    #seg: "SegmentSpline", " SegmentConic"  
    #Slope: Linear, CatmullRom
    with pw.Application.begin("Create") as creator:
        if seg == "SegmentSpline" or seg=="Spline" or seg=="spline":
            seg = pw.SegmentSpline.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentConic" or seg=="Conic" or seg=="conic":
            seg = pw.SegmentConic.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentCircle" or seg=="Circle" or seg == "circle":
            seg = pw.SegmentCircle.create()
            for point in points:
                seg.addPoint(point)
            if shoulder!=0:
                seg.setShoulderPoint(shoulder)
            elif center!=0:
                seg.setCenterPoint(center,plane)
            elif endAngle!=0:
                seg.setEndAngle(endAngle)
            if slope != 0:
                seg.setSlope(slope)

        else:
            print('Incorrect segment type: {}'.format(seg))

        src = pw.SourceCurve.create()
        src.addSegment(seg)
        return src            
  
def createDom(pw,ents,gridtype='Unstructured'):
    #copy format examples from matlab_coord_example

    try:
        ent = ents[0]
        ent = ent[0]
    except:
        ent = ents[0]

    if 'con-' in ent.getName():
        if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
            pw.Application.setGridPreference('Unstructured')
            doms = pw.DomainUnstructured.createFromConnectors(ents) 
        elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
            pw.Application.setGridPreference('Structured')
            doms = pw.DomainStructured.createFromConnectors(ents) 
        else:
            print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))

    else:
        if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
            pw.Application.setGridPreference('Unstructured')
            doms = pw.DomainUnstructured.createOnDatabase(ents) 
        elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
            pw.Application.setGridPreference('Structured')
            doms = pw.DomainStructured.createOnDatabase(ents) 
        else:
            print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))
        
    return doms
      

def createConsOnDatabase(pw,ents,gridtype='Unstructured'):
    # try:
        # ent = ents[0]
        # ent = ent[0]
    # except:
        # ent = ents[0]

    # if 'con-' in ent.getName():
        # if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
            # pw.Application.setGridPreference('Unstructured')
            # doms = pw.DomainUnstructured.createFromConnectors(ents) 
        # elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
            # pw.Application.setGridPreference('Structured')
            # doms = pw.DomainStructured.createFromConnectors(ents) 
        # else:
            # print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))

    # else:
    if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
        pw.Application.setGridPreference('Unstructured')
        cons = pw.Connector.createOnDatabase(ents) 
    elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
        pw.Application.setGridPreference('Structured')
        cons = pw.Connector.createOnDatabase(ents) 
    else:
        print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))
        
    return cons      

      
def createFarfield(pw,ents,shape='Sphere',size=[],BCs=[]):
    # BCs = [['bcname2',[ents]],['bcname2',[ents]]]
    with pw.Application.begin('VolumeMesher',ents) as mesher:
        mesher.setFarfieldShapeType(shape)
        mesher.setFarfieldRadius(size)
        for BC in BCs:
            mesher.addBoundaryConditionFilter()
            mesher.setBoundaryConditionFilterName('bcf-1',BC[0])
            mesher.setBoundaryConditionFilterAdaptation(BC[0],'Off')
            mesher.setBoundaryConditionFilterPatterns(BC[0],BC[1])
            
        mesher.createGridEntities()
        mesher.end()
        
def createDomainFromConnectors(pw,ents,gridtype='Unstructured'):
      
    if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
        pw.Application.setGridPreference('Unstructured')
        doms = pw.DomainUnstructured.createFromConnectors(ents)
    elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
        pw.Application.setGridPreference('Structured')
        doms = pw.DomainStructured.createFromConnectors(ents)
    else:
        print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))
        
    return doms      

def patch(pw,ent):
    
    with pw.Application.begin('SurfaceFit') as patcher:
        surface = patcher.createSurfacesFromCurves(ent)
        patcher.setBoundaryTolerance(pw.Database.getFitTolerance())
        patcher.setUseBoundaryTangency(False)
        
    return surface
