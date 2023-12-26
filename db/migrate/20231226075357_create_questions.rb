class CreateQuestions < ActiveRecord::Migration[7.0]
  def change
    create_table :questions, id: false do |t|
      t.bigint :question_id, primary_key: true
      t.string :title
      t.string :owner_id
      t.text :body
      t.boolean :is_answered
      t.integer :answer_count
      t.integer :comment_count
      t.integer :view_count
      t.integer :score
      t.string :link
      t.integer :last_activity_date
      t.integer :creation_date
      t.timestamps
    end
  end
end
