import pandas as pd
import os
from datetime import datetime

from handlers.event_handler import EventHandler
from services.process_data_service import ProcessDataService

def test_group_data_by_freq():
    """Should pre-process a dataframe to have buckets based on the frequency"""

    json_path = os.path.join(os.path.dirname(__file__), '../../../data/inputs/input.json')
    df = EventHandler.convert_json_to_df(json_path)
    result = ProcessDataService.group_data_by_freq(df)
    assert len(result) == 14
    assert result.columns.values.tolist() == ['timestamp', 'duration']
    assert result.duration.values.tolist() == [0.0, 20.0, 0.0, 0.0, 0.0, 31.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 54.0]

def test_generate_empty_buckets():
    """Should should create a list of buckets"""

    
    start = datetime.strptime('2022-12-26 18:11:00', '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime('2022-12-26 18:31:00', '%Y-%m-%d %H:%M:%S')

    buckets = ProcessDataService.generate_empty_buckets(start, end)
    
    assert len(buckets) == 20