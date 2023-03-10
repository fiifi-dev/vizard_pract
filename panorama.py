import viz

viz.setMultiSample(4)
viz.fov(60)
viz.go()

env = viz.addEnvironmentMap('townhall_L.jpg')

sky = viz.addCustomNode('skydome.dlc')
sky.texture(env)
