from energydiagram import ED
import matplotlib.pyplot as plt
a = ED()
a.add_level(0, 'Separated Reactants')
a.add_level(-5.4, 'mlC1')
a.add_level(-15.6, 'mlC2', 'last',)
a.add_level(28.5, 'mTS1', color='g')
a.add_level(-9.7, 'mCARB1')
a.add_level(-19.8, 'mCARB2', 'last')
a.add_level(20, 'mCARBX', 'last')
a.add_link(0, 1, color='r')
a.add_link(0, 2)
a.add_link(2, 3, color='b')
a.add_link(1, 3)
a.add_link(3, 4, color='g')
a.add_link(3, 5)
a.add_link(0, 6)
a.add_electronbox(level_id=0, boxes=1, electrons=2, side=3, spacing_f=3)
a.add_electronbox(3, 3, 1, 3, 3)
a.add_electronbox(5, 3, 5, 3, 3)
a.add_arrow(6, 4)
a.offset *= 2
a.plot(show_IDs=True)
plt.show()