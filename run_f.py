from src import one_plot as op
from src import all_plot as ap
from src import best_plot as bp
from src import cv_plot as cp
from matplotlib import cm
blue = cm.get_cmap('PuBu_r', 10)(range(9))
red = cm.get_cmap('PuRd_r', 10)(range(9))
green = cm.get_cmap('BuGn_r', 10)(range(9))
set = ['red','blue','forestgreen','gold','dimgray','blueviolet']

# location2 = ['Al_HfO2(O2_2)_Si 2 100 WO','Al_HfO2(O2_4)_Si 2 100 WO','Al_HfO2(O2_6)_Si 2 100 WO',
# 'Al_HfO2(O2_2)_Si 2 100 300','Al_HfO2(O2_4)_Si 2 100 300','Al_HfO2(O2_6)_Si 2 100 300',
# 'Al_ZrO2(O2_2)_Si 2 100 WO','Al_ZrO2(O2_4)_Si 2 100 WO','Al_ZrO2(O2_6)_Si 2 100 WO',
# 'Al_ZrO2(O2_2)_Si 2 100 500','Al_ZrO2(O2_4)_Si 2 100 500','Al_ZrO2(O2_6)_Si 2 100 500',
# 'Al_Al2O3(O2_2)_Si 2 100 WO','Al_Al2O3(O2_4)_Si 2 100 WO','Al_Al2O3(O2_6)_Si 2 100 WO',
# 'Al_Al2O3(O2_2)_Si 2 100 500','Al_Al2O3(O2_4)_Si 2 100 500','Al_Al2O3(O2_6)_Si 2 100 500']

location2 = ['Al_HfO2','Al_ZrO2','Al_Al2O3']

# location2 = ['Al_HfO2_Si 2 100','Al_ITZO_HfO2_Si 2 100','Al_Al2O3_Si 2 100','Al_ZrO2_Si 2 100']

# location2 = ['Al_ITZO_HfO2_Si 2 100']

# location2 = ['Al_ZrO2_Si 2 100 300','Al_ZrO2_Si 2 100 500','Al_ZrO2_Si 2 100 700','Al_ZrO2_Si 2 100 X']

# location2 = ['Al2O3_IV']

# location = [['Al_HfO2(O2_2)_Si 10 100 X',1],['Si_HfO2_Al 10 75 100',0],['Si_HfO2_Al 10 100 300',3],['Si_HfO2_Al 10 100 300',4],
# ['Si_HfO2_Al 10 75 400',0],['Si_HfO2_Al 10 100 400',5],['Si_HfO2_Al 10 75 500',3]]

# location2 = ['Si_HfO2_Al 10 100 500','Si_HfO2_Al 10 200 500','Si_HfO2_Al 10 75 X','Si_HfO2_Al 10 100 X','Si_HfO2_Al 10 200 400']

# for i in location: 
#     ap.allplot("T", "test", '%s'%i[0], 1, [i[1]], red)

for i in location2:
    ap.allplot("T", "rta", '%s'%i, 1, [1E-11,1E-4], [], set)