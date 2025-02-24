# Databricks notebook source
# Create class to read data from a certain layer and its children classes
from abc import abstractmethod, ABC
from typing import List
from pyspark.sql import DataFrame

class Reader(ABC):
    def __init__(self, location: str, file_names: List[str] = [], file_list: List[DataFrame]=[]):
        self.location = location
        self.file_names = []
        self.file_list = []
        
    def set_file_names(self) -> None:
        location_dir = dbutils.fs.ls(self.location)
        file_names = [file_name.name.split('/')[0] for file_name in location_dir]
        
        self.file_names = file_names
        
    @abstractmethod
    def set_file_list(self) -> None:
        pass
        
class CsvReader(Reader):
    def set_file_list(self) -> None:
        file_list = []
        for file_name in self.file_names:
            curr_file = spark.read.option("delimiter", ";").csv(f"{self.location}{file_name}/", header=True)
            file_list.append(curr_file)
        
        self.file_list = file_list

class DeltaReader(Reader):
    def set_file_list(self) -> None:
        file_list = []
        for file_name in self.file_names:
            curr_file = spark.read.format('delta').load(f'{self.location}{file_name}/')
            file_list.append(curr_file)

        self.file_list = file_list

# COMMAND ----------

# Create class to write data in the necessary layer
class Writer():
    def __init__(self, location: str, file_names: List[str] = [], file_list: List[DataFrame] = []):
        self.location = location
        self.file_names = file_names
        self.file_list = file_list
        
    def write_files (self) -> None:
        for file, file_name in zip(self.file_list, self.file_names):
            (file
                .coalesce(1)
                .write
                .format('delta')
                .mode('overwrite')
                .save(f'{self.location}{file_name}')
            )
 