import numpy as np
import pandas as pd
from evaluation_template import evaluation_template 

class MSE(evaluation_template):
    def setup_method(self):
        pass
     
    def evaluate_prediction_method(self):
        Error = 0
        for i_sample in range(len(self.Output_path_pred)):
            (num_poss, num_timesteps_out) = self.Output_path_pred.iloc[i_sample, 0].shape
            diff = np.zeros((num_poss, num_timesteps_out))
            for j in range(len(self.Output_path.columns)):
                diff += (self.Output_path_pred.iloc[i_sample, j] -
                         self.Output_path.iloc[i_sample, j][np.newaxis,:]) ** 2
            diff = np.sqrt(diff)   
            
            Error += np.mean(diff)
        return [Error / len(self.Output_path_pred)]
    
    
    def get_output_type_class(self = None):
        return 'path'
    
    def get_t0_type():
        return 'col'
    
    def get_name(self):
        return 'MSE'
    
    def requires_preprocessing(self):
        return False
    
    def allows_plot(self):
        return False