class CreateCodes < ActiveRecord::Migration[7.0]
  def change
    create_table :codes do |t|
      t.string :name, null: false
      t.text :description
      t.references :parent, foreign_key: { to_table: :codes }
      t.timestamps
    end

    create_table :codes_sentences do |t|
      t.references :code, foreign_key: true
      t.references :sentence, foreign_key: true
      t.timestamps
    end
  end
end
