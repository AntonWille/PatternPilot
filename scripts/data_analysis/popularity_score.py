import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text as alch_text

query = """
        SELECT q.category as "category",
            AVG(q.score) AS "avg_question_score",
            AVG(a.score) AS avg_answer_score,
            AVG(q.comment_count + a.comment_count) AS avg_comment_count
        FROM public.questions q
        LEFT JOIN public.answers a ON q.question_id = a.question_id
        GROUP BY q.category
        """

def plot_popularity(df):
    fig, ax = plt.subplots(figsize=(10, 7))
    categories = df['category']
    x = range(len(categories))
    bar_width = 0.25

    # Plot each metric in a grouped bar
    ax.bar(x, df['avg_question_score'], bar_width, label='Avg. Q Score')
    ax.bar([p + bar_width for p in x], df['avg_answer_score'], bar_width, label='Avg. A-Score')
    ax.bar([p + bar_width * 2 for p in x], df['avg_comment_count'], bar_width, label='Avg. Comment Count')

    # Add some text for labels, title, and custom x-axis tick labels, etc.
    ax.set_xlabel('Category')
    ax.set_ylabel('Scores')
    ax.set_title('Average Scores and Comment Count by Category')
    ax.set_xticks([p + bar_width for p in x])
    ax.set_xticklabels(categories)
    ax.legend()

    # Rotate the tick labels for better readability
    plt.xticks(rotation=45)

    # Make layout tight to handle long labels
    plt.tight_layout()

    # Save the figure
    fig.savefig('average_scores_by_category.png', dpi=300)  # Adjust the path and file name as needed

def main():
    engine = create_engine('postgresql://postgres@localhost:5432/pattern_pilot_development')
    with engine.connect() as conn:
        df = pd.read_sql(alch_text(query), conn)
        plot_popularity(df)

if __name__ == "__main__":
    main()
