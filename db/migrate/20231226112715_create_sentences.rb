class CreateSentences < ActiveRecord::Migration[7.0]
  def change
    create_table :sentences do |t|
      t.string :post_type, null: false
      t.bigint :post_id, null: false
      t.integer :sequence_number
      t.text :sentence_text
      t.timestamps
    end
  end
end
