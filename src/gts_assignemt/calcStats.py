import pandas as pd
import numpy as np



class calcTradesStats:
    def __init__(self,inputFile,outputFile):
        # ----------
        # Region Upload data
        # ----------
        print('Input Info...')
        input_data=pd.read_csv(inputFile)
        print('We loaded data frames with {0} records'.format(len(input_data)))
        with_nas=input_data.dropna()
        print('We drop {0} records due to incomplete dara'.format(len(input_data)-len(with_nas)))
        input_data=with_nas
        input_data.reset_index(inplace=True)
        print('After removing nas we left {0} records'.format(len(input_data)))
        # ----------
        # End Region Upload data
        # ----------

        # ---------
        # Region Build Extention
        # ---------
        d_grouped_by_symbol=self.groupedBySymbol(input_df=input_data,col_name=['Symbol'])
        d_grouped_by_exchange=self.groupedBySymbol(input_df=input_data,col_name=['FillExchange'])
        input_data=self.extend_buy_sell(input_df=input_data,
                                   symbol_grouped=d_grouped_by_symbol)

        input_data['SymbolPosition']=input_data['SymbolBought']-input_data['SymbolSold']
        input_data['SymbolNotional']=input_data.apply(lambda x:self.symbolNotional(x['FillSize'],x['FillPrice']),axis=1)
        input_data = self.extend_buy_sell_exchange(input_df=input_data,
                                          symbol_grouped=d_grouped_by_exchange)
        input_data=self.getTotalBought(input_df=input_data)
        input_data = self.getTotalSold(input_df=input_data)
        input_data=self.getTotalBoughtNotional(input_df=input_data)
        input_data = self.getTotalSoldNotional(input_df=input_data)
        # ---------
        # End Region Build Extention
        # ---------

        # ---------
        # Region Build Extention
        # ---------
        input_data.to_csv(outputFile)
        # ---------
        # Region Build Extention
        # ---------

        # ----------
        # Region Generate Results
        # ----------
        self.summaryStatistic(df_for_summary=input_data)
        # ----------
        # End Region Generate Results
        # ----------

    def summaryStatistic(self,df_for_summary):
        """
        Description
        -----------
        Function retrives data from extended data frame and provide basic statistics
        Args:
            df_for_summary: extended data frame

        Returns:
        None. Just print basic info about trades population
        """

        processed_trades=len(df_for_summary)
        average = df_for_summary['FillSize'].mean()
        total_bought = df_for_summary['TotalBought'].max()
        total_sold = df_for_summary['TotalSold'].max()
        total_volume=total_sold+total_bought
        notional_bought=df_for_summary['TotalBoughtNotional'].max()
        notional_sold = df_for_summary['TotalSoldNotional'].max()
        arr_different_exchanges=df_for_summary['FillExchange'].drop_duplicates().values
        median=self.getMedian(arr=df_for_summary['FillSize'])





        print("Processed Trades {0}".format(processed_trades))
        print('#-'*20)
        print('Shares Bought {0}'.format(total_bought))
        print('#-' * 20)

        print('Shares Sold {0}'.format(total_sold))
        print('#-' * 20)
        print("Total Volume: {0}".format(total_volume))
        print('#-' * 20)
        print("Notional Bought :${0:.2f}".format(notional_bought))

        print('#-' * 20)
        print("Notional Sold :${0:.2f}".format(notional_sold))
        print('#-' * 20)
        print("Per Exchange Volumes:")
        for i in arr_different_exchanges:
            print('{0} Bought {1}'.format(i,df_for_summary.query('FillExchange==@i')['ExchangeBought'].max()))
            print('{0} Sold {1}'.format(i, df_for_summary.query('FillExchange==@i')['ExchangeSold'].max()))

        print('#-' * 20)
        print("Averaged trades sized {0:.2f}".format(average))
        print("Median {0}".format(median))
        print('#-' * 20)






    def groupedBySymbol(self,input_df,col_name):
        """

        Args:
            input_df: basic df
            col_name: column tha=t is used to group

        Returns: prity dictionary that binds indexed with the same symbol or exchange flag

        """
        d_groups=input_df.groupby(col_name).groups
        return d_groups

    def symbolNotional(self,x,y):
        return x*y

    def getTotalBought(self,input_df):
        input_df['TotalBought'] = 0
        input_df.loc[0, 'TotalBought'] = input_df.loc[0, 'FillSize'] if input_df.loc[0, 'Side'] == 'b' else 0
        for i in input_df.index[1:]:

            if input_df.loc[i, 'Side']=='b':
                input_df.loc[i, 'TotalBought']=input_df.loc[i-1, 'TotalBought']+input_df.loc[i, 'FillSize']
            else:
                input_df.loc[i, 'TotalBought']=input_df.loc[i-1, 'TotalBought']
        return input_df


    def getTotalSold(self,input_df):
        input_df['TotalSold'] = 0
        input_df.loc[0, 'TotalSold'] = input_df.loc[0, 'FillSize'] if input_df.loc[0, 'Side'] == 't' or input_df.loc[0, 'Side'] == 's'  else 0
        for i in input_df.index[1:]:

            if input_df.loc[i, 'Side']=='t' or  input_df.loc[i, 'Side']=='s':
                input_df.loc[i, 'TotalSold']=input_df.loc[i-1, 'TotalSold']+input_df.loc[i, 'FillSize']
            else:
                input_df.loc[i, 'TotalSold']=input_df.loc[i-1, 'TotalSold']
        return input_df

    def getMedian(self,arr):
        """

        Args:
            arr: series from one of the column

        Returns: float median of array.

        """
        median=0
        arr=arr.to_numpy()
        arr=np.sort(arr)
        middle_index=int(len(arr)/2)
        if len(arr)%2!=0:
            median=arr[middle_index]
            return median
        else:
            median=(arr[middle_index]+arr[middle_index-1])//2
            return median

    def getTotalBoughtNotional(self,input_df):
        input_df['TotalBoughtNotional'] = 0
        input_df.loc[0, 'TotalBoughtNotional'] = input_df.loc[0, 'SymbolNotional'] if input_df.loc[0, 'Side'] == 'b' else 0
        for i in input_df.index[1:]:

            if input_df.loc[i, 'Side'] == 'b':
                input_df.loc[i, 'TotalBoughtNotional'] = input_df.loc[i - 1, 'TotalBoughtNotional'] + input_df.loc[i, 'SymbolNotional']
            else:
                input_df.loc[i, 'TotalBoughtNotional'] = input_df.loc[i - 1, 'TotalBoughtNotional']
        return input_df

    def getTotalSoldNotional(self,input_df):
        input_df['TotalSoldNotional'] = 0
        input_df.loc[0, 'TotalSoldNotional'] = input_df.loc[0, 'SymbolNotional'] if input_df.loc[0, 'Side'] == 't' or input_df.loc[0, 'Side'] == 's'  else 0
        for i in input_df.index[1:]:

            if input_df.loc[i, 'Side'] == 't' or input_df.loc[i, 'Side'] == 's':
                input_df.loc[i, 'TotalSoldNotional'] = input_df.loc[i - 1, 'TotalSoldNotional'] + input_df.loc[i, 'SymbolNotional']
            else:
                input_df.loc[i, 'TotalSoldNotional'] = input_df.loc[i - 1, 'TotalSoldNotional']
        return input_df



    def extend_buy_sell(self,input_df,symbol_grouped):
        input_df['SymbolBought']=0
        input_df['SymbolSold']=0

        for k in symbol_grouped:
            index_per_symbol=list(symbol_grouped[k].values)
            input_df.loc[index_per_symbol[0],'SymbolBought']=input_df.loc[index_per_symbol[0],'FillSize'] if input_df.loc[index_per_symbol[0],'Side']=='b' else 0
            for j in range(1,len(index_per_symbol)):
                if input_df.loc[index_per_symbol[j], 'Side'] == 'b':
                    input_df.loc[index_per_symbol[j], 'SymbolBought'] = input_df.loc[index_per_symbol[j], 'FillSize']+input_df.loc[index_per_symbol[j-1], 'SymbolBought']
                else:
                    input_df.loc[index_per_symbol[j], 'SymbolBought'] += input_df.loc[index_per_symbol[j-1], 'SymbolBought']
        for k in symbol_grouped:
            index_per_symbol=list(symbol_grouped[k].values)
            input_df.loc[index_per_symbol[0],'SymbolSold']=input_df.loc[index_per_symbol[0],'FillSize'] if input_df.loc[index_per_symbol[0],'Side']=='t' else 0
            for j in range(1,len(index_per_symbol)):
                if input_df.loc[index_per_symbol[j], 'Side'] == 't':
                    input_df.loc[index_per_symbol[j], 'SymbolSold'] = input_df.loc[index_per_symbol[j], 'FillSize']+input_df.loc[index_per_symbol[j-1], 'SymbolSold']
                else:
                    input_df.loc[index_per_symbol[j], 'SymbolSold'] += input_df.loc[index_per_symbol[j-1], 'SymbolSold']

        return input_df


    def extend_buy_sell_exchange(self,input_df,symbol_grouped):
        input_df['ExchangeBought']=0
        input_df['ExchangeSold']=0

        for k in symbol_grouped:
            index_per_symbol=list(symbol_grouped[k].values)
            input_df.loc[index_per_symbol[0],'ExchangeBought']=input_df.loc[index_per_symbol[0],'FillSize'] if input_df.loc[index_per_symbol[0],'Side']=='b' else 0
            for j in range(1,len(index_per_symbol)):
                if input_df.loc[index_per_symbol[j], 'Side'] == 'b':
                    input_df.loc[index_per_symbol[j], 'ExchangeBought'] = input_df.loc[index_per_symbol[j], 'FillSize']+input_df.loc[index_per_symbol[j-1], 'ExchangeBought']
                else:
                    input_df.loc[index_per_symbol[j], 'ExchangeBought'] += input_df.loc[index_per_symbol[j-1], 'ExchangeBought']
        for k in symbol_grouped:
            index_per_symbol=list(symbol_grouped[k].values)
            input_df.loc[index_per_symbol[0],'ExchangeSold']=input_df.loc[index_per_symbol[0],'FillSize'] if input_df.loc[index_per_symbol[0],'Side']=='t' or input_df.loc[index_per_symbol[0],'Side']=='s' else 0
            for j in range(1,len(index_per_symbol)):
                if input_df.loc[index_per_symbol[j], 'Side'] == 't' or input_df.loc[index_per_symbol[j], 'Side'] == 's':
                    input_df.loc[index_per_symbol[j], 'ExchangeSold'] = input_df.loc[index_per_symbol[j], 'FillSize']+input_df.loc[index_per_symbol[j-1], 'ExchangeSold']
                else:
                    input_df.loc[index_per_symbol[j], 'ExchangeSold'] += input_df.loc[index_per_symbol[j-1], 'ExchangeSold']

        return input_df

if __name__ =="__main__":
    
    trades_blotter=calcTradesStats(inputFile="SampleInput.csv",
                                   outputFile="enrichedTrades.csv"

                                   )
