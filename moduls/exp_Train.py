#export training samples with arcpy env
#for this function, you only have to set the output location
#activat with exportTrainingSamplesSSD(outLocation = 'blabla',input_layer="something" )
def exportTrainingSamplesSSD(workspace = r'C:\Users\urial\DeepLearningProjects\mashhetot\mashhetot.gdb',
                             outLocation='',
                             in_raster='tif',
                             input_layer = '',
                             image_chip_format='TIFF',
                             tile_size_x='448',
                             tile_size_y='448',
                             stride_x='128',
                             stride_y='128',
                             output_nofeature_tiles='ONLY_TILES_WITH_FEATURES',
                             metadata_format='PASCAL_VOC_rectangles',
                             start_index='0',
                             class_value_field='Classvalue',
                             buffer_radius='0',
                             in_mask_polygons=None,
                             rotation_angle='90'):
    arcpy.env.workspace = workspace #create a work space
    output_location = outLocation #set out put location for the samples
    #export oparation
    arcpy.ia.ExportTrainingDataForDeepLearning(in_raster=in_raster,
                                               out_folder= outLocation,
                                               in_class_data=input_layer,
                                               image_chip_format=image_chip_format,
                                               tile_size_x=tile_size_x,
                                               tile_size_y=tile_size_y,
                                               stride_x=stride_x,
                                               stride_y=stride_y,
                                               output_nofeature_tiles=output_nofeature_tiles,
                                               metadata_format=metadata_format,
                                               start_index=start_index,
                                               class_value_field=class_value_field,
                                               buffer_radius=buffer_radius,
                                               in_mask_polygons=in_mask_polygons,
                                               rotation_angle=rotation_angle)
    arcpy.ClearEnvironment("workspace")
    
    def exportCheck(FolderPAth):
        files_in_folder = os.listdir(FolderPAth)
        needed_files = ['esri_accumulated_stats.json','esri_model_definition.emd','images','labels','map.txt','stats.txt']
        for i in needed_files:
            if i in files_in_folder:
                print('the file: {} found in folder'.format(i))
                continue

            else:
                print('Not all files created as should. please check and repeat the process')
                break
    print('Export training samples completed the output location:\n{}'.format(outLocation))
    print('Checking for appropriate file structure...')
    
    exportCheck(outLocation)
    
