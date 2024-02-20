import os
import pandas as pd

class DataLoader:
    """Write a DataFrame to various destinations"""
    def __init__(self, df):
        self.df = df

    def to_json(self, path):
        self.df.to_json(path, orient='records')

    def to_csv(self, path):
        if not os.path.exists(path):
            self.df.to_csv(path, index=False)
        else:
            self.df.to_csv(path, mode='a', header=False, index=False)

    def to_db(self, engine, table_name):
        self.__normalize_df()
        if table_name == 'questions':
            formatted_df = self.format_questions_df()
        elif table_name == 'answers':
            formatted_df = self.format_answers_df()
        elif table_name == 'questions_comments':
            formatted_df = self.format_comments_df()
        elif table_name == 'answers_comments':
            formatted_df = self.format_comments_df()
        else:
            raise Exception('Invalid table name')
        formatted_df.to_sql(table_name, con=engine, if_exists='append', index=False)


    def format_questions_df(self):
        return self.df[['question_id', 'title', 'owner_id', 'owner_display_name', 'tags',
                                     'body', 'is_answered', 'score', 'answer_count', 'comment_count',
                                     'view_count', 'last_activity_date', 'creation_date', 'category', 'link']]

    def format_answers_df(self):
        return self.df[['answer_id', 'question_id', 'owner_id', 'owner_display_name',
                                     'body', 'is_accepted', 'score', 'comment_count',
                                     'last_activity_date', 'creation_date']]

    def format_comments_df(self):
        self.df['parent_id'] = self.df['post_id']
        return self.df[['comment_id', 'parent_id', 'owner_id', 'owner_display_name',
                                     'body', 'score', 'creation_date']]

    def __normalize_df(self):
        owners_df = pd.json_normalize(self.df['owner']).add_prefix('owner_')
        flattened_df = self.df.drop('owner', axis=1).join(owners_df)
        flattened_df['owner_id'] = flattened_df['owner_user_id']
        self.df = flattened_df
