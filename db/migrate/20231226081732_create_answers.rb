class CreateAnswers < ActiveRecord::Migration[7.0]
  def change
    create_table :answers, id: false do |t|
      t.bigint :answer_id, primary_key: true
      t.string :owner_id
      t.string :owner_display_name
      t.bigint :question_id, null: false, foreign_key: true
      t.text :body
      t.boolean :is_accepted
      t.integer :comment_count
      t.integer :score
      t.integer :last_activity_date
      t.integer :creation_date
    end

    add_foreign_key :answers, :questions, column: :question_id, primary_key: :question_id
  end
end
