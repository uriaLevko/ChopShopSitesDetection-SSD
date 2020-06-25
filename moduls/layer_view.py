def Access_and_view_layer(layerName = '',colunmAnalyze = 'Classname',arc_env = ''):
    arcpy.env.workspace = f'r"{arc_env}"'
    layer1 = GeoAccessor.from_featureclass(layerName)
    m1 = GIS().map(location = 'kalanswa',zoomlevel=11)
    layer1.spatial.plot(map_widget= m1,renderer_type='u',col=colunmAnalyze)
    arcpy.ClearEnvironment("workspace")
    return(layer1,m1)
