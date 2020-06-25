def Access_and_view_layer(layerName = '',colunmAnalyze = 'Classname',arc_env = '',online_url='https://xyz.maps.arcgis.com',user_name = 'xyz',password = 'xyz'):
    """
    connects to agol.
    sets a map and feature data.
    return the layer and the map by: 
    layer,map =  Access_and_view_layer(var1,var2,var3)
    
    """
    gis = GIS(online_url,user_name,password)
    arcpy.env.workspace = f'r"{arc_env}"'
    layer1 = GeoAccessor.from_featureclass(layerName)
    m1 = GIS().map(location = 'israel',zoomlevel=11)
    layer1.spatial.plot(map_widget= m1,renderer_type='u',col=colunmAnalyze)
    arcpy.ClearEnvironment("workspace")
    return(layer1,m1)
