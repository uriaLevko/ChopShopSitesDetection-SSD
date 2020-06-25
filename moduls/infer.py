#function for SSD detection
#only enter output layer and model path
def detectObjects_arcpy(workspace = r"C:\Users\urial\DeepLearningProjects\mashhetot\mashhetot.gdb",
                  extent = arcpy.Extent(198206.573316857, 689300.881492417, 199070.473746703, 690255.718809615),
                 full_detection_raster_path = r"\\gis-rocket\e$\Kenes2019\ML\Ortophoto examples.ecw",
                  name_of_result_layer="",
                  full_model_path="",
                  arguments = "padding 0;threshold 0.4;nms_overlap 0.1;batch_size 64",
                  nms = "NMS",
                  confidence_score_field = "Confidence",
                  class_value_field="Class",
                  max_overlap_ratio=0.1):
    
    """
    activate with:
    | PUT_variable_name_here = detectObjects_arcpy(name_of_result_layer = 'insert',full_model_path = 'insert') |
       other variables have defaults
       """
    
    arcpy.env.workspace = workspace
    
    arcpy.env.extent = extent
    
    arcpy.ia.DetectObjectsUsingDeepLearning(in_raster = full_detection_raster_path,
                                            out_detected_objects = name_of_result_layer,
                                            in_model_definition = full_model_path,
                                            arguments = arguments,
                                            run_nms = nms,
                                            confidence_score_field = confidence_score_field,
                                            class_value_field = class_value_field,
                                            max_overlap_ratio = max_overlap_ratio)
    arcpy.ClearEnvironment("workspace")
    
    return name_of_result_layer
