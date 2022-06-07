# 사고사례읽기
import pandas as pd

def get_accident_case(path):
    df = pd.read_csv(path)
    print(df.head())
    print(df.columns)
    print(len(df))
    df1 = df[['사고경위']]
    df1.rename(columns = {'사고경위' : 'sentence'}, inplace = True)
    print(len(df1))
    df2 = df[['구체적 사고원인']]
    df2.rename(columns = {'구체적 사고원인' : 'sentence'}, inplace = True)
    print(len(df2))
    new_df = pd.concat([df1,df2])
    print(len(new_df))
    print(new_df.head())
    return new_df


def trian_csv_to_df(path):
    df = pd.read_csv(path)
    df = df[['sentence']]
    print(df.head())
    return df

def train_DF_to_csv(train_DF, save_dir):
    file_name = 'train_GJ&case.csv'
    # with open(save_dir+'/'+file_name, 'w') as file: 
    #     writer = csv.writer(file) 
    #     writer.writerow(train_DF)
    train_DF.to_csv(save_dir+'/'+file_name)
    return "done"

train_csv_path = '/Users/namcheolher/aiffel/Safety_Helmet/code_txt_to_df/db_df_result/tf_idf_train_GJ&info.csv'
accident_case_path = '/Users/namcheolher/aiffel/Safety_Helmet/accident_case/accident_case_rawdata/accident_case_col.csv'

GJ_df = trian_csv_to_df(train_csv_path)
case_df = get_accident_case(accident_case_path)
train_GJ_case = pd.concat([GJ_df,case_df])
print(GJ_df.columns)
print(case_df.columns)
print(train_GJ_case.columns)
print(len(GJ_df))
print(len(case_df))
print(len(train_GJ_case))

save_dir = '/Users/namcheolher/aiffel/Safety_Helmet/code_txt_to_df/db_df_result'

train_DF_to_csv(train_GJ_case, save_dir)


