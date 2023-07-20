from pxr import Sdf


root_layer: Sdf.Layer = stage.GetRootLayer()
sub_layer: Sdf.Layer = Sdf.Layer.CreateNew(r"C:/path/to/sublayer.usd")
# You can use standard python list.insert to add the subLayer to any position in the list
root_layer.subLayerPaths.append(sub_layer.identifier)