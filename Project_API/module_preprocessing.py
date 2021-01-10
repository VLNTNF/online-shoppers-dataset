import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import pickle

def datapreprocessing(array):

    model = pickle.load(open('minmaxscaler_model.pickel','rb'))

    col = ['Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues','SpecialDay','Month','OperatingSystems','Browser','Region','TrafficType','VisitorType','Weekend']
    data = pd.DataFrame(data=array,index=[1], columns=col)
    
    temp = [[0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,1,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Mar",2,2,2,2,"New_Visitor","True"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"May",3,3,3,3,"Other","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Jun",4,4,4,4,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Jul",5,5,5,5,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Aug",6,6,6,6,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Sep",7,7,7,7,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Oct",8,8,8,8,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Nov",1,9,1,9,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Dec",1,10,1,10,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,11,1,11,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,12,1,12,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,13,1,13,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,14,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,15,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,16,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,17,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,18,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,19,"Returning_Visitor","False"],
            [0,0.0,0,0.0,1,0.000000,0.20,0.20,0.0,0.0,"Feb",1,1,1,20,"Returning_Visitor","False"]]
    temp_index = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    temp_df = pd.DataFrame(data=temp, index=temp_index, columns=col)
    
    data = pd.concat([data, temp_df])
    
    data['Month'] = data['Month'].astype('category')
    data['OperatingSystems'] = data['OperatingSystems'].astype('int')
    data['OperatingSystems'] = data['OperatingSystems'].astype('category')
    data['Browser'] = data['Browser'].astype('int')
    data['Browser'] = data['Browser'].astype('category')
    data['Region'] = data['Region'].astype('category')
    data['TrafficType'] = data['TrafficType'].astype('int')
    data['TrafficType'] = data['TrafficType'].astype('category')
    data['VisitorType'] = data['VisitorType'].astype('category')
    data['Weekend'] = data['Weekend'].astype('category')
    data['Administrative_Duration'] = data['Administrative_Duration'].astype('float32')
    data['Administrative'] = data['Administrative'].astype('float32')
    data['Informational_Duration'] = data['Informational_Duration'].astype('float32')
    data['Informational'] = data['Informational'].astype('float32')
    data['ProductRelated'] = data['ProductRelated'].astype('float32')
    data['ProductRelated_Duration'] = data['ProductRelated_Duration'].astype('float32')
    data['BounceRates'] = data['BounceRates'].astype('float32')
    data['ExitRates'] = data['ExitRates'].astype('float32')
    data['PageValues'] = data['PageValues'].astype('float32')
    data['SpecialDay'] = data['SpecialDay'].astype('float32')


    del(data['ProductRelated'])
    del(data['ExitRates'])
    del(data['Region'])
    
    data['ratio_administrative'] = data['Administrative_Duration']/data['Administrative']
    data['ratio_administrative'] = data['ratio_administrative'].fillna(0)

    data['ratio_informational'] = data['Informational_Duration']/data['Informational']
    data['ratio_informational'] = data['ratio_informational'].fillna(0)

    # Suppression des varaibles qui nous ont servi à en créer de nouvelles
    del(data['Administrative'])
    del(data['Administrative_Duration'])
    del(data['Informational'])
    del(data['Informational_Duration'])
    
    # Variable 'Month'
    dummies = pd.get_dummies(data['Month'],drop_first=True, prefix='Month', prefix_sep='_')
    data = pd.concat([data, dummies], axis=1)
    del(data['Month'])

    # Variable 'OperatingSystems'
    dummies = pd.get_dummies(data['OperatingSystems'],drop_first=True, prefix='OperatingSystems', prefix_sep='_')
    data = pd.concat([data, dummies], axis=1)
    del(data['OperatingSystems'])

    # Variable 'Browser'
    dummies = pd.get_dummies(data['Browser'],drop_first=True, prefix='browser', prefix_sep='_')
    data = pd.concat([data, dummies], axis=1)
    del(data['Browser'])

    # Variable 'TrafficType'
    dummies = pd.get_dummies(data['TrafficType'],drop_first=True, prefix='TrafficType', prefix_sep='_')
    data = pd.concat([data, dummies], axis=1)
    del(data['TrafficType'])

    # Variable 'VisitorType'
    dummies = pd.get_dummies(data['VisitorType'],drop_first=True, prefix='VisitorType', prefix_sep='_')
    data = pd.concat([data, dummies], axis=1)
    del(data['VisitorType'])

    # Variable 'Weekend'
    dummies = pd.get_dummies(data['Weekend'],drop_first=True, prefix='Weekend', prefix_sep='_')
    data = pd.concat([data, dummies], axis=1)
    del(data['Weekend'])
    
    data = data[data.index==1]
    data = data.values

    data = model.transform(data)
    
    return data