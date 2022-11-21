import pandas as pd
from datetime import datetime, timedelta
class ProcessDataService:

    @staticmethod
    def datetime_range(start: datetime, end: datetime, delta: timedelta):
        """Returns a generator of all the timestamps"""

        current = start
        while current < end:
            yield current
            current += delta

    @staticmethod
    def generate_empty_buckets(start: datetime, end: datetime, freq: int = 1):
        """Generates a list with all the buckets by frequency"""

        return [dt.strftime('%Y-%m-%d %H:%M:00') for dt in 
        ProcessDataService.datetime_range(start, end,
        timedelta(minutes=freq))]

    @staticmethod
    def group_data_by_freq(raw_data: pd.DataFrame , freq: int = 1):
        """Pre-processes the dataframe to have buckets based on the frequency (in minutes). Default is 1 minute"""

        dts = ProcessDataService.generate_empty_buckets(raw_data.iloc[0].timestamp, raw_data.iloc[-1].timestamp + timedelta(minutes = 1))
        
        #data frame with buckets and empty lists inside
        #index is the timestamp to avoid O(n^2)
        df = pd.DataFrame(index = dts)
        df['duration'] = [list() for x in range(len(df.index))]
        
        #iterate over events and puts it in the right bucket.
        #Only if the event has an exact timespant should be in that bucket, 
        #otherwise should always overflow to the next bucket
        for index, row in raw_data.iterrows():
            t = row.timestamp
            t_rounded = t.round('T')

            #should go to next bucket
            if t > t_rounded:
                indice = t_rounded + timedelta(minutes = freq)
            else:
                indice = t_rounded
            
            df.at[indice, 'duration'] = df.loc[str(indice)]['duration'].append(row.duration)
        df = df.dropna()
        
        #convert bucket lists in average
        for index, row in df.iterrows():
            if len(row['duration']) > 0:
                row['duration'] = sum(row['duration']) / len(row['duration'])
            else:
                row['duration'] = 0
        df = df.reset_index()
        df = df.rename(columns={'index': 'timestamp'})
        
        return df