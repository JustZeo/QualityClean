from abc import ABC,abstractmethod

import polars  as pl 

class BaseRule(ABC):
    @abstractmethod
    def run(self,df:pl.DataFrame,**kwargs,)-> pl.DataFrame:
        pass
