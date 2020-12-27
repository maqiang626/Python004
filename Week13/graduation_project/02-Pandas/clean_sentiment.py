import numpy as np
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from snownlp import SnowNLP


pymysql_connect = pymysql.connect(host='192.168.59.220',
                                  port=3306,
                                  user='root',
                                  password='MRP@Tmp59220',
                                  database='db_w13',
                                  charset='utf8mb4'
                                  )


def get_original_data():
    '''从数据库中获取原始评论数据
    '''

    sql = "SELECT id,title,alink,comment,crawling_date FROM tb_original_comments"
    df = pd.read_sql(sql, pymysql_connect)

    return df


def data_clean(df):
    '''对评论数据进行清洗
    '''

    # 去除重复值
    df.drop_duplicates(subset=['comment'], keep='first', inplace=True)

    # 去除缺失值
    df['comment'].replace(' ', np.NaN, inplace=True)
    df['comment'].replace('', np.NaN, inplace=True)
    df.dropna(subset=['comment'], how='any', inplace=True)

    return df


def semantic_analysis(df):
    '''对清洗后的数据进行语义情感分析
    '''

    for i, row in df.iterrows():
        comment = row['comment']
        sentiment = SnowNLP(comment).sentiments
        df.loc[[i], ['sentiment']] = sentiment

    return df


def analysis_tosql(df):
    '''DataFrame 数据（经过语义情感分析后的数据）存入数据库
    '''

    con = create_engine(
        'mysql+pymysql://root:MRP@Tmp59220@192.168.59.220:3306/db_w13?charset=utf8mb4')
    df.to_sql('tb_semantic_emotion', con=con, if_exists='replace', index=None)


def sentiment_tosql(df):
    '''舆情分析的结果存入到 MySQL 数据库中
    '''

    # 舆情分析
    counter = len(df)
    sentiment_avg = round(df['sentiment'].mean(), 2)
    crawling_date_latest = df['crawling_date'].max()
    plus = len(df[df['sentiment'] >= sentiment_avg])
    minus = len(df[df['sentiment'] < sentiment_avg])

    # 存入数据库
    connect_cursor = pymysql_connect.cursor()
    insert_sql = 'INSERT INTO tb_sentiment_analysis(counter, crawling_date_latest, sentiment_avg, plus, minus) values(%s, %s, %s, %s, %s)'
    insert_value = (counter, str(crawling_date_latest),
                    str(sentiment_avg), plus, minus)
    connect_cursor.execute(insert_sql, insert_value)
    connect_cursor.close()
    pymysql_connect.commit()
    pymysql_connect.close()


if __name__ == '__main__':
    df_original = get_original_data()
    df_cleaned = data_clean(df_original)
    df_analyzed = semantic_analysis(df_cleaned)
    analysis_tosql(df_analyzed)
    sentiment_tosql(df_analyzed)
