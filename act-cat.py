import pandas as pd
import csv

# #acts_sections refers to act_key for acts under which cases were filed
# acf = pd.read_csv('../csv/acts_sections.csv', nrows=10)
# print(acf)

# c10f = pd.read_csv('../csv/cases/cases_2010.csv', nrows=10)
# print(c10f)

# akeyf = pd.read_csv('../csv/keys/act_key.csv', nrows=10)
# print(akeyf)

crimes_set = {'509', '304B', '365', 'Immoral Traffic', '354', '511', 
            'Dowry', '376', 'Sati', '364', '306', '366', '367', '368', '369',
            '364A', 'Indecent Representation', 'Women', 'Woman', 'domestic Violence', 
            '363', '498A'}


#go through act_key and create dataframe of act keys related to crimes against women
act_key_df = pd.read_csv('./csv/keys/act_key.csv')
print(act_key_df)

# relevant_keys_df = act_key_df.loc[act_tok in crimes_set for act_tok in act_key_df['act_s']]

act_key_df['tokens'] = act_key_df['act_s'].apply(lambda x: str(x).split())
act_key_df['matches'] = act_key_df['tokens'].apply(lambda x: list(crimes_set.intersection(x)))
act_key_df['is_against_women'] = act_key_df['matches'].apply(lambda x: True if x else False)
print(act_key_df)

acts_true_df = act_key_df.loc[act_key_df['is_against_women']==True]
print(acts_true_df)
'''
relevant_keys_df - dataframe which is subset of act_key where only crimes relating to women
                included
'''
print(relevant_keys_df)
print('print(relevant_keys_df)==============DONE==============')

#go through acts_sections to find cases
acts_sections_df = pd.read_csv('./csv/acts_sections.csv')


#add something to read all cases files into one dataframe or join their dataframes
relevant_ddls_df = acts_sections_df.loc(acts_sections_df['act'] in relevant_keys_df['act'].unique())


all_cases_df = pd.read_csv('./csv/cases/cases_2010.csv') # READ ALL RELEVANT YEAR FILES INTO ONE DF OR JOIN THEIR DFS

relevant_cases_df = all_cases_df.loc(all_cases_df['ddl_case_id'] in relevant_ddls_df['ddl_case_id'].unique())

pd.options.display.max_rows = 10
print(relevant_cases_df)
#find cases from joint dataframe where act key refers to a crime against women
